import cmath

def get_sol(a,b,c):
    if a != 0:
        d = b**2-4*a*c
        if d < 0:
            return("Es gibt keine Lösung!")
        if d == 0:
            x1 = (-b+cmath.sqrt(d))/(2*a)
            return("Es gibt eine Lösung",x1)
        if d > 0:
            x1 = (-b+cmath.sqrt(d))/(2*a)
            x2 = (-b-cmath.sqrt(d))/(2*a)
            return("Es gibt 2 Lösungen",x1,x2)
    elif a == 0 and b ==0:
        return("Unendlich viele oder keine Lösung")
    elif a == 0:
        x1 = (-c/b)
        return("Es gibt eine Lösung",x1)   


print("Nutze die Formel: ax² + bx  + c = 0")
a = int(input("Wert für a: "))
b = int(input("Wert für b: "))
c = int(input("Wert für c: "))

print(get_sol(a,b,c))