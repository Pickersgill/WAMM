import sys
import re

def decode(chat):
    expr = r"\d\d/\d\d/\d\d\d\d, \d\d:\d\d - (.*?): (.*)$"
    msgs = []

    for l in chat:
        l = re.sub(r"[\r\n]", "", l)
        m = re.search(expr, l)

        if m:
            msgs.append(m.group(2))

    return msgs



