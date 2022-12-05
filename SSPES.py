import random


def aufrufen(Countplayerwins,Countcompwins):
    print("Welcome to Schere Stein Papier Echse Spock")
    print("Schere = 0, Stein = 1, Papier = 2, Echse = 3, Spock = 4")
    print("")
    comp = str(random.randint(0,4))
    player = str(input())


    print("Computer: " + str(comp))

    if player == comp: print("Unentschieden")
    elif player == "0":
        if comp == "1" or comp == "4": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    elif player == "1":
        if comp == "2" or comp == "4": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    elif player == "2":
        if comp == "0" or comp == "3": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt")   ; Countplayerwins += 1
    elif player == "3":
        if comp == "1" or comp == "0": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    elif player == "4":
        if comp == "2" or comp == "3": print("Computer gewinnt") ; Countcompwins += 1
        else: print("Spieler gewinnt") ; Countplayerwins += 1
    else: print("Falsche Eingabe")

    again = str(input("Nochmal? (y/n)"))

    if again == "y": aufrufen(Countplayerwins,Countcompwins)
    elif again == "n":
        timesplayed = Countplayerwins + Countcompwins
        print("Gespielt: " + str(timesplayed))
        print("Spieler:  " + str(Countplayerwins) + " Percent: " + str((Countplayerwins/timesplayed)*100)+ "%")
        print("Computer: " + str(Countcompwins) + " Percent: " + str((Countcompwins/timesplayed)*100) + "%")
        
        print("Auf Wiedersehen")
    else: print("Falsche Eingabe")


if __name__ == '__main__':
    Countplayerwins = 0
    Countcompwins = 0
    aufrufen(Countplayerwins,Countcompwins)