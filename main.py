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

wf.count_solutions_amount(k, n, cond)

result = wf.find_all_solutions(k, n, cond)

result = list(tools.chain.from_iterable(result))

result = wf.apply_condition(cond, result)

print(f"Знайдено розв'язків: {len(result)}")

print()

print(result)