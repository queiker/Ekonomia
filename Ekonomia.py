def procent_skladany_roczny():
    print("\n" * 30)
    print("""Procent składany z kapitalizacją roczną 
    """)
    kapital_poczatkowy = float(input("Podaj kapitał początkowy : "))
    oprocentowanie_roczne = float(input("Podaj liczbę oznaczającą oprocentowanie roczne : "))
    ile_lat = float(input("Na ile lat ma być złożony depozyt : "))
    return kapital_poczatkowy * (1 + (oprocentowanie_roczne / 100)) ** ile_lat

def procent_skladany_kapitalizacja_miedzyokresowa():
    print("\n" * 30)
    print("""Procent składany z kapitalizacją między okresową 
    """)
    kapital_poczatkowy = float(input("Podaj kapitał początkowy : "))
    oprocentowanie_roczne = float(input("Podaj liczbę oznaczającą oprocentowanie roczne : "))
    ile_lat = float(input("Na ile lat ma być złożony depozyt : "))
    liczba_rocznych_kapitalizacji = float(input("Ile razy w roku ma być kapitalizowany depozyt? : "))
    return kapital_poczatkowy * (1 + ((oprocentowanie_roczne / 100)/liczba_rocznych_kapitalizacji)) ** (ile_lat*liczba_rocznych_kapitalizacji)


def main():
    x = 1
    print("\n" * 30)
    while (x != 0):
                
        print("""Witaj w programie EKONOMIA napisanym przez Grzegorza Płonkę:

        1) Procent składany z kapitalizacją roczną
        2) Procent składany z kapitalizacją między okresową
        0) Wyjście

        """)
        x = int(input("Podaj numer żeby wejść do odpowiedniej części programu "))
        if x == 0:
            return
        elif x == 1:
            print("\n" * 30)
            print(procent_skladany_roczny())
        elif x == 2:
            print("\n" * 30)
            print(procent_skladany_kapitalizacja_miedzyokresowa())
        else :
            return
        
main()

