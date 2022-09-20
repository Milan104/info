def Ausgabe(input):
    print((int(input) // 200),"x 2 Eurostücke werden ausgegben")
    rest = int(input) % 200
    if rest > 0:
        print((int(rest) // 100),"x 1 Eurostücke werden ausgegben")
        rest1 = (int(rest) % 100)
        if rest1 > 0:
            print((int(rest1) // 50),"x 50 Centstücke werden ausgegben")
            rest2 = (int(rest1) % 50)
            if rest2 > 0:
                print((int(rest2) // 20),"x 20 Centstücke werden ausgegben")
                rest3 = (int(rest2) % 20)
                if rest3 > 0:
                     print((int(rest2) // 10),"x 10 Centstücke werden ausgegben")
                     rest4 = (int(rest3) % 10)
                     if rest4 > 0:
                         print((int(rest2) // 5),"x 5 Centstücke werden ausgegben")
                         rest5 = (int(rest4) % 10)
                         if rest5 > 0:
                             print("Der Rest wird einbehalten 2 und 1 Centstücken sollten eh aus dem Verkehr gezogen werden")
                        
                     
                     
input = input("Geldsumme in ct angeben: ")

Ausgabe(input)