#inspiriert durch https://www.reddit.com/r/de/comments/mkt3a8/w%C3%BCrfeln_mit_armin_erstelle_deinen_eigenen/

from random import randint as würfel
from satzbausteine import *

#germanisierung der 'print'-Funktion
def drucken(faden):
    print(faden)

#germanisierung der 'len'-Funktion
def länge(liste):
    return len(liste)

#faule germanisierung der 'append'-Funktion
def anhängen(liste, anhängsel):
    return liste.append(anhängsel)     

#würfelt für den Benutzer und gibt diese für weitere Nutzung deformiert aus
def würfeln():
    würfel_ergebnis = []
    while länge(würfel_ergebnis) != 9:
        anhängen(würfel_ergebnis, würfel(1, 6))
    return würfel_deformisator(würfel_ergebnis)

#hier erfolgt die deformisierung der würfel ergebnisse
def würfel_deformisator(würfel_ergebnis):
    pass    

#kreirt einen Pandemieplan nach dem Laschet-Prinzip 
def pandemieplan_generator(würfel_ergebnis):
    Satzbausteine_index = 0
    pandemieplan = [Satzbausteine[Satzbausteine_index][0]]
    Satzbausteine_index +=1

    for augenzahl in würfel_ergebnis:
        if Satzbausteine_index != 6 and Satzbausteine_index != 6 and Satzbausteine_index != 6:
            anhängen(pandemieplan, Satzbausteine[Satzbausteine_index][augenzahl])
        Satzbausteine_index +=1

        if Satzbausteine_index == 6:
            anhängen(pandemieplan, Satzbausteine[6][0])
        if Satzbausteine_index == 7:
            anhängen(pandemieplan, Satzbausteine[8][0])
        if Satzbausteine_index == 9:
            anhängen(pandemieplan, Satzbausteine[11][0])    
    return pandemieplan    

#Hauptfunktion wenn direkt ausgeführt
if __name__ == '__main__':
    drucken(f'Dein eigener Pandemieplan nach dem Laschet-Prinzip;\njetzt voll digital!')
    print(pandemieplan_generator(würfeln()))
