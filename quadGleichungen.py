import cmath

a = int(input("Wert für a: "))
b = int(input("Wert für b: "))
c = int(input("Wert für c: "))

if a != 0:
    d = b**2-4*a*c
    if d < 0:
        print("Es gibt keine Lösung!")
    if d == 0:
        x1 = (-b+cmath.sqrt(d))/(2*a)
        print("Es gibt eine Lösung",x1)
    if d > 0:
        x1 = (-b+cmath.sqrt(d))/(2*a)
        x2 = (-b-cmath.sqrt(d))/(2*a)
        print("Es gibt 2 Lösungen",x1,x2)
