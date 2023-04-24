# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:27:26 2023

@author: romas
"""

from __future__ import annotations 

import itertools as tools

# import dataclasses as dc

class Solution:
    
    solution = []
    
    next_solutions = []
    
    def __init__(self, arr: list):
        
        self.solution = arr
        
    def __repr__(self):
        
        return f"{self.solution}"
    
    def __eq__(self, other: Solution):
        
        if self.solution == other.solution:
            
            return True
        
        return False
    
    def add_next_solutions(self, n: int, arr: list, arr_sol: list) -> None:
        
        max_ind = self.solution.index(max(self.solution))
        
        temp_sol = [x-1 if x == max(self.solution) else x for x in self.solution]
        
        if sum(temp_sol) == n-1:
        
            count = 0
            
            while count < len(temp_sol):
                
                temp_sol_1 = temp_sol.copy()
                
                if count != max_ind:
                    
                    temp_sol_1[count] += 1
                    
                    new_solution = Solution(temp_sol_1)
    
                    if new_solution not in arr and new_solution not in list(tools.chain.from_iterable(arr_sol)):
                    
                        arr.append(new_solution)
                    
                count += 1