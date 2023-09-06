import unittest
import rover

class TestRover(unittest.TestCase):        
    def test_board_parse(self):
        inputFile = rover.readFile()
        self.assertTrue(len(inputFile) == 10)
    
    def test_parse_board_dimension(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)
        self.assertTrue(grid.width == 20)
        self.assertTrue(grid.height == 10)



if __name__ == '__main__':
    unittest.main()