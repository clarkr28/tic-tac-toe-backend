from enum import Enum



class PositionState(Enum):
    '''states that a position on a tic tac toe board can have'''
    empty = '0'
    playerA = '1'
    playerB = '2'



class TicTacToeBoard:
    '''A class to represent a tic tac toe board'''

    def __init__(self, rawBoard="000000000"):
        # create and fill the board
        self.board = []
        for i in range(9):
            if i % 3 == 0:
                self.board.append([])
            self.board[-1].append(PositionState(rawBoard[i]))


    def __str__(self):
        '''return the state of the board as a string'''
        boardStr = ''
        for rowIdx in range(3):
            for colIdx in range(3):
                boardStr += self.board[rowIdx][colIdx].value
        return boardStr

    
    def performMove(self, nextMoveType: str):
        '''
        perform the next move on the board
        returns true if the move was successful
        '''
        if nextMoveType != PositionState.playerA.value and \
            nextMoveType != PositionState.playerB.value:
            return False

        for rowIdx in range(3):
            for colIdx in range(3):
                if self.board[rowIdx][colIdx] == PositionState.empty:
                    self.board[rowIdx][colIdx] = PositionState(nextMoveType)
                    return True
        return False