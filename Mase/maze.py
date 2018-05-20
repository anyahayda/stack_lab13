# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from lliststack import Stack


class Maze:
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = " *"
    PATH_TOKEN = " x"
    TRIED_TOKEN = " o"

    # Creates a maze object with all cells marked as open.
    def __init__(self, num_rows, num_cols):
        self._mazeCells = Array2D(num_rows, num_cols)
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def num_rows(self):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols(self):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall(self, row, col):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart(self, row, col):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition(row, col)

    # Sets the exit cell position.
    def setExit(self, row, col):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition(row, col)

    def findPath(self):
        path_stack = Stack()
        new = self._startCell
        path_stack.push(new)

        while len(path_stack) != 0:
            new.row = path_stack.peek().row
            new.col = path_stack.peek().col
            self._markPath(new.row, new.col)
            flag_valid = False
            for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if self._validMove(path_stack.peek().row + i, path_stack.peek().col + j):
                    new.row = new.row + i
                    new.col = new.col + j
                    path_stack.push(_CellPosition(new.row, new.col))
                    self._markPath(new.row, new.col)
                    flag_valid = True
                    break
            if flag_valid:
                if self._exitFound(new.row, new.col):
                    self._markPath(new.row, new.col)
                    return True
                continue
            cell = path_stack.pop()
            self._markTried(cell.row, cell.col)
        return False

    # Resets the maze by removing all "path" and "tried" tokens
    def reset(self):
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                cur_cell = self._mazeCells[row, col]
                if cur_cell == (self.TRIED_TOKEN or self.PATH_TOKEN):
                    self._mazeCells[row, col] = None

    # Prints a text-based representation of the maze.
    def draw(self):
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._mazeCells[row, col] is None:
                    self._mazeCells[row, col] = '  '
                print(self._mazeCells[row, col], end='')
            print('')

    # Returns True if the given cell position is a valid move.
    def _validMove(self, row, col):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound(self, row, col):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried(self, row, col):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath(self, row, col):
        self._mazeCells[row, col] = self.PATH_TOKEN


# Private storage class for holding a cell position.
class _CellPosition(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
