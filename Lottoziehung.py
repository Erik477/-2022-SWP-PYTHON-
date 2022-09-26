import random

def Lottoziehung(wiederholungen):
    Ziehungen = {}
    for x in range(1, wiederholungen + 1):
        Ziehungen[x] = random.randint(1, 45)
    print(Ziehungen)

def LottoziehungOhneDoppelt(wiederholungen):
    Ziehungen = {}
    zusaetzlich = 0 
    for x in range(1, wiederholungen + 1):
        Randnum = random.randint(1, 45)
        for y in Ziehungen:
            if Ziehungen[y] == Randnum:
                Randnum = 50
                zusaetzlich + 1
        if Randnum != 50:
            Ziehungen[x] = Randnum
    

    print(Ziehungen)
    
LottoziehungOhneDoppelt(45)