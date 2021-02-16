#jatekosok tárolásához
class Szemely:
    def __init__(self, nev,ido,pont):
        self.nev = nev
        self.ido = ido
        self.pont = pont
#beolvassa a jatekosokat a dicsoseglista.txt-ből, amennyiben nincs ilyen, akkor újat hoz létre        
def beolvas():
    jatekosok = []
    try:
        f = open("dicsoseglista.txt","r")
        sor = f.readline()
        for sor in f:
            sor = sor.rstrip("\n")
            darabok = sor.split("\t")
            sz = Szemely(str(darabok[0]),darabok[1],int(darabok[2]))
            jatekosok.append(sz)        
        return jatekosok
    except Exception:
        f = open("dicsoseglista.txt","w")        
        return jatekosok
    finally:
        f.close()
    
#txt-be kiírja a játékosokat
def kiir(jatekosok):
    f = open("dicsoseglista.txt","a")
    for i in jatekosok:
        f.write(i.nev+"\t"+str(i.ido)+"\t"+str(i.pont)+"\n")
    f.close()

    
#pontszám szerint csökkenő sorrendben elmenti a jatekosok listát, majd kilistázza azt (max 10et)
def listaz(jatekosok):
    jatekosok.sort(reverse = True, key=lambda x: x.pont)
    print("Helyezés Név Játékidő   Pont")
    if len(jatekosok)>=10:
        for i in range(0,10):
            print(i+1,"\t",jatekosok[i].nev,"\t",jatekosok[i].ido,"\t",jatekosok[i].pont,"\n")
    else:
        for i in range(0,len(jatekosok)):
            print(i+1,"\t",jatekosok[i].nev,"\t",jatekosok[i].ido,"\t",jatekosok[i].pont,"\n")

