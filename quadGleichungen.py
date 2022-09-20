import cmath
import numpy as np
import matplotlib.pyplot as plt

def get_solution(a,b,c):
    if a != 0:
        d = b**2-4*a*c
        if d < 0:
            quadr_system(a,b,c)
            return"Es gibt keine Lösung!"
        if d == 0:
            x1 = (-b+cmath.sqrt(d))/(2*a)
            quadr_system(a,b,c)
            return"Es gibt eine Lösung: ",x1
        if d > 0:
            x1 = (-b+cmath.sqrt(d))/(2*a)
            x2 = (-b-cmath.sqrt(d))/(2*a)
            quadr_system(a,b,c)
            return"Es gibt 2 Lösungen: ",x1,x2
    elif a == 0 and b ==0:
        return"Unendlich viele oder keine Lösung"
    elif a == 0:
        x1 = (-c/b)
        lineare_system(b,c)
        return"Es gibt eine Lösung: ",x1  

def lineare_system(a, b):
    x = list(range(-5, 5))
    y = [ (a*i + b) for i in x]
    plt.plot(x, y)

def quadr_system(a,b,c):
    x = list(range(-5, 5))
    y = [ (a*i**2 + b*i + c) for i in x]
    plt.plot(x, y)

print("Nutze die Formel: ax² + bx  + c = 0")
a = int(input("Wert für a: "))
b = int(input("Wert für b: "))
c = int(input("Wert für c: "))

print(get_solution(a,b,c))
plt.grid()
plt.show()