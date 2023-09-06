import sys 
from enum import Enum
from itertools import groupby

def runner():   
    #board = readFile()
    pass
    
if __name__ == runner() :
    runner()    

def readFile():
    input = "./rover/roverMap.txt" #sys.argv[1]
    with open(input,"r") as file:
        board = [list(line.strip()) for line in file]
    return board


class Grid():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

def parseBoard(input: list) -> Grid:
    grid = Grid(len(input[0]), len(input))
    return grid



