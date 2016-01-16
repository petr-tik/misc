#!/usr/bin/python


# Craig Turner's swamp monster game

import os
import random
import sys
import time

import termios
import tty

# --------------------------------------------------------
#   static
# --------------------------------------------------------
KEY_ESC = 27
KEY_ENTER = 13
KEY_SPACE = 32

SPACE_BUFFER = ' '*5
NSPACE_BUFFER = '\n%s'%SPACE_BUFFER

COUNT_STATUS_LINES_RESERVED = 5

ROWSIZE = 12
COLSIZE = 30

COLOURS = { 'blue': '\033[94m'
          , 'green': '\033[92m'
          , 'yellow': '\033[93m'
          , 'red': '\033[91m'
          }
ENDC = '\033[0m'


# --------------------------------------------------------
#   entity statics
# --------------------------------------------------------
ENTITY_SIZE_MULTIPLE = 5

ES_PILL = 1
ES_RING = ES_PILL * ENTITY_SIZE_MULTIPLE
ES_VIAL = ES_RING * ENTITY_SIZE_MULTIPLE
ES_TOOL = ES_VIAL * ENTITY_SIZE_MULTIPLE
ES_TOME = ES_TOOL * ENTITY_SIZE_MULTIPLE
ES_STOOL = ES_TOME * ENTITY_SIZE_MULTIPLE
ES_PLINTH = ES_STOOL * ENTITY_SIZE_MULTIPLE
ES_WALL = ES_PLINTH * ENTITY_SIZE_MULTIPLE


# --------------------------------------------------------
#   space statics
# --------------------------------------------------------
SPACE_CAPACITY = ES_WALL


# --------------------------------------------------------
#   context struct
# --------------------------------------------------------
#
# This gives us a namespace that we can pass around the
# program. It's a centralised place for storing game
# state, and a the place to start when you want to reach
# an object known to the game.
#
class Context(object):
    def __init__(self):
        self.keep_running = True
        self.exit_message = None
        self.turn_counter = 0

        self.io = None

        self.status = []

        # int v object
        self.planes = {}
        self.unique_plane_idx = -1
        #
        # fairies
        self.fairies = []
        self.player = None
        self.lady_of_the_lake = None
        #
        # feature planes
        self.island_plane = None
        self.water_spots = []
    def player_plane(self):
        return self.player.ent.owner.plane
    def retain_plane(self, plane):
        self.unique_plane_idx += 1
        plane.unique_id = self.unique_plane_idx
        self.planes[self.unique_plane_idx] = plane
    def release_plane(self, plane_id):
        del self.planes[plane_id]


