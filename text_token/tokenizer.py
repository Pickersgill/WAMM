import re
import pandas as pd

def tokenize(card):
    name = card["name"]
    shortname = name.split(",")[0]
    text = card["text"]
    retext = re.sub(r"[\(.*?\)]", "", text)
    retext = "{START}" + re.sub("%s|%s" % (name, shortname), "{THIS}", retext) + "{END}"

    matches = re.findall(r"([0-9a-zA-Z'-+]+)|(\{[^}]+\})|([,:./])", retext)
    tokens = []
    for m in matches:
        tokens.append("".join(list(m)))
    
    return tokens
    
def tokenize_string(obj):
    tokens = ["{START}"] + obj.split(" ") + ["{END}"]
    return tokens
    

