import random
import json
from flask import Flask, jsonify

def aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp,difficulty):
    
    if difficulty == 3:
        print("Welcome to Schere Stein Papier Echse Spock")
        print("Schwierigkeit: 1 = leicht, 2 = schwer")
        difficulty = str(input())


    print("Schere = 0, Stein = 1, Papier = 2, Echse = 3, Spock = 4")
    print("")
    if difficulty == "1": 
        comp = str(random.randint(0,4))
    elif difficulty == "2":
        comp = str(random.randint(0,4))
        if comp == "0" and symbols_player[4] > symbols_player[2]:
            comp = "4"
        elif comp == "1" and symbols_player[0] > symbols_player[3]:
            comp = "0"
        elif comp == "2" and symbols_player[1] > symbols_player[4]:
            comp = "1"
        elif comp == "3" and symbols_player[2] > symbols_player[1]:
            comp = "2"
        elif comp == "4" and symbols_player[3] > symbols_player[0]:
            comp = "3"
    else: print("Falsche Eingabe bei Schwierigkeit")
    player = str(input())

    symbols_player[int(player)] += 1
    symbols_comp[int(comp)] += 1

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

    if again == "y": aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp,difficulty)
    elif again == "n":
        
        playerstats = {"Schere": symbols_player[0], "Stein": symbols_player[1], "Papier": symbols_player[2], "Echse": symbols_player[3], "Spock": symbols_player[4], "Gewonnen": Countplayerwins}
        compstats = {"Schere": symbols_comp[0], "Stein": symbols_comp[1], "Papier": symbols_comp[2], "Echse": symbols_comp[3], "Spock": symbols_comp[4], "Gewonnen": Countcompwins}

        with open('playerstats.json', 'w') as f:
            json.dump(playerstats, f)
        with open('compstats.json', 'w') as f:
            json.dump(compstats, f)

        print("Auf Wiedersehen")
    else: print("Falsche Eingabe")

def statistics( Countplayerwins, Countcompwins, symbols_player, symbols_comp):
    timesplayed = Countplayerwins + Countcompwins
    print("Gespielt: " + str(timesplayed))
    print("Spieler:  " + str(Countplayerwins) + " Percent: " + str((Countplayerwins/timesplayed)*100)+ "%")
    print("Symbole: " + str(symbols_player))
    print("Computer: " + str(Countcompwins) + " Percent: " + str((Countcompwins/timesplayed)*100) + "%")
    print("Symbole: " + str(symbols_comp))

def uploaddata(Countplayerwins,Countcompwins,symbols_player,symbols_comp):
    playerstats = {"Schere": symbols_player[0], "Stein": symbols_player[1], "Papier": symbols_player[2], "Echse": symbols_player[3], "Spock": symbols_player[4], "Gewonnen": Countplayerwins}
    compstats = {"Schere": symbols_comp[0], "Stein": symbols_comp[1], "Papier": symbols_comp[2], "Echse": symbols_comp[3], "Spock": symbols_comp[4], "Gewonnen": Countcompwins}

    print("Playerstats: " + str(playerstats))
    print("Compstats: " + str(compstats))

    changedata = str(input("Daten ändern? (y/n)"))

    if changedata == "y":
        print("Welche Daten sollen geändert werden?")
        print("1. Spieler")
        print("2. Computer")
        print("3. Beide")
        whatdata = str(input())

        if whatdata == "1" or whatdata == "3":
            print("Wie viele Spiele hat der Spieler gewonnen?")
            Countplayerwins = int(input())
            print("Wie viele Schere hat der Spieler geworfen?")
            symbols_player[0] = int(input())
            print("Wie viele Stein hat der Spieler geworfen?")
            symbols_player[1] = int(input())
            print("Wie viele Papier hat der Spieler geworfen?")
            symbols_player[2] = int(input())
            print("Wie viele Echse hat der Spieler geworfen?")
            symbols_player[3] = int(input())
            print("Wie viele Spock hat der Spieler geworfen?")
            symbols_player[4] = int(input())
            print("Daten geändert")
            if whatdata == "3":
                print("Wie viele Spiele hat der Computer gewonnen?")
                Countcompwins = int(input())
                print("Wie viele Schere hat der Computer geworfen?")
                symbols_comp[0] = int(input())
                print("Wie viele Stein hat der Computer geworfen?")
                symbols_comp[1] = int(input())
                print("Wie viele Papier hat der Computer geworfen?")
                symbols_comp[2] = int(input())
                print("Wie viele Echse hat der Computer geworfen?")
                symbols_comp[3] = int(input())
                print("Wie viele Spock hat der Computer geworfen?")
                symbols_comp[4] = int(input())
                print("Daten geändert")
        elif whatdata == "2":
            print("Wie viele Spiele hat der Computer gewonnen?")
            Countcompwins = int(input())
            print("Wie viele Schere hat der Computer geworfen?")
            symbols_comp[0] = int(input())
            print("Wie viele Stein hat der Computer geworfen?")
            symbols_comp[1] = int(input())
            print("Wie viele Papier hat der Computer geworfen?")
            symbols_comp[2] = int(input())
            print("Wie viele Echse hat der Computer geworfen?")
            symbols_comp[3] = int(input())
            print("Wie viele Spock hat der Computer geworfen?")
            symbols_comp[4] = int(input())
            print("Daten geändert")
        else: print("Falsche Eingabe")

        with open('playerstats.json', 'w') as f:
            json.dump(playerstats, f)
        with open('compstats.json', 'w') as f:
            json.dump(compstats, f)

if __name__ == '__main__':

    with open('playerstats.json', 'r') as f:
        playerstats = json.load(f)

    with open('compstats.json', 'r') as f:
        compstats = json.load(f)

    Countplayerwins = playerstats["Gewonnen"]
    Countcompwins = compstats["Gewonnen"]
    symbols_player = [playerstats["Schere"],playerstats["Stein"],playerstats["Papier"],playerstats["Echse"],playerstats["Spock"]]
    symbols_comp = [compstats["Schere"],compstats["Stein"],compstats["Papier"],compstats["Echse"],compstats["Spock"]]

    app = Flask(__name__)
    @app.route('/statistic')
    def statistic():
        
        return jsonify({"Player: ": playerstats, "Computer: ": compstats})
    
    print("Willkommen bei Schere Stein Papier Echse Spock")
    print("1. Spiel starten")
    print("2. Statistik + API")
    print("3. Daten ändern")
    print("4. Beenden")
    choice = str(input())
    if choice == "1":
        aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp,3)
        statistics( Countplayerwins, Countcompwins, symbols_player, symbols_comp)
    elif choice == "2":
        statistics( Countplayerwins, Countcompwins, symbols_player, symbols_comp)
        app.run()
    elif choice == "3":
        uploaddata(Countplayerwins,Countcompwins,symbols_player,symbols_comp)
    elif choice == "4":
        print("Auf Wiedersehen")
        exit()
    else: print("Falsche Eingabe")