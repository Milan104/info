import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def getBMI(height, weight):
    BMI = weight / (height/100)**2
    return (int(BMI))
def idealGewicht(gender, height):
    if gender == "Mann":
        idealGewicht = ((height-100)*0.95)
        return (idealGewicht)
    if gender == "Frau":
        idealGewicht = ((height-100)*0.9)
        return (idealGewicht)
def getOptimalIndex(age):
    if age <= 19 and age <= 24:
        optimalBMI = "19-24"
    elif age <= 25 and age <= 34:
        optimalBMI = "20-25"
    elif age <= 35 and age <= 44:
        optimalBMI = "21-26"
    elif age <= 45 and age <= 54:
        optimalBMI = "22-27"
    elif age <= 55 and age <= 64:
        optimalBMI = "23-28"
    elif age <= 65:
        optimalBMI = "24-29"
    else:
        optimalBMI = "Keine Daten für dieses Alter vorhanden."
    return(optimalBMI)
def printBefund():
    werte = ["Berechneter BMI: ",str(getBMI(height, weight)),"Optimaler BMI: ",str(getOptimalIndex(age)),"Optimal Gewicht: ",str(idealGewicht(gender, height))]
    with open('befund.txt', 'w') as f:
        for werte in werte:
         f.write(werte)
         f.write('\n')
def datenAuswertung():
    cls()
    print ("Jetziger BMI: ",getBMI(height, weight))
    print ("Optimaler BMI: ",getOptimalIndex(age))
    print ("Optimal Gewicht: ",idealGewicht(gender, height))
    befundAns = input("Befund als .txt (ja/nein): ")
    if befundAns == "ja":
        printBefund()
    elif befundAns == "nein":
        exit()
    else:
        print("Falscher Input!")




print("BMI Rechner")
print("Bitte Werte eingeben.")
weight = int(input("Dein Gewicht in KG: "))
gender = input("Dein Geschlecht (Mann/Frau): ")
age = int(input("Dein Alter: "))
height = int(input("Deine Größe in CM: "))

datenAuswertung()