# what is a binary tree

# class for a node in a binary tree

class Node(object):
    def __init__(self, value, left_c=None, right_c=None):
        self.value = value
        self.left_child = left_c
        self.right_child = right_C
        # NEEDS a value as well as record of left and right children. Doesn't have to have all children

# binary search tree NOT binary tree


node = Node(5, 3, 4)
def tree_swapper(node):
    """Recursive function that takes start node of a binary tree as input, returns the tree with all children swapped"""
            # input 
    #          5
    #      3      10
    #    1   4  8   15

        # output
    #         5
    #     10      3
    #   15   8  4   1

    # key insight 
    # 15 was the right child of a right child and is now mirror opposite
    # you need to swap on your level first, then go down to children, if there are any
    temp = Node.left_child
    Node.left_child = Node.right_child
    Node.right_child = temp
    # no need to define the base case - no children, stop generating
    if Node.left_child not None: 
        tree_swapper(Node.left_child)
    if Node.right_child not None:
        tree_swapper(Node.right_child)



############## BINARY SEARCH TREE ########
## Binary search tree
# binary search O(log N)
# binary search tree - tree structure where: 
# left child of X is less than X 
# right child of X is greater than X

#           5
#       3            10
#    1     4      8      15

# Given a BST and lower/upper bounds return another tree with numbers only inside those bounds
#         5
#     4      10
#           8
# 8, 9
#       8