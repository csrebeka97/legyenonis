import pyconio
import jatek
import dicsosegtabla
import kerdesek
import time    
    
def main():
    choice = '0'
    pyconio.gotoxy(50,0)
    print("Legyen Ön is Milliomos!\n\n")
    pyconio.settitle('Legyen Ön is Milliomos!')
    jatekosok = dicsosegtabla.beolvas()
    menu(choice, jatekosok)
    
def menu(choice, jatekosok):
    while choice != '3':
        pyconio.textbackground(pyconio.BLACK)
        pyconio.textcolor(pyconio.LIGHTBLUE)
        pyconio.gotoxy(50,5)
        print("1. Új játék")
        pyconio.gotoxy(50,7)
        print("2. Dicsőséglista")
        pyconio.gotoxy(50,9)
        print("3. Kilépés")
        pyconio.gotoxy(50,20)
        choice=input("Írd be a választásod: ")
        print(choice)    
        #uj jatek kezdese
        if choice == '1':
            print("Új játék kezdése")
            pyconio.clrscr()
            jatek.ujjatek(jatekosok)        
        #dicsosegtabla kiirasa   
        elif choice == '2':
            pyconio.clrscr()
            dicsosegtabla.listaz(jatekosok)
        #kilepes    
        elif choice == '3':
            pyconio.clrscr()
            print("Viszlát!")
            break
        #ha 1-2-3 karakteren kívül mást kapna inputba
        else:
            pyconio.clrscr()
            print("Érvénytelen választás\n")
main()



