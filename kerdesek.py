#kerdes class
class Kerdes:
    
    def __init__(self, nehezseg,kerdes, a,b,c,d,megoldas,kateg):
        self.kerdes = kerdes
        self.a = a
        self.b= b
        self.c = c
        self.d = d
        self.megoldas = megoldas
        self.nehezseg = nehezseg
        self.kateg = kateg
        
#kerdesek beolvasasa a mappaban talalhato kerdesek.txt fájlból
def beolvas():
    f = open("kerdesek.txt","r")
    kerdeslista = []
    sor = f.readline()
    for sor in f:
        sor = sor.rstrip("\n")
        darabok = sor.split("\t")
        k = Kerdes(darabok[0],darabok[1],darabok[2],darabok[3],darabok[4],darabok[5],darabok[6],darabok[7])      
        kerdeslista.append(k)
    f.close()
    return kerdeslista

#kiválogatja az inputként kapott nehézségi szinthez tartozó kérdéseket
def nehezsegvalaszto(szint,osszeskerdes):
    nehezsegKerdesek = []
    for i in osszeskerdes:
        
        if i.nehezseg == szint:
            nehezsegKerdesek.append(i)
    return nehezsegKerdesek
#kiválogatja az inputként kapott kategóriához tartozó kérdéseket
def kategoria (kateg,kerdeslista):
    kategKerdesek = []
    for i in kerdeslista:
        if kateg == 1:
            return kerdeslista
            
        elif i.kateg == kateg:
            kategKerdesek.append(i)
    return kategKerdesek
        
#megkapott sorszám alapján meghívja a kategóriához tartozó kategoria() függvényt        
def kategvalaszto(kateg,kerdesek):
    print("1. Mind\n2. Általános\n3. Biológia\n4. Építészet\n5. Film\n6. Földrajz\n7. Irodalom\n8. Játék\n9. Képzőművészet\n10. Konyha\n11. Magyarország")
    print("12. Művészet\n13. Nyelv\n14. Opera\n15. Országok\n16. Sport\n17. Színház\n18. Technika\n19. Történelem\n20. Tudomány\n21. Vallás\n22. Zene")
    temak = {
        1: "Mind",
        2: "ÁLTALÁNOS",
        3: "BIOLÓGIA",
        4: "ÉPÍTÉSZET",
        5: "FILM",
        6: "FÖLDRAJZ",
        7: "IRODALOM",
        8: "JÁTÉK",
        9: "KÉPZŐMŰVÉSZET",
        10: "KONYHA",
        11: "MAGYARORSZÁG",
        12: "MŰVÉSZET",
        13: "NYELV",
        14: "OPERA",
        15: "ORSZÁGOK",
        16: "SPORT",
        17: "SZÍNHÁZ",
        18: "TECHNIKA",
        19: "TÖRTÉNELEM",
        20: "TUDOMÁNY",
        21: "VALLÁS",
        22: "ZENE" }   
    if kateg == 1:
        katkerdesek = kategoria(kateg,kerdesek)
        return katkerdesek
    else:
        katkerdesek = kategoria(temak[kateg],kerdesek)
        return katkerdesek
        
    
        
    
    
    
    