import sys 
from enum import Enum
from itertools import groupby


def readFile():
    input = sys.argv[1]
    with open(input,"r") as file:
        board = [list(line.strip()) for line in file]
    return board

def runner():   
    #board = readFile()
    pass
    
if __name__ == runner() :
    runner()    



