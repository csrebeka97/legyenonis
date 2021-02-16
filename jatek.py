import kerdesek
import dicsosegtabla
import time
import pyconio
import random
import grafika

#kozonseg segitseget adja meg
def kozonseg(ujkerdes, kozonsegetkerhet):
    if kozonsegetkerhet == False:
        print("Már felhasználtad ezt a segítséget!")
    else:
        a = grafika.Pozicio("A",2,10)
        b = grafika.Pozicio("B",45,10)
        c = grafika.Pozicio("C",2,20)
        d = grafika.Pozicio("D",45,20)
        
        if ujkerdes.megoldas == "A":
            grafika.kozonsegkiiro(a,b,c,d)            
        elif ujkerdes.megoldas =="B":
            grafika.kozonsegkiiro(b,a,c,d)
        elif ujkerdes.megoldas =="C":
            grafika.kozonsegkiiro(c,a,b,d)
        elif ujkerdes.megoldas == "D":
            grafika.kozonsegkiiro(d,a,b,c)            

#felezo segitseget adja meg
def felezo(ujkerdes,felezhet,szerzettpont,pontok):
    if felezhet == False:
        print("Már felhasználtad ezt a segítséget!")
    else:
        pyconio.clrscr()
        pyconio.gotoxy(10,0)
        print(ujkerdes.kerdes)
        nyeremenyek(szerzettpont,pontok)
        a = grafika.Pozicio("A",7,10)
        b = grafika.Pozicio("B",50,10)
        c = grafika.Pozicio("C",7,20)
        d = grafika.Pozicio("D",50,20)
        poz = [a,b,c,d]
        if ujkerdes.megoldas == "A":
           grafika.megfelez(ujkerdes,a,poz)
        elif ujkerdes.megoldas == "B":
           grafika.megfelez(ujkerdes,b,poz)
        elif ujkerdes.megoldas == "C":
            grafika.megfelez(ujkerdes,c,poz)
        elif ujkerdes.megoldas == "D":
            grafika.megfelez(ujkerdes,d,poz)
        

#pontlista kirajzolása, megszerzett pont megjelölése    
def nyeremenyek(szerzettpont,pontok):
    pyconio.gotoxy(110,8)
    print("Pontok")
    pyconio.gotoxy(110,10)
    for i in range(0,len(pontok)):
        if pontok[i] == szerzettpont:
            pyconio.textbackground(pyconio.WHITE)
            print(pontok[i])
            pyconio.gotoxy(110,10+i+1)
            pyconio.textbackground(pyconio.BLACK)
        else:
            print(pontok[i])
            pyconio.gotoxy(110,10+i+1)
            
def vege(jatekosok, now,szerzettpont):
    end = time.time()
    dur = (end-now)/60
    dur = round(dur,2)
    nev = input("Add meg a neved: ")                
    sz = dicsosegtabla.Szemely(nev,dur,int(szerzettpont))
    jatekosok.append(sz)
    pyconio.clrscr()                
    dicsosegtabla.listaz(jatekosok)
    dicsosegtabla.kiir(jatekosok)
    
def kerdeskiiro(i,ujkerdes):
    pyconio.gotoxy(10,0)
    print(i+1,". kérdés")
    pyconio.gotoxy(100,2)
    print("K. Közönség segítség")
    pyconio.gotoxy(100,5)
    print("F. Felezés")    
    print(ujkerdes.kerdes)    
    pyconio.gotoxy(7,10)
    print("A."+ujkerdes.a)
    pyconio.gotoxy(50,10)
    print("B."+ujkerdes.b)
    pyconio.gotoxy(7,20)
    print("C."+ujkerdes.c)
    pyconio.gotoxy(50,20)
    print("D."+ujkerdes.d,"\n\n\n")
    
 #uj jatek indítása   
def ujjatek(jatekosok):
    now = time.time()
    print("Jó játékot!")
    osszeskerdes = kerdesek.beolvas()
    szint = input("Válaszd ki a nehézséget! 1-10: ")
    szintkerdesek = []
    szintkerdesek = kerdesek.nehezsegvalaszto(szint, osszeskerdes)
    pyconio.clrscr()
    print("1. Mind\n2. Általános\n3. Biológia\n4. Építészet\n5. Film\n6. Földrajz\n7. Irodalom\n8. Játék\n9. Képzőművészet\n10. Konyha\n11. Magyarország")
    print("12. Művészet\n13. Nyelv\n14. Opera\n15. Országok\n16. Sport\n17. Színház\n18. Technika\n19. Történelem\n20. Tudomány\n21. Vallás\n22. Zene")
    kateg = int(input("Válaszd ki a kategóriát a kategória sorszámának megadásával!: "))
    kategkerdesek = kerdesek.kategvalaszto(kateg,szintkerdesek)    
    pyconio.clrscr()
    pontok = [5000,10000,25000,50000,100000,200000,300000,500000,800000,1500000,3000000,5000000,10000000,20000000,40000000]
    jatszhat = True
    i = 0
    szerzettpont =0
    kozonsegetkerhet = True
    felezhet = True
    while jatszhat == True :
        ujkerdes = random.choice(kategkerdesek)
        kerdeskiiro(i,ujkerdes)
        nyeremenyek(szerzettpont,pontok)
        pyconio.gotoxy(7,25)
        valasz = input("Add meg a válasz betűjelét: ")
        if valasz == "K" or valasz == "k" or valasz == "F" or valasz == "f":
            if valasz == "K" or valasz == "k":
                kozonseg(ujkerdes,kozonsegetkerhet)
                kozonsegetkerhet =False
                pyconio.gotoxy(7,25)
                valasz = input("Add meg a válasz betűjelét: ")
            elif valasz == "F" or valasz == "f":
                felezo(ujkerdes,felezhet,szerzettpont,pontok)
                felezhet = False
                pyconio.gotoxy(7,25)
                valasz = input("Add meg a válasz betűjelét: ")
        jovalasz = (valasz == ujkerdes.megoldas or valasz.upper() ==ujkerdes.megoldas)
        grafika.szinezo(valasz,jovalasz,ujkerdes)
        if jovalasz == True:
            szerzettpont = pontok[i]
            i=i+1
            pyconio.clrscr()
            if i ==15:
                print("Gratulálunk, nyertél!")
                vege(jatekosok,now,szerzettpont)                
                jatszhat=False                
        else:
            print("A játék véget ért")
            vege(jatekosok,now,szerzettpont)            
            jatszhat = False
           
            
        
        
        
        
    
            
    