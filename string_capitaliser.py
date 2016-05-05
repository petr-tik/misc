#! usr/bin/env/python

sent = raw_input("")
final = ""
for idx, char in enumerate(sent):
    if idx == 0:
        final += (char.upper())
    elif sent[idx - 1] == " ":
        final += (char.upper())
    else:
        final += (char)


print final
