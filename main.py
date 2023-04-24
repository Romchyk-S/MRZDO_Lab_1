# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 14:13:27 2023

@author: romas
"""



import itertools as tools

import working_functions as wf

print()


k, n, cond = wf.get_user_input()

equation = wf.form_equation_output(k, n, "x")

print("Задане рівняння: ")

print(equation)

n = wf.form_new_equation(k, n, cond)

solutions_amount = wf.count_solutions_amount(k, n, cond)

print(f"За формулою кількість розв'язків для x>={cond}: {solutions_amount}")


if solutions_amount <= 10**4:

    result, time_taken = wf.find_all_solutions(k, n, cond)
    
    result = list(tools.chain.from_iterable(result))
    
    result = wf.apply_condition(cond, result)
    
    print(f"Знайдено розв'язків алгоритмічно: {len(result)}")
    
    print(f"Час пошуку розв'язків {round(time_taken, 4)} секунд")
    
    print()
    
    print("Розв'язки:")
    
    print(result)
    
else:
    
    print("Кількість розв'язків перевищує бажану кількість.")