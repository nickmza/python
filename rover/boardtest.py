import unittest
import rover

class BoardTest(unittest.TestCase):        
    def test_board_parse(self):
        inputFile = rover.readFile()
        self.assertTrue(len(inputFile) == 10)
    
    def test_parse_board_dimension(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)
        self.assertTrue(grid.width == 20)
        self.assertTrue(grid.height == 10)

    def test_obstacles_loaded(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)
        obstacles = grid.GetObstacles()
        self.assertEquals(len(obstacles),3)

    def test_resources_loaded(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)
        self.assertEquals(len(grid.GetResources()),3)
    
    def test_aliens_loaded(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)
        self.assertEquals(len(grid.GetAliens()),2)

    def getBoard(self):
        inputFile = rover.readFile()
        return rover.parseBoard(inputFile)
    
    def test_get_empty_cell(self):
        grid = self.getBoard()
        cell = grid.get_cell(1,1)
        self.assertEquals(cell, None)
    
    def test_get_cell(self):
        grid = self.getBoard()
        cell = grid.get_cell(3,4)
        self.assertTrue(isinstance(cell, rover.Obstacle))
        self.assertEqual(cell.row, 3)
        self.assertEqual(cell.column, 4)

if __name__ == '__main__':
    unittest.main()