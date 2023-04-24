import math as m

import time as tm

import solution_class as sc

def get_user_input() -> tuple[int]:
    
    k = 1

    n = 0

    while k > n:
        
        try:

            k = int(input("Введіть кількість x: "))
            
            n = int(input("Введіть праву частину: "))
            
            cond = int(input("Введіть обмеження x: "))
            
            print()            
            
        except ValueError:
            
            print("Неправильно введено одне з чисел, повторіть дію.")
            
            print()
            
            k, n, cond = get_user_input()
    
    return k, n, cond

        
def form_new_equation(k: int, n: int, cond: int) -> int:

    if cond > 0:
        
        n -= k*cond
            
        equation = form_equation_output(k, n, "y")
            
        print("Перехід до рівняння з y: ")
    
        print(equation)
                      
    print()
    
    return n

def form_equation_output(k: int, n: int, var: str) -> str:
    
        left_part = ""
        
        for i in range(1, k+1):
            
            if i != k:
            
                left_part += f"{var}_{i} + "
                
            else:
                
                left_part += f"{var}_{i} = "
    
        equation = left_part + f"{n}"
        
        return equation

def count_solutions_amount(k: int, n: int, cond: int) -> int:
    
    try:
        
        solutions_amount = int(m.factorial(n+k-1) / (m.factorial(n) * (m.factorial(k-1))))

        return solutions_amount

    except ValueError:
        
        print("У факторіалі від'ємне число, задане обмеження виключає можливість наявности розв'язків.")

        return 0

def find_all_solutions(k: int, n: int, cond: int) -> tuple[list, float]:
    
    solutions = []
    
    i = n
    
    start = tm.perf_counter()
    
    while i >= m.floor(n/k)-cond:

        arr = []
        
        if i == n:
            
            j = 0
            
            while j < k:
                
                new_solution = sc.Solution([0 if x != j else i for x in range(k)])
                
                if new_solution not in arr:
                
                    arr.append(new_solution)
                
                j += 1
        
        else:
            
            for sol in solutions[n-i-1]:
                
                sol.add_next_solutions(n, arr, solutions)
                
        solutions.append(arr)
            
        i -= 1
        
    time_taken = tm.perf_counter()-start
        
    return solutions, time_taken

def apply_condition(cond: int, result: list) -> list:
    
    if cond != 0:
        
        for res in result:
            
            i = 0
            
            while i < len(res.solution):
                
                res.solution[i] += cond
                
                i += 1 
                
    return result