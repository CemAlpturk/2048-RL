from enum import Enum
from typing import Any, Dict, List, Optional

import numpy as np


class Action(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Board:
    
    def __init__(
        self,
        width: int = 4,
        height: int = 4
    ) -> None:
        
        self.width = width 
        self.height = height 
        
        self.end = False
        
        self.initial_value = 2
        
        # Initialize board
        self.board = np.zeros(shape=(width, height), dtype=int)
        
    def _fill_radom_tile(
        self,
        n: int = 1
    ) -> None:
        """
        Add a 2 to n random tiles. If there are no available tiles left end game.

        Args:
            n (int, optional): Number of tiles to fill. Defaults to 1.
        """
        
        # Input checks
        assert isinstance(n, int), f"n must be of type int, {type(n)} was given."
        assert n > 0, f"n must be greater than 0, {n}<=0"
        
        # Indices of empty tiles 
        idx = np.argwhere(self.board == 0)
        n_empty_tiles = idx.shape[0]
        
        if n_empty_tiles < n:
            # Not enough empty times
            self.end = True 
            return 
        
        # Randomly select n tiles without replacement 
        chosen_idx = np.random.choice(n_empty_tiles, n)
        
        for i in chosen_idx:
            self.board[idx[i]] = self.initial_value
        