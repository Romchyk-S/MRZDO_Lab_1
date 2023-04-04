# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:13:27 2023

@author: romas
"""

print()

left_part = ""

def get_user_input():
    
    k = 1

    n = 0

    while k > n:
        
        try:

            k = int(input("Введіть кількість x: "))
            
            print()
            
            n = int(input("Введіть праву частину: "))
            
            print()            
            
        except ValueError:
            
            print("Неправильно введено одне з чисел, повторіть дію.")
            
            print()
            
            k, n = get_user_input()
    
    return k, n

k, n = get_user_input()



for i in range(1, k+1):
    
    if i != k:
    
        left_part += f"x_{i} + "
        
    else:
        
        left_part += f"x_{i} = "

equation = left_part + f"{n}"

print("Задане рівняння: ")

print(equation)