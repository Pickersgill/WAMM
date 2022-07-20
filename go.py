import markov
import sys
import pandas as pd
import argparse
from decode import decode

parser = argparse.ArgumentParser(description="A tool for fitting Markov Models to WhatsApp\
        group chat history.")

parser.add_argument("-d", "--data", type=str,
        help="The chat data (.txt) file")
parser.add_argument("-l", "--limit", type=int,
    help="Limits the number of messages used during fitting, 10,000 by default")
parser.add_argument("-m", "--memory", type=int,
    help="Sets the memory length of the model, 1 by default. Setting this any higher will\
            significantly increase the mememory usage")

args = parser.parse_args()

if args.data is None:
    print("No history data provided, use -d to give file.")
    print("See -h for further help")
    quit(1)

limit = 10000 if args.limit is None else args.limit
mem = 1 if args.memory is None else args.mem

data = decode(open(args.data))

model = markov.SimpleMM(data[:limit], mem)

inp = input("Press any key to generate messages. Enter 'q' to quit...")

while inp.lower() != "q":
    new = model.generate()
    print(new)
    inp = input()


