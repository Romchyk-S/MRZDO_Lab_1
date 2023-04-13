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
    
    def add_next_solutions(self, num: int) -> list:
        
        arr = []
        
        temp_sol = [x-1 if x == max(self.solution) else x for x in self.solution]
        
        count = 0
        
        while count < len(temp_sol)-1:
            
            temp_sol_1 = temp_sol.copy()
        
            i = 0
            
            while i < len(temp_sol_1):
                
                if temp_sol_1[i] != max(temp_sol_1) and i > count:
                    
                    temp_sol_1[i] += 1
                    
                    break
                
                elif temp_sol_1[i] != max(temp_sol_1) and i == 0 and len(arr) != 0:
                    
                    temp_sol_1[i] += 1
                    
                    break
                    
                i += 1
            
            arr.append(Solution(temp_sol_1))
                
            count += 1
            
        return arr