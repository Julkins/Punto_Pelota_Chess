from const import *
from square import Square
from piece import *

class Board:

    def __init__(self):
        self.sqares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()

    def _create(self):

        for row in range(ROWS):
            for col in range(COLS):
                self.sqares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else row_pawn, row_other = (1, 0)

        #pawns
        for col in [COLS]:
            self.sqares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        #knights
        for col in [COLS]:
            self.sqares[row_other][1] = Square(row_other, 1, Knight(color))
            self.sqares[row_other][6] = Square(row_other, 6, Knight(color))

        #bishops
        for col in [COLS]:
            self.sqares[row_other][2] = Square(row_other, 2, Bishop(color))
            self.sqares[row_other][5] = Square(row_other, 5, Bishop(color))

        #rooks
        for col in [COLS]:
            self.sqares[row_other][0] = Square(row_other, 0, Rook(color))
            self.sqares[row_other][7] = Square(row_other, 7, Rook(color))

        #queen
        for col in [COLS]:
            self.sqares[row_other][3] = Square(row_other, 3, Queen(color))

        #king
        for col in [COLS]:
            self.sqares[row_other][4] = Square(row_other, 4, King(color))




