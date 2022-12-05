import random

def Kartenziehung(anzZiehungen,anzKarten):
    ziehungen = []
    for x in range(2, anzKarten+1):
        ziehungen.append(x)
    for x in range(0, anzZiehungen):
        index = random.randrange(len(ziehungen) - x)
        last_pos = len(ziehungen) -1 - x    
        #Herausfinden der letzten noch nicht besetzten stelle
        ziehungen[last_pos],ziehungen[index]=ziehungen[index],ziehungen[last_pos] 
        #Zufallszahl und letzte noch nicht besetzte stelle werden getauscht
    return ziehungen[-anzZiehungen:]
    
def Kombinationen(Karten,aceistheworst):
    kombination = "nix"
    if Flush(Karten):                       #Flush          (Alle gleiche Farbe)
        kombination = "Flush" 
        if StraightFlush(Karten,aceistheworst): #Straight Flush     (aufeinanderfolgend)
            kombination = "Straight Flush" 
            if RoyalFlush(Karten):          #Royal Flush        (endet mit Ass)
                kombination = "Royal Flush" 
    else:
        ident = Gleiche(Karten)             #Gleiche geht die Karten durch und zählt wie viele gleich sind (22 sind 2 Paare)
        if ident == 2:                      #Paar
            kombination = "Paar"
        elif ident == 3:                    #Drilling
            kombination = "Drilling"
        elif ident == 6:                    #Vierling
            kombination = "Vierling"
        elif ident == 4:                   #Zwei Paar
            kombination = "2 Paare"
        elif ident == 5:                   #Full House     (ein Paar ein Drilling)
            kombination = "Full House"
        if StraightFlush(Karten,aceistheworst) and Gleiche(Karten) < 2: #Straße         
            kombination = "Straße" 

    return(kombination)

def Flush(Karten):
    Herz = 0
    Karo = 0
    Pik = 0
    Kreuz = 0
    nr = 0

    for x in range(len(Karten)):
        nr = Karten[x][0]
        if nr == 0:
            Herz += 1
        elif nr == 1:
            Karo += 1
        elif nr == 2:
            Pik += 1
        elif nr == 3:
            Kreuz += 1

    if Herz >= 5 or Karo >= 5 or Pik >= 5 or Kreuz >= 5:
        return True
    else:
        return False

def StraightFlush(Karten,aceistheworst):
    Numbers = []
    for x in range(len(Karten)):
        #if aceistheworst == False:
            #if Karten[x][1] == 1:
                #Karten[x][1] = 14
        Numbers.append(Karten[x][1])
    Numbers.sort()
    if len(Numbers) == 5:
        if (Numbers[len(Numbers)-1] - Numbers[0]) == (len(Numbers) - 1):
            return True
        else:
            return False
    elif len(Numbers) > 5:
        count = 0
        oldvar = 15

        for x in range(len(Numbers)):
            if Numbers[x] == oldvar + 1:
                count += 1
                oldvar = Numbers[x]
            else:
                count = 0
                oldvar = Numbers[x]
            if count == 5:
                Karten.append([x,0])
                return True

        return False 
    return False     
    
def RoyalFlush(Karten):

    if Karten[Karten[len(Karten)-1][0]][1] == 14:
        return True
    else:
        return False

def Gleiche(Karten):
    result = 0
    counting = [0] * 15

    for x in range(len(Karten)):
        counting[Karten[x][1]] += 1
       
    if counting.count(2) > 0:
        result = 2
        if counting.count(2) == 2:
            result = 22                  
    elif counting.count(3) > 0:
        result = 3
    elif counting.count(4) > 0:
        result = 4
   
   
    return result

def Farbe(nr):

    if nr == 0:
        Color = "Herz"
    elif nr == 1:
        Color = "Karo"
    elif nr == 2:
        Color = "Pik"
    elif nr == 3:
        Color = "Kreuz"
    else:
        Color = "Falsche Eingabe"

    return Color   

def Zahl(nr):

    if nr == 1:
        if aceistheworst:
            number = "Ass"
    elif nr <= 10 and nr > 1:
        number = str(nr)
    elif nr == 11:
        number = "Bua"
    elif nr == 12:
        number = "Dame"
    elif nr == 13:
        number = "König"
    elif nr == 14:
        if aceistheworst == False:
            number = "Ass"
    else:
        number = "Falsche Eingabe"
        print("Falsche eingabe: " + str(number))

    return number   

def Aufrufen(anzZiehungen,aceistheworst,anzKartenimdeck):
    Ziehung = Kartenziehung(anzZiehungen,anzKartenimdeck)
    Karten = []
    Karte = []

    for x in range(len(Ziehung)):
        Karte.append(Ziehung[x]%4)
        Karte.append(Ziehung[x]//4)
        Karten.append(Karte)
        Karte = []
    
    erg = Kombinationen(Karten,aceistheworst)

    return erg

def Statistik(wieoft,anzKarten,aceistheworst,anzKartenimdeck):

    ErgList = []
    for x in range(0, 14):
        ErgList.append(0)

    for wieoft in range(0, wieoft):
        
        ErgList[0] += 1
        Ergebnis = Aufrufen(anzKarten,aceistheworst,anzKartenimdeck)
        if Ergebnis == "nix":ErgList[1] += 1
        elif Ergebnis == "Flush": ErgList[2] += 1
        elif Ergebnis == "Straight Flush": ErgList[3] += 1
        elif Ergebnis == "Royal Flush": ErgList[4] += 1
        elif Ergebnis == "Paar": ErgList[5] += 1
        elif Ergebnis == "Drilling": ErgList[6] += 1
        elif Ergebnis == "Vierling": ErgList[7] += 1
        elif Ergebnis == "2 Paare": ErgList[8] += 1
        #elif Ergebnis == "mehr als 2 Paare": ErgList[9] += 1
        elif Ergebnis == "Full House":ErgList[10] += 1
        #elif Ergebnis == "vierling und ein zwilling": ErgList[11] += 1
        elif Ergebnis == "Straße": ErgList[13] += 1            

    print("------------------------------------------------------")
    print("Anzahl gezogener Karten: " + str(anzKarten))
    print("Ist Ass die schlechteste Karte? " + str(aceistheworst))
    print("Anzahl der Karten im deck: " + str(anzKartenimdeck))
    print()
    print("Wahrscheinlichkeiten:")
    print()

    for x in range(1,len(ErgList)):
        percent = (ErgList[x]/ErgList[0])*100

        if x == 1: print("Nix: " + str(percent) + "%")
        elif x == 5: print("Paar: " + str(percent) + "%")
        elif x == 8: print("2 Paare: " + str(percent) + "%")
        elif x == 6: print("Drilling: " + str(percent) + "%")
        elif x == 13: print("Straße: " + str(percent) + "%")
        elif x == 2: print("Flush: " + str(percent) + "%")
        elif x == 10: print("Full House: " + str(percent) + "%")
        elif x == 7: print("Vierling: " + str(percent) + "%")
        elif x == 3: print("Straight Flush: " + str(percent) + "%")
        elif x == 4: print("Royal Flush: " + str(percent) + "%")        
        elif x == 9: print("mehr als 2 Paare: " + str(percent) + "%")
        elif x == 11: print("Vierling und ein Zwilling: " + str(percent) + "%") 

if __name__ == '__main__':

    aceistheworst  = False
    anzKarten = 5
    wieoft = 100000
    
    anzKartenimdeck = 52
    Statistik(wieoft,anzKarten,aceistheworst,anzKartenimdeck)