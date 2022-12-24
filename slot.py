#Budget: 1500€
#3 Reihen mit jeweils 3 Simbolen (X=2;O=0;V=1)
#3X ist Hauptgewinn (Vervierfachung der Eingabe)
#2O ist 1.5fachung
#3O ist Verdopplung
#Verlust
#sys.exit()

import random as rnd
#print(rnd.randint(1,3))
geld = 1500
mult = 0

def gewinn():
    i=0
    while i < len(ausgabe):
        double=0
        for x in ausgabe:
            if ausgabe[i] == x:
                double+=1
        if double == 2 and ausgabe[i]==0:
            print(1)
            return 1.5
        if double == 3 and ausgabe[i]!=1:
            if ausgabe[i]==0:
                print(2)
                return 2
            if ausgabe[i]==0:
                print(3)
                return 4
        i+=1
    print(4)
    return -1

def zuordnung(x, y, z):
    ausgabe = []
    if x==1:
        ausgabe.append("Nischts")
    elif x==0:
        ausgabe.append("Banane")
    else:
        ausgabe.append("Kirsche")

    if y==1:
        ausgabe.append("Nischts")
    elif y==0:
        ausgabe.append("Banane")
    else:
        ausgabe.append("Kirsche")

    if z==1:
        ausgabe.append("Nischts")
    elif z==0:
        ausgabe.append("Banane")
    else:
        ausgabe.append("Kirsche")

w = input(f"Das ist die Schlottmaschine\nDu hast {geld}€ Budget!\nPress Enter")

while True:
    inns = int(input("Gib deinen Einsatz!\n"))
    while inns>geld or not isinstance(inns, int):
        inns = int(input("Gib weniger!\n"))

    ausgabe = []
    for i in range(3):
        ausgabe.append(rnd.randint(0,2))

    mult=gewinn()
    print(ausgabe)
    zuordnung(ausgabe[0], ausgabe[1], ausgabe[2])
    geld+=inns*mult
    print(f"Du hast jetzt {geld}€")
    w=input(ausgabe)
    







#break
sys.exit()