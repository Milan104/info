def rueckgeld(eingabe):
    print((eingabe -(eingabe % 200))/200,"x 2 Eurostücke werden ausgegben")
    rest1 = eingabe % 200
    print((rest1-(rest1 % 100))/100,"x 1 Eurostücke werden ausgegben")
    rest2 = rest1 % 100
    print((rest2-(rest2 % 50))/50,"x 50ct Stücke werden ausgegben")
    rest3 = rest2 % 50
    print((rest3-(rest3 % 20))/20,"x 20ct Stücke werden ausgegben")
    rest4 = rest3 % 20
    print((rest4-(rest4 % 10))/10,"x 10ct Stücke werden ausgegben")
    rest5 = rest4 % 10
    print((rest5-(rest5 % 5))/5,"x 5ct Stücke werden ausgegben")
    rest6 = rest5 % 5
    print((rest6-(rest6 % 2))/2,"x 2ct Stücke werden ausgegben")
    rest7 = rest6 % 2
    print(rest7,"x 1ct Stücke werden ausgegben")

eingabe = int(input("Geldsumme in ct angeben: "))
rueckgeld(eingabe)

