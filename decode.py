import sys
import re

MEDIA = "<Media omitted>"

def decode(chat):
    expr = r"\d\d/\d\d/\d\d\d\d, \d\d:\d\d - (.*?): (.*)$"
    msgs = []

    for l in chat:
        l = re.sub(r"[\r\n]", "", l)
        m = re.search(expr, l)

        if m and m.group(2) != MEDIA:
            msgs.append(m.group(2))

    return msgs



