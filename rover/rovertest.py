import unittest
import rover

class RoverTest(unittest.TestCase):

    def test_init_rover_fail_if_invalid(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)

        try:
            r = rover.Rover(grid,99,99, rover.CompassDirection.North)
            self.assertTrue(False)
        except:
            pass
    