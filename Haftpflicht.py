from dateutil import parser
import math

def monate_zwischen(datum1, datum2):
    diff = parser.parse(datum2) - parser.parse(datum1)
    monate_vergangen = math.ceil(((diff.days)/30)) #umrechnen der vergangenen Tage in Monate und aufrunden dieser, zur vollständigen Einbeziehung des Kaufmonats
    return monate_vergangen

def rueckerstatt(monate_vergangen,n_wert):
    if monate_vergangen < 0:
        print("Bitte Eingabe überprüfen!")
    else:
        prozentVerlust = (monate_vergangen*(7.7/12))
        return(n_wert-(prozentVerlust * n_wert) / 100.0)



n_wert = int(input("Neuwert eingeben: "))
k_date = input("Kaufdatum angeben (Format: YYYY-MM): ")
anspruch_datum = input("Datum der Inanspruchname angeben (Format: YYYY-MM):")

print(monate_zwischen(k_date,anspruch_datum))
print(rueckerstatt(monate_zwischen(k_date,anspruch_datum),n_wert))