# --------------------------------------------------------
#   io
# --------------------------------------------------------
class UnixIo(object):
    def __init__(self, context):
        self.context = context
    def clear_screen(self):
        os.system('clear')
        #print chr(27) + "[2J"
    def getchar(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    def ask_yn(self, msg, default, clear=True):
        def say_no():
            print 'No'
            time.sleep(0.1)
        def say_yes():
            print 'Yes'
            time.sleep(0.1)

        if clear:
            self.clear_screen()

        print '\n%s'%msg,
        if None != default:
            if default:
                print "[y]"
            else:
                print "[n]"
        else:
            print
        r = self.getchar()
        if r in ['y', 'Y']:
            say_yes()
            return True
        if r in ['n', 'N']:
            say_no()
            return False

        if default:
            say_yes()
            return True
        else:
            say_no()
            return False
    def get_wordy_input(self):
        sys.stdout.write(':')
        input = raw_input()
        return input
    def redraw(self, lines, with_status=False):
        status_buffer = COUNT_STATUS_LINES_RESERVED - len(self.context.status)

        sb = []
        #
        # status messages, or gaps in their stead
        for i in range(status_buffer):
            sb.append('')
        if with_status:
            sb.extend(self.context.status)
        #
        # render the supplied lines
        sb.extend(lines)

        out = "%s%s"%(SPACE_BUFFER, NSPACE_BUFFER.join(sb))

        self.clear_screen()
        print out


# --------------------------------------------------------
#   container
# --------------------------------------------------------
#
# A container holds entities. e.g. a player's inventory. The
# base case looks very much like a list, but containers need
# logic for things like capacity checking and placement.
#
# Entities always reside in something that quacks like a
# container.
#
class Container(object):
    def __init__(self):
        self.within = []
    def contained(self):
        return self.within[:]
    def add(self, ent):
        """Don't call this directly. Use move_ent, because
        this takes responsibility for reassigning the
        owner."""
        self.within.append(ent)
    def remove(self, ent):
        self.within.remove(ent)
    def get_position(self):
        """Returns a three-item tuple representing the
        global coordinate position of this container,
        (level, row, column)"""
        raise Exception("Needs to be implemented.")


# --------------------------------------------------------
#   mapping
# --------------------------------------------------------
#
# Planes are composed of Space.
#
class Plane(object):
    def __init__(self, context, rowsize, colsize):
        self.unique_id = None

        self.context = context
        self.rowsize = rowsize
        self.colsize = colsize

        self.d_space = {}
    def retain_entity(self, row, col, placement):
        coords = (row, col)
        self.placements[coords] = placement
    def release_entity(self, entity):
        ridx, cidx = [(r, c) for (r, c), p in self.placements.items() if p == entity][0]
        coords = (ridx, cidx)
        del self.placements[coords]
    def render(self):
        rows = []
        for ridx in xrange(self.rowsize):
            sb = []
            for cidx in xrange(self.colsize):
                sb.append(self.d_space[ (ridx, cidx) ].symbol())
            rows.append(sb)
        return [''.join(colchars) for colchars in rows]
    def move(self, ent, keypad_cardinal):
        #
        # Work out the desired coordinate
        plane_id, old_ridx, old_cidx = ent.owner.get_position()
        plane = self.context.planes[plane_id]
        nrow, ncol = old_ridx, old_cidx
        if keypad_cardinal in (1,2,3):
            nrow += 1
        if keypad_cardinal in (1,4,7):
            ncol -= 1
        if keypad_cardinal in (3,6,9):
            ncol += 1
        if keypad_cardinal in (7,8,9):
            nrow -= 1
        #
        # Validate it's within map bounds
        val_msg = "You escaped! Well done."
        if nrow < 0 or nrow > self.rowsize-1:
            if ent.name == ENT_PLAYER:
                self.context.exit_message = val_msg
                self.context.keep_running = False
            return
        elif ncol < 0 or ncol > self.colsize-1:
            if ent.name == ENT_PLAYER:
                self.context.exit_message = val_msg
                self.context.keep_running = False
            return
        new_space = self.d_space[(nrow, ncol)]
        #
        # If the user has motioned towards claimed space, that's
        # an interaction rather than movement.
        lst_cl = new_space.claimants()
        if lst_cl:
            for cl in lst_cl:
                if ent.sentient and cl.sentient:
                    ent.sentient_interaction(cl)
                    return
            if ent.name == ENT_PLAYER:
                status(self.context, "You bump into a %s"%lst_cl[-1].name)
            return
        #
        # Player can't move into water.
        if new_space.surface.within[-1].name == ENT_WATER:
            if ent.name == ENT_PLAYER:
                m = random.choice( [ "But it's much warmer out here."
                                   , "You can't swim."
                                   , "The water looks dirty."
                                   , "You can't walk on that!"
                                   , "You splash your toes in the water"
                                   , "You might sink"
                                   , "Your wouldn't want your crowbar to get rusty."
                                   , "You're scared of water"
                                   , "No way - there might be sharks!"
                                   ] )
                self.context.status.append(m)
                return
        #
        # Do the move
        move_ent(ent, new_space)
        #
        # If the user isn't the player, we allow them to
        # mess up any well-cultivated sand
        if ent.name != ENT_PLAYER:
            surface = new_space.surface.within[-1]

def create_plane(context, rowsize, colsize):
    plane = Plane(context, rowsize, colsize)
    context.retain_plane(plane)
    #
    # Prepare the space containers in the plane
    for ridx in xrange(plane.rowsize):
        for cidx in xrange(plane.colsize):
            space = create_space(plane.context, plane, ridx, cidx)
            plane.d_space[ (ridx, cidx) ] = space

    return plane

def merge_plane_onto_plane(context, source_plane, target_plane, t_ridx_offset, t_cidx_offset):
    """Merges all of source onto target, using (t_ridx_offset, t_cidx_offset)
    as the top-left point at which to start merging."""
    for ridx in xrange(source_plane.rowsize):
        for cidx in xrange(source_plane.colsize):
            space = source_plane.d_space[ (ridx, cidx) ]
            space.plane = target_plane
            space.ridx = ridx + t_ridx_offset
            space.cidx = cidx + t_cidx_offset
            t_coords = ( space.ridx
                       , space.cidx
                       )
            target_plane.d_space[t_coords] = space

class SpaceContainer(object):
    def __init__(self, context, plane, ridx, cidx):
        self.context = context
        self.capacity = SPACE_CAPACITY
        self.surface = Container()
        self.within = []
        self.plane = plane
        self.ridx = ridx
        self.cidx = cidx
    def contained(self):
        return self.within[:]
    def claimants(self):
        return [e for e in self.within if e.claims_space]
    def add(self, ent):
        self.within.append(ent)
    def remove(self, ent):
        self.within.remove(ent)
    def symbol(self):
        ent = self.top_ent()
        if ent:
            return str(ent)
        else:
            return str(self.surface.within[-1])
    def top_ent(self):
        if not self.within:
            return None
        for ent in self.within:
            if ent.claims_space:
                return ent
        return self.within[-1]
    def get_position(self):
        """Returns a three-item tuple representing the
        global coordinate position of this container,
        (level, row, column)"""
        return (self.plane.unique_id, self.ridx, self.cidx)

def create_space(context, plane, ridx, cidx):
    space = SpaceContainer(context, plane, ridx, cidx)
    declare_water(context, space.surface)
    return space


# --------------------------------------------------------
#   feature planes
# --------------------------------------------------------
#
# You create structures on a plane of their own, and then
# copy them onto the player's current plane. You should
# either create the plane once and store it in context so
# you can reuse it, or else be vigilant to deallocate the
# plane once you're done with it! :)
#
def declare_island_plane(context):
    plane = create_plane( context
                        , rowsize=8
                        , colsize=10
                        )
    sketch = [ 'xxxxxxxxxx'
             , 'xxx....xxx'
             , 'xx......xx'
             , 'x.......xx'
             , 'x........x'
             , 'x........x'
             , 'xx......xx'
             , 'xxxxxxxxxx'
             ]
    def replace_water_with_dirt(context, space):
        space.surface.within.pop()
        declare_dirt(context, space.surface)
    legend = { 'x': None
             , '.': lambda context, container: replace_water_with_dirt(context, container)
             }
    for ridx, row in enumerate(sketch):
        for cidx, cell in enumerate(row):
            setup_fn = legend[cell]
            if setup_fn:
                container = plane.d_space[ (ridx, cidx) ]
                setup_fn(context, container)
    randomish_mangroves_and_stuff(context, plane)

    context.island_plane = plane


# --------------------------------------------------------
#   entity foundations
# --------------------------------------------------------
#
# An entity is anything that can have a sprite in the world.
# So a table, a c
#
class Entity(object):
    def __init__(self):
        self.c = None
        self.name = None
        self.size = None
        self.mass = None
        self.inv = None
        self.colour = None
        # sentience indicates that moving into it should check
        # for a custom interaction.
        self.sentient = False
        self.sentient_fn = None
        # container this sits in
        self.owner = None
        # a piece of space can't be claimed by more than
        # one entity.
        self.claims_space = False
        # can it be picked up?
        self.mobile = True
        #
        # item-specific properties and functions
        self.d = {}
        #
        # plugin functions
        self.desc_fn = None
        self.apply_fn = None
        self.wet_fn = None
    def __repr__(self):
        if None == self.colour:
            return self.c
        return ''.join( [ COLOURS[self.colour]
                        , self.c
                        , ENDC
                        ] )
    def apply(self, context):
        if not self.apply_fn:
            # shouldn't get here
            context.status.append("Your developer is a muppet. (apply)")
            return
        self.apply_fn(self, context)
    def desc(self):
        """This is default, but you can override it by setting
        desc_fn."""
        if self.desc_fn:
            return self.desc_fn(self)
        else:
            return self.name
    def sentient_interaction(self, acc):
        """Pass in the entity with which you're interacting as the
        accusative."""
        if self.sentient_fn == None:
            # shouldn't get here
            self.context.status.append("Your developer is a muppet. (sent.i)")
            return
        self.sentient_fn( nom=self
                        , acc=acc
                        )
    def wet(self):
        if self.wet_fn:
            self.wet_fn()

class InventoryContainer(object):
    def __init__(self, entity):
        self.entity = entity
        self.within = []
    def contained(self):
        return self.within
    def add(self, ent):
        self.within.append(ent)
    def remove(self, ent):
        self.within.remove(ent)
    def get_position(self):
        return self.entity.owner.get_position()

def create_entity(container, c, name, size, colour=None, claims_space=False, mobile=True):
    ent = Entity()
    ent.c = c
    ent.name = name
    ent.size = size
    ent.inv = InventoryContainer(ent)
    ent.owner = container
    ent.colour = colour
    ent.claims_space = claims_space
    ent.mobile = mobile

    container.add(ent)

    return ent

def move_ent(ent, new_container):
    """Can be used for dropping, pickup and just rearrangement."""
    ent.owner.remove(ent)
    new_container.add(ent)
    ent.owner = new_container


# --------------------------------------------------------
#   entities
# --------------------------------------------------------
ENT_BAG_OF_SAND = 'bag of sand'
ENT_BAG_OF_SAND_C_KEY = 'charges'
def declare_bag_of_sand(context, container):
    e = create_entity(container, '(', ENT_BAG_OF_SAND, ES_STOOL)
    e.d[ENT_BAG_OF_SAND_C_KEY] = random.choice(range(12, 26))
    def inspect_bag(ent):
        return "bag, hefty (sand, %s kilo)"%ent.d[ENT_BAG_OF_SAND_C_KEY]
    e.desc_fn = inspect_bag
    def apply_sandbag(entity, context):
        surface_name = context.player.ent.owner.surface.within[-1].name
        if 'hole' == surface_name:
            context.status.append('No, it would be a waste to bury this.')
            return
        if 'water' == surface_name:
            context.status.append('No, I would lose it in the stream.')
            return
        if 'dirt' != surface_name:
            context.status.append('This sand should fall over dirt')
            return
        declare_sand(context, context.player.ent.owner.surface)
        e.d[ENT_BAG_OF_SAND_C_KEY] -= 1
        # xxx destroy the bag if necessary
    e.apply_fn = apply_sandbag

ENT_CROWBAR = 'crowbar'
def declare_crowbar(context, container):
    e = create_entity(container, ')', ENT_CROWBAR, ES_STOOL)

ENT_DIRT = 'dirt'
ENT_DIRT_Q_KEY = 'quality'
ENT_DIRT_Q_ROUGH = 'rough'
ENT_DIRT_Q_TILLED = 'tilled'
def declare_dirt(context, container):
    e = create_entity(container, '.', ENT_DIRT, ES_STOOL)
    e.d[ENT_DIRT_Q_KEY] = ENT_DIRT_Q_ROUGH
    def desc(ent):
        return '%s %s'%(e.d[ENT_DIRT_Q_KEY], e.name)
    e.desc_fn = desc

ENT_MANGROVE = 'mangrove'
def declare_mangrove(context, container):
    e = create_entity(container, "%", ENT_MANGROVE, ES_WALL, colour='green')
    e.claims_space = True

ENT_SHAMBLER = 'shambler'
def declare_shambler(context, container):
    ent = create_entity(container, 'Y', ENT_SHAMBLER, ES_PLINTH*3, colour="red")
    ent.claims_space = True
    ent.sentient = True
    def sentient_fn(nom, acc):
        if acc.name == ENT_SHAMBLER:
            pass
        if acc.name == ENT_PLAYER:
            context.exit_message = "A shambler crushes you."
            context.keep_running = False
            context.player.ent.c = '&'
    ent.sentient_fn = sentient_fn
    ent.d['dead'] = False
    return ent

ENT_WATER = 'water'
def declare_water(context, container):
    ent = create_entity(container, '~', ENT_WATER, ES_WALL, colour="blue")
    ent.claims_space = True



# --------------------------------------------------------
#   inventory
# --------------------------------------------------------
INVENTORY_SELECTION_KEYS = []
INVENTORY_SELECTION_KEYS.extend( [chr(c) for c in xrange(ord('a'), ord('z')+1)] )
INVENTORY_SELECTION_KEYS.extend( [chr(c) for c in xrange(ord('A'), ord('Z')+1)] )

def inspect_mobile_items_in_container(context, container, heading, use_selection):
    """Looks at a container. If selection is True, then you can select
    something from the container."""
    mobile_items = [tpl[1] for tpl in sorted([(e.desc(), e) for e
                                                            in container.contained()
                                                            if e.mobile
                                                            ])
                    ]

    choice_d = {}
    for idx, ent in enumerate(mobile_items):
        idesc = ent.desc()
        choice_d[INVENTORY_SELECTION_KEYS[idx]] = (idesc, ent)

    selection = None
    status = None

    while selection == None:
        lines = []
        lines.append(heading)
        lines.append('')
        for key in sorted(choice_d.keys()):
            name = choice_d[key][0]
            if use_selection:
                lines.append("  %s) %s"%(key, name))
            else:
                lines.append("  %s"%name)
        if len(choice_d) == 0:
            lines.append('  [Nothing]')
        lines.append('')
        if status:
            lines.append(status)

        context.io.redraw(lines)
        result = context.io.getchar()
        if not use_selection:
            break
        if ord(result) in (KEY_ESC, KEY_SPACE, KEY_ENTER):
            return None
        elif result in choice_d:
            selection = choice_d[result][1]
        else:
            status = "* escape to return"
    return selection


# --------------------------------------------------------
#   actions
# --------------------------------------------------------
KEYPRESS_ACTIONS = {}

def handle_keypress(*keys):
    def decorator(func):
        def wrapper(context):
            func(context)
        for key in keys:
            if key in KEYPRESS_ACTIONS:
                raise Exception("Duplicate keybind definition. %s"%key)
            KEYPRESS_ACTIONS[key] = wrapper
        if func.__doc__:
            wrapper.__doc__ = func.__doc__
        else:
            wrapper.__doc__ = func.__name__
        if wrapper.__doc__.startswith('action_'):
            wrapper.__doc__ = ' '.join(wrapper.__doc__.split('_')[1:])
        return wrapper
    return decorator

@handle_keypress('w', ' ')
def action_wait(context):
    pass

@handle_keypress('q')
def action_quit(context):
    # xxx polish
    context.keep_running = False
    """
    print
    print "Confirm quit [yn]>",
    res = context.io.getchar()
    if res in ['y', 'Y']:
        context.keep_running = False
    """

@handle_keypress('?')
def action_help(context):
    "Help: shows this menu"
    context.io.clear_screen()
    sb = []
    for i in range(COUNT_STATUS_LINES_RESERVED):
        sb.append('')
    sb.append('%sKeys:'%SPACE_BUFFER)
    sb.append('')
    for k, fn in sorted(KEYPRESS_ACTIONS.items()):
        text = fn.__doc__
        sb.append('%s  %s  %s'%(SPACE_BUFFER, k, text))
    sb.append('')
    sb.append('  [paused]')
    print '\n'.join(sb)
    context.io.getchar()

@handle_keypress('i')
def action_inventory(context):
    "Inventory: Show what you're holding"
    # xxx change this so that once you've selected an item, you get a
    # choice of how you'd like to interact with it.
    ent = inspect_mobile_items_in_container( context
                                           , context.player.ent.inv
                                           , 'Inventory:'
                                           , use_selection=False
                                           )
    if None == ent:
        return

    context.status.append("Selected a %s"%ent.desc())

@handle_keypress('1', 'b')
def action_go_sw(context):
    context.player_plane().move(context.player.ent, 1)

@handle_keypress('2', 'j')
def action_go_s(context):
    context.player_plane().move(context.player.ent, 2)

@handle_keypress('3', 'n')
def action_go_se(context):
    context.player_plane().move(context.player.ent, 3)

@handle_keypress('4', 'h')
def action_go_w(context):
    context.player_plane().move(context.player.ent, 4)

@handle_keypress('6', 'l')
def action_go_e(context):
    context.player_plane().move(context.player.ent, 6)

@handle_keypress('7', 'y')
def action_go_e(context):
    context.player_plane().move(context.player.ent, 7)

@handle_keypress('8', 'k')
def action_go_n(context):
    context.player_plane().move(context.player.ent, 8)

@handle_keypress('9', 'u')
def action_go_n(context):
    context.player_plane().move(context.player.ent, 9)


# --------------------------------------------------------
#   fairies
# --------------------------------------------------------
#
# The program runs on fairies. A game 'turn' is comprised
# of all fairies working out what they want to do.
#
class PlayerFairy(object):
    def __init__(self, context, ent):
        self.context = context
        self.ent = ent
        self.health = 0
    def turn(self):
        "Have a turn"
        self.context.io.clear_screen()

        player_plane = self.context.player_plane()
        self.context.io.redraw( player_plane.render()
                              , True
                              )
        self.context.status = []
        key = self.context.io.getchar()
        if key in KEYPRESS_ACTIONS:
            fn = KEYPRESS_ACTIONS[key]
            fn(self.context)
        else:
            self.context.status.append("Unknown command, %s"%key)
        #
        # Tell the player about the surface they're on
        self.context.status.append(str(self.context.turn_counter))

ENT_PLAYER = 'player'
def declare_player_actor(context):
    middle = (ROWSIZE/2, COLSIZE/2)
    starting_space = context.starting_plane.d_space[middle]
    starting_space.within = []
    ent = create_entity( starting_space
                       , '@'
                       , ENT_PLAYER
                       , ES_PLINTH * 2
                       , colour='yellow'
                       , claims_space=True
                       , mobile=False
                       )
    ent.sentient = True
    def sentient_fn(nom, acc):
        if acc.name == ENT_SHAMBLER:
            acc.d['dead'] = True
            status(context, 'Klunk!')
    ent.sentient_fn = sentient_fn

    context.player = PlayerFairy(context, ent)
    context.fairies.append(context.player)

    declare_crowbar(context, context.player.ent.inv)

class LadyOfTheLakeFairy(object):
    "She sends swamp monsters after you."
    def __init__(self, context):
        self.context = context
        # list of entity
        self.monsters = []
    def turn(self):
        #
        # clean up the dead shambers
        dead = [m for m
                  in self.monsters
                  if m.d['dead'] == True
                  ]
        for d in dead:
            d.owner.within.remove(d)
        self.monsters = [m for m
                           in self.monsters
                           if m.d['dead'] == False
                           ]
        #
        # move the shamblers
        player_space = self.context.player.ent.owner
        p_ridx, p_cidx = player_space.ridx, player_space.cidx
        for m in self.monsters:
            m_space = m.owner
            m_ridx, m_cidx = m_space.ridx, m_space.cidx
            cardinal = None
            if m_ridx > p_ridx and m_cidx > p_cidx:
                cardinal = random.choice( [7,7,7,7,4,8] )
            elif m_ridx > p_ridx and m_cidx < p_cidx:
                cardinal = random.choice( [9,9,9,9,8,6] )
            elif m_ridx < p_ridx and m_cidx > p_cidx:
                cardinal = random.choice( [1,1,1,1,2,4] )
            elif m_ridx < p_ridx and m_cidx < p_cidx:
                cardinal = random.choice( [3,3,3,3,2,6] )
            elif m_ridx < p_ridx:
                cardinal = random.choice( [2,2,2,2,1,3] )
            elif m_ridx > p_ridx:
                cardinal = random.choice( [8,8,8,8,9,7] )
            elif m_cidx < p_cidx:
                cardinal = random.choice( [6,6,6,6,9,3] )
            elif m_cidx > p_cidx:
                cardinal = random.choice( [4,4,4,4,1,7] )
            m.owner.plane.move(m, cardinal)

        # randomly create monsters
        val = random.choice(range(4))
        if val == 0:
            empty_water_spots = [ws for ws
                                    in self.context.water_spots
                                    if len(ws.within) == 0
                                    ]
            if empty_water_spots:
                m = random.choice( [ "You hear a rustle."
                                   , "There is a sudden splashing."
                                   , "A shambler rises from the swamp."
                                   , "A new pair of red eyes."
                                   , "The creature shambles towards you."
                                   , "A distant sheep bleets."
                                   , "You hear a cowbell."
                                   ] )
                status(self.context, m)
                starting_space = random.choice(self.context.water_spots)
                ent = declare_shambler(self.context, starting_space)
                self.monsters.append(ent)

def declare_lady_of_the_lake(context):
    context.lady_of_the_lake = LadyOfTheLakeFairy(context)
    context.fairies.append(context.lady_of_the_lake )

def create_initial_fairies(context):
    declare_player_actor(context)
    declare_lady_of_the_lake(context)


# --------------------------------------------------------
#   complex actions
# --------------------------------------------------------
def talk_to_shed_door(context, player_ent, shed_door_ent):
    ent = inspect_mobile_items_in_container( context=context
                                           , container=shed_door_ent.inv
                                           , heading="Contents of the shed:"
                                           , use_selection=False
                                           )
    if context.io.ask_yn("Pack something in the shed?", default=False, clear=False):
        ent = inspect_mobile_items_in_container( context=context
                                               , container=player_ent.inv
                                               , heading="Select item to deposit:"
                                               , use_selection=True
                                               )
        if ent:
            move_ent(ent, shed_door_ent.inv)
            status(context, 'Done')
    if context.io.ask_yn("Retrieve from shed?", default=False, clear=False):
        ent = inspect_mobile_items_in_container( context=context
                                               , container=shed_door_ent.inv
                                               , heading="Select item to get"
                                               , use_selection=True
                                               )
        if ent:
            move_ent(ent, player_ent.inv)
            status(context, 'Taken')


# --------------------------------------------------------
#   alg
# --------------------------------------------------------
def setup_and_populate_the_map(context):
    """Create rooms, and then spaces for walls and
    the enclosed areas of this plane."""
    context.starting_plane = create_plane(context, ROWSIZE, COLSIZE)

    randomish_mangroves_and_stuff(context, context.starting_plane)

    #
    # put land randomly on the map

    #
    # create the island
    declare_island_plane(context)
    merge_plane_onto_plane( context=context
                          , source_plane=context.island_plane
                          , target_plane=context.starting_plane
                          , t_ridx_offset=2
                          , t_cidx_offset=10
                          )

def randomish_mangroves_and_stuff(context, plane):
    #
    # randomly allocate mangroves and land
    for ridx in xrange(plane.rowsize):
        for cidx in xrange(plane.colsize):
            choice = random.choice( [1,2,3,4,5,6,7,8,9] )
            if choice == 1:
                space = plane.d_space[ (ridx, cidx) ]
                space.surface.within.pop() # eliminate water
                declare_dirt(context, space.surface)
            elif choice == 2:
                space = plane.d_space[ (ridx, cidx) ]
                space.surface.within.pop() # eliminate water
                declare_dirt(context, space.surface)
                declare_mangrove(context, space)

def main():
    context = Context()
    context.io = UnixIo(context)

    status(context, "You're lost in the swamp. The water has risen. It's getting dark.")
    status(context, "Fortunately, you brought your crowbar. You can hit nasties by walking into")
    status(context, 'then. Get them before they get you.')
    status(context, "[Turn on numlock, or use vi keys. ? for help]")
    status(context, '')

    setup_and_populate_the_map(context)

    context.water_spots = [ent for ent
                               in context.starting_plane.d_space.values()
                               if ent.surface.within[-1].name == ENT_WATER
                               ]

    create_initial_fairies(context)

    key = None
    while context.keep_running:
        context.turn_counter += 1
        if context.turn_counter > 100:
            context.exit_message = "You survived the night."
            context.keep_running = False
        else:
            for actor in context.fairies:
                actor.turn()

    context.io.clear_screen()
    player_plane = context.player_plane()
    context.io.redraw( player_plane.render()
                     , True
                     )

    if context.exit_message:
        print context.exit_message


# --------------------------------------------------------
#   stencil
# --------------------------------------------------------
def status(context, msg):
    context.status.append(msg)


# --------------------------------------------------------
#   util
# --------------------------------------------------------
class Timer(object):
    def __init__(self, context, turns, fn_action):
        self.context = context
        self.turns = turns
        self.fn_action = fn_action
    def tick(self):
        self.turns -= 1
        if self.turns == 0:
            fn_action()
            context.timers.remove(t)
def create_timer(context, turns, fn_action):
    t = Timer(context, 5, fn_action)
    context.timers.append(t)


# --------------------------------------------------------
#   loader
# --------------------------------------------------------
if __name__ == '__main__':
    main()




