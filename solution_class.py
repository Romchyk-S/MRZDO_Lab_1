# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:27:26 2023

@author: romas
"""

from __future__ import annotations 

import dataclasses as dc

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
    
    def add_next_solutions(self, n: int, arr: list) -> None:
        
        temp_sol = [x-1 if x == max(self.solution) else x for x in self.solution]
        
        if sum(temp_sol) == n-1:
        
            count = 0
            
            while count < len(temp_sol):
                
                temp_sol_1 = temp_sol.copy()
                
                if temp_sol_1[count] != max(temp_sol_1):
                    
                    temp_sol_1[count] += 1
                    
                    new_sol = Solution(temp_sol_1)
                    
                    if new_sol not in arr:
                    
                        arr.append(new_sol)
                    
                count += 1