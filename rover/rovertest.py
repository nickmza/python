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
    
    def test_command_parsing(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)    
        r = rover.Rover(grid,1,1, rover.CompassDirection.South)
        commands = "FFFLFF"
        r.load_commands(commands)
        commandBuffer = r.commands
        self.assertEquals(len(commandBuffer), 6)
        self.assertEquals(commandBuffer[5], rover.Commands.Forward)

    
    def test_move_rover(self):
        inputFile = rover.readFile()
        grid = rover.parseBoard(inputFile)    
        r = rover.Rover(grid,1,1, rover.CompassDirection.South)
        commands = "FFFLFF"
        r.load_commands(commands)
        r.execute_commands()

        self.assertEquals(r.row, 4)
        self.assertEquals(r.column, 3)