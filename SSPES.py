import random
import json
import mysql.connector

def aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp,difficulty,username):
    
    if difficulty == 3:
        print("Welcome to Schere Stein Papier Echse Spock")
        if username == "defaultuser":
            username = str(input("Username: "))
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

    if int(player) <= 4:
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

    if again == "y": aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp,difficulty,username)
    elif again == "n":

        safeDatatoMysql(Countcompwins,symbols_comp,"Computer")
        safeDatatoMysql(Countplayerwins,symbols_player,username)

        print("Auf Wiedersehen")
    else: print("Falsche Eingabe")

def statistics( Countplayerwins,  symbols_player):
    print()
    print("Wins:  " + str(Countplayerwins))
    print("Schere:  " + str(symbols_player[0]))
    print("Stein:  " + str(symbols_player[1]))
    print("Papier:  " + str(symbols_player[2]))
    print("Echse:  " + str(symbols_player[3]))
    print("Spock:  " + str(symbols_player[4]))
    print("WinRate:  " + str(Countplayerwins/(symbols_player[0]+symbols_player[1]+symbols_player[2]+symbols_player[3]+symbols_player[4])*100) + "%")
    print()

def safeDatatoMysql(Wins,symbols,username):

    username = username.lower()

    with mysql.connector.connect(host="localhost",user="root", password="admin"
    ) as mydb:

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS SWPRubner")

        mycursor.execute("USE SWPRubner")

        mycursor.execute("CREATE TABLE IF NOT EXISTS playerstats (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), wins INT, Schere INT, Stein INT, Papier INT, Echse INT, Spock INT)")

        mycursor.execute("SELECT * FROM playerstats WHERE username = %s", (username,))
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            mycursor.execute("Insert into playerstats (username, wins, Schere, Stein, Papier, Echse, Spock) values (%s, %s, %s, %s, %s, %s, %s)", (username, Wins, symbols[0], symbols[1], symbols[2], symbols[3], symbols[4]))
            mydb.commit()
        else:
            mycursor.execute("UPDATE playerstats SET wins = %s, Schere = %s, Stein = %s, Papier = %s, Echse = %s, Spock = %s WHERE username = %s", (Wins, symbols[0], symbols[1], symbols[2], symbols[3], symbols[4], username))
            mydb.commit()
    
def getDatafromMysqltoJson():

     with mysql.connector.connect(host="localhost",user="root", password="admin"
    ) as mydb:
    
            cur = mydb.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS SWPRubner")

            cur.execute("USE SWPRubner")

            cur.execute("CREATE TABLE IF NOT EXISTS playerstats (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), wins INT, Schere INT, Stein INT, Papier INT, Echse INT, Spock INT)")
            cur.execute('SELECT * FROM playerstats')
            row_headers=[x[0] for x in cur.description] #this will extract row headers
            rv = cur.fetchall()
            json_data=[]
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))

            with open('playerstats.json', 'w') as f:
                json.dump(json_data, f)

def getDatafromMysql(username):

    username = username.lower()

    with mysql.connector.connect(host="localhost",user="root", password="admin"
    ) as mydb:

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS SWPRubner")

        mycursor.execute("USE SWPRubner")

        mycursor.execute("CREATE TABLE IF NOT EXISTS playerstats (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), wins INT, Schere INT, Stein INT, Papier INT, Echse INT, Spock INT)")

        mycursor.execute("SELECT * FROM playerstats WHERE username = %s", (username,))
        myresult = mycursor.fetchall()

        if len(myresult) == 0:
            return "NoUser"
        else:
            myresult = str(myresult)
            myresult = myresult.replace("(","")
            myresult = myresult.replace(")","")	
            myresult = myresult.replace("[","")
            myresult = myresult.replace("]","")
            myresult = myresult.split(",")
            return myresult

if __name__ == '__main__':


    compstats = getDatafromMysql("Computer")
    if compstats == "NoUser":
        safeDatatoMysql(0,[0,0,0,0,0],"Computer")
        compstats = getDatafromMysql("Computer")
    playing = True


    Countplayerwins = 0
    Countcompwins = int(compstats[2])

    symbols_player = [0,0,0,0,0]
    symbols_comp = [int(compstats[3]),int(compstats[4]),int(compstats[5]),int(compstats[6]),int(compstats[7])]

    print("Willkommen bei Schere Stein Papier Echse Spock")
    
    while playing:
        
        print("1. Spiel starten")
        print("2. Statistik")
        print("3. Upload Statistik")
        print("4. Beenden")
        choice = str(input())
        if choice == "1":
            username = str(input("Username: "))
            userstats = getDatafromMysql(username)
            if userstats == "NoUser":
                print("User nicht gefunden")
                if input("Möchten Sie einen neuen User erstellen? (y/n)") == "y":
                    safeDatatoMysql(0,[0,0,0,0,0],username)
                    aufrufen(0,Countcompwins,[0,0,0,0,0],symbols_comp,3,username)
            else:
                Countplayerwins = int(userstats[2])
                symbols_player = [int(userstats[3]),int(userstats[4]),int(userstats[5]),int(userstats[6]),int(userstats[7])]
                aufrufen(Countplayerwins,Countcompwins,symbols_player,symbols_comp,3,username)
        elif choice == "2":
            username = str(input("Username: "))
            userstats = getDatafromMysql(username)
            if userstats == "NoUser":
                print("User nicht gefunden")
            else:
                Countplayerwins = int(userstats[2])
                symbols_player = [int(userstats[3]),int(userstats[4]),int(userstats[5]),int(userstats[6]),int(userstats[7])]
                statistics( Countplayerwins,symbols_player)
        elif choice == "3":
            getDatafromMysqltoJson()
        elif choice == "4":
            print("Auf Wiedersehen")
            playing = False
        else: print("Falsche Eingabe")
    exit()