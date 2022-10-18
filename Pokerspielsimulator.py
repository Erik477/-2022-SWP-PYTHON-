#Karten modellieren: 52 Karten-> Array mit 52 Stellen -> zufällige Zahl ziehen 0 bis 52 -> 
# Bei Farbe modulo 4 => 1 bis 4 kommt da raus ->
# Bei Symbolen dividieren durch 13 ->

# 5 karten ziehen und in eine Liste packen und dann überprüfen ob eine der Kombinationen Zutrifft

# Wahrscheinlichkeiten für Kombinationen nach 1000 Versuchen Ausgeben

#https://www.partypoker.com/de-at/how-to-play/hand-rankings

import random

def Kartenziehung(anzZiehungen,anzKarten):
    ziehungen = []
    for x in range(1, anzKarten+1):
        ziehungen.append(x)
    for x in range(0, anzZiehungen):
        index = random.randrange(len(ziehungen) - x)

        last_pos = len(ziehungen) -1 - x    #Herausfinden der letzten noch nicht besetzten stelle
        ziehungen[last_pos],ziehungen[index]=ziehungen[index],ziehungen[last_pos] #Zufallszahl und letzte noch nicht besetzte stelle werden getauscht

    return ziehungen[-anzZiehungen:]
    
def Kombinationen(Karte1,Karte2,Karte3,Karte4,Karte5):
    
    if Karte1[0] == Karte2[0] == Karte3[0] == Karte4[0] == Karte5[0]:   #Flush
        return("Flush")                                                 #Straight Flush
                                                                        #Royal Flush
        
    
    #Vierling
    #Full House
    
    #Straße 
    #Drilling
    #Zwei Paare
    #Paar
    #High Card
    return("Nix")
    
def aufrufen(anzKarten):
    Ziehung = Kartenziehung(5,anzKarten)

    Karte1 = [Ziehung[0]%4,Ziehung[0]//4]
    Karte2 = [Ziehung[1]%4,Ziehung[1]//4]
    Karte3 = [Ziehung[2]%4,Ziehung[2]//4]
    Karte4 = [Ziehung[3]%4,Ziehung[3]//4]
    Karte5 = [Ziehung[4]%4,Ziehung[4]//4]

    erg = Kombinationen(Karte1,Karte2,Karte3,Karte4,Karte5)

    print("Ziehung: " + str(Ziehung))
    print("Karte1:" + str(Karte1))
    print("Karte1:" + str(Karte2))
    print("Karte1:" + str(Karte3))
    print("Karte1:" + str(Karte4))
    print("Karte1:" + str(Karte5))
    print("Ergebnis: " + erg)



if __name__ == '__main__':
    stat = {}

    anzKarten = 52
    aufrufen(anzKarten)


