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

class Alien(Cell):
    def __init__(self, row: int, column: int):
        Cell.__init__ (self, row, column)

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
    
    def GetAliens(self)->list:
        return self.GetCellsByType(Alien)
    
    def get_cell(self, row, column) -> Cell:
        result = filter(lambda x: x.row == row and x.column == column, self.cells)
        return list(result)[0]

class CompassDirection(Enum):
    North = 1
    East = 2
    South = 3
    West = 4

class Rover():
    def __init__(self, grid:Grid, row: int, column: int, direction:CompassDirection):
        self.grid = grid
        self.direction = direction
        self.row = row
        self.column = column

        currentCell = self.grid.get_cell(row, column)
        if(currentCell == None):
            raise Exception("Rover start position invalid.") 

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
                return Alien(row, column)

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



