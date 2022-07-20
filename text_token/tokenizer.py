import re
import pandas as pd

def tokenize_string(text):
    tokens = ["{START}"] + text.split(" ") + ["{END}"]
    return tokens
    

