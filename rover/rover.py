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
        self.cells = []

    def GetCellsByType(self, cellType: type):
        result = filter(lambda x: isinstance(x, cellType), self.cells)
        return list(result)

    def GetObstacles(self)->list:
        return self.GetCellsByType(Obstacle)

    def GetResources(self)->list:
        return self.GetCellsByType(Resource)

class Cell():
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

class Obstacle(Cell):
    def __init__(self, row: int, column: int):
        Cell.__init__ (self, row, column)

class Resource(Cell):
    def __init__(self, row: int, column: int):
        Cell.__init__ (self, row, column)

class CellFactory():
    def createCell(self, symbol, row: int, column: int) -> Cell:
        match symbol:
            case ".":
                return None
            case "*":
                return Resource(row, column)
            case "X":
                return Obstacle(row, column)
            case "?":
                return None

def parseBoard(input: list) -> Grid:
    grid = Grid(len(input[0]), len(input))

    row = 1
    col = 1

    factory = CellFactory()
    for line in input:
        for symbol in line:
            cell = factory.createCell(symbol,row, col)
            if(cell != None):
                grid.cells.append(cell)
            col+=1
        col = 1
        row += 1

    return grid



