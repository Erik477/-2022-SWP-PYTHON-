import random

def Lottoziehung():
    ziehungen = []
    #test = []
    for x in range(1, 46):
        ziehungen.append(x)
    for x in range(0, 6):
        index = random.randrange(len(ziehungen) - x)
        rand = ziehungen[index]
        ziehungen[len(ziehungen) - 1 - x] = rand
        ziehungen[index] = len(ziehungen) - x
    
    #for x in range(39,45):
        #test.append(x)
    
    #print(test)
    #print(ziehungen[39:45])

    return ziehungen[39:45]

stat = {}

def Statistik(ziehungen):
    for b in range(0,5):
        value = ziehungen[b]
        count = stat[value] 
        #print(count)
        stat[value] = count + 1
    #print(stat)
    
    
def aufrufen(wieoft):
    for x in range(1, 46):
        stat[x] = 0
    for wieoft in range(0, wieoft):
        Statistik(Lottoziehung())
    print(stat)

if __name__ == '__main__':
    aufrufen(1000)

