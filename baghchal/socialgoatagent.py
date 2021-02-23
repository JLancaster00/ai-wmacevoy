from typing import List, Tuple, Optional
from agent import Agent
from game import Game
from const import Const
from move import Move
import random

class SocialGoatAgent(Agent):
    def __init__(self,game : Game, side : int):
        super(SocialGoatAgent, self).__init__(game,side)
        if side != Const.MARK_GOAT:
            raise ValueError("side must be goat")

    def isBetweenGoats(self,row : int, col : int):
        game : Game = self.game
        board : List[List[int]] = game.board
        for (dRow,dCol) in Const.DIRS[(row,col)]:
            for (eRow,eCol) in Const.DIRS[(row,col)]:
                if board[row+dRow][col+dCol] == Const.MARK_GOAT and board[row+eRow][col+eCol] == Const.MARK_GOAT:
                    if (dRow == eRow and dCol != eCol) or (dRow != eRow and dCol == eCol):
                        return True
        return False

    def propose(self) -> Move:
        BetweenGoatsMoves : List[Move] = []
        moves = self.game.goatMoves()
        for move in moves:
            if self.isBetweenGoats(move.toRow,move.toCol):
                BetweenGoatsMoves.append(move)
        if len(BetweenGoatsMoves) > 0:
            return random.choice(BetweenGoatsMoves)
        if (len(moves) == 0):
            print(self.game)
        return random.choice(moves)