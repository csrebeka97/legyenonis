import pyconio
import time
import random

class Pozicio:
    nev = None
    x = None
    y = None
    
    def __init__(self,nev,x,y):
        self.nev = nev
        self.x = x
        self.y = y
        
def kozonsegkiiro(megoldaspoz,maspoz,harmpoz,negypoz):
    szamolo = 100
    szaz1= random.randrange(50,100)
    szamolo = szamolo-szaz1
    pyconio.gotoxy(megoldaspoz.x,megoldaspoz.y)
    print(szaz1, "%")
    pyconio.gotoxy(maspoz.x,maspoz.y)
    szaz2 = random.randrange(0,szamolo)
    szamolo = szamolo-szaz2
    print(szaz2, "%")
    pyconio.gotoxy(harmpoz.x, harmpoz.y)
    szaz3 = random.randrange(0,szamolo)
    szamolo = szamolo-szaz3
    print(szaz3,"%")
    pyconio.gotoxy(negypoz.x, negypoz.y)
    szaz4 = szamolo
    print(szaz4, "%")

def megfelez(kerdes,megoldas,poziciok):
    poziciok.remove(megoldas)
    kerddict = {"A": kerdes.a, "B": kerdes.b, "C": kerdes.c, "D": kerdes.d}
    pyconio.gotoxy(megoldas.x,megoldas.y)
    print(megoldas.nev,".", kerddict[megoldas.nev])
    masik = random.choice(poziciok)
    pyconio.gotoxy(masik.x,masik.y)
    print(masik.nev,". ",kerddict[masik.nev])
    
#kiszinezi a valós jó választ zöld hátterűre                   
def jovalaszszinezo(ujkerdes, poz):
    kerddict = {"A": ujkerdes.a, "B": ujkerdes.b, "C": ujkerdes.c, "D": ujkerdes.d}
    pyconio.gotoxy(poz.x,poz.y)
    pyconio.textbackground(pyconio.LIGHTGREEN)
    print(poz.nev+"."+kerddict[ujkerdes.megoldas])
    pyconio.textbackground(pyconio.BLACK)
    time.sleep(1)
    
#kiszinezi a rossz választ piros hátterűre   
def rosszvalaszszinezo(ujkerdes,pozi):            
    a = Pozicio("A",7,10)
    b = Pozicio("B",50,10)
    c = Pozicio("C",7,20)
    d = Pozicio("D",50,20)   
    poz = {"A":a,"B":b,"C":c,"D":d}
    kerddict = {"A": ujkerdes.a, "B": ujkerdes.b, "C": ujkerdes.c, "D": ujkerdes.d}
    pyconio.gotoxy(pozi.x,pozi.y)
    pyconio.textbackground(pyconio.RED)
    print(pozi.nev+"."+kerddict[pozi.nev])
    jovalaszszinezo(ujkerdes,poz[ujkerdes.megoldas])
    pyconio.textbackground(pyconio.BLACK)
    time.sleep(1)
    pyconio.clrscr()
    
#amikor a játékos választott akkor kiszinezi a választ magenta hátterűre, majd vár   
def valasztasszinezo(ujkerdes,poz):
    kerddict = {"A": ujkerdes.a, "B": ujkerdes.b, "C": ujkerdes.c, "D": ujkerdes.d}
    pyconio.gotoxy(poz.x,poz.y)
    pyconio.textbackground(pyconio.MAGENTA)
    print(poz.nev+"."+kerddict[poz.nev])
    time.sleep(3)
    
#kiszinezi a kiválasztott válaszlehetőséget
def szinezo(valasz,jovalasz,ujkerdes):
    a = Pozicio("A",7,10)
    b = Pozicio("B",50,10)
    c = Pozicio("C",7,20)
    d = Pozicio("D",50,20)     
    if valasz == "A" or valasz == "a":
        valasztasszinezo(ujkerdes,a)
        if jovalasz == True:
            jovalaszszinezo(ujkerdes,a)
        else:
            rosszvalaszszinezo(ujkerdes,a)            
    elif valasz == "B" or valasz == "b":
        valasztasszinezo(ujkerdes,b)
        if jovalasz == True:
            jovalaszszinezo(ujkerdes,b)
        else:
            rosszvalaszszinezo(ujkerdes,b)            
    elif valasz == "C" or valasz =="c":
        valasztasszinezo(ujkerdes,c)
        if jovalasz == True:
            jovalaszszinezo(ujkerdes,c)
        else:
            rosszvalaszszinezo(ujkerdes,c)
    elif valasz == "D" or valasz == "d": 
        valasztasszinezo(ujkerdes,d)
        if jovalasz == True:
            jovalaszszinezo(ujkerdes,d)
        else:
            rosszvalaszszinezo(ujkerdes,d)