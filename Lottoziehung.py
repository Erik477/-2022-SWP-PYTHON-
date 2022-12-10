import random

def Lottoziehung(anzZiehungen,maxZahl):
    ziehungen = []
    #test = []
    for x in range(1, maxZahl + 1):
        ziehungen.append(x)
    for x in range(0, anzZiehungen):
        index = random.randrange(len(ziehungen) - x)

        rand = ziehungen[index]
        last_pos = len(ziehungen) -1 - x
        ziehungen[last_pos],ziehungen[index]=ziehungen[index],ziehungen[last_pos]

        #ziehungen[len(ziehungen) - 1 - x] = rand
        #ziehungen[index] = len(ziehungen) - x
    
    #for x in range(39,45):
        #test.append(x)
    
    #print(test)
    #print(ziehungen[-anzZiehungen:])

    return ziehungen[-anzZiehungen:]


def Statistik(ziehungen,anzZiehungen):
    for b in range(0,anzZiehungen-1):
        value = ziehungen[b]
        count = stat[value] 
        #print(count)
        stat[value] = count + 1
    #print(stat)
    
    
def aufrufen(wieoft,anzZiehungen,maxZahl):
    for x in range(1, maxZahl + 1):
        stat[x] = 0
    for wieoft in range(0, wieoft):
        Statistik(Lottoziehung(anzZiehungen,maxZahl),anzZiehungen)
    print(stat)

if __name__ == '__main__':
    stat = {}
    wieoft = 1000000
    anzZiehungen = 6
    maxZahl = 10
    aufrufen(wieoft,anzZiehungen,maxZahl)


