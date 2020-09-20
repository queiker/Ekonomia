debug_code = True

#
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



def transpozycja_macierzy_kwadratowej(macierz):
    # funkcja zwraca macirz transponowaną
    

    macierz_T = []
    
    kolumna_T = 0
    for row in range (0, len(macierz)):
        macierz_T.append([])
        for column in range (0, len(macierz)):
            # debug code
            #print(f"kolumna : {column} rząd : {row} wartość : {macierz[column][row]}")
            macierz_T[kolumna_T].append(macierz[column][row])
        kolumna_T += 1

    return(macierz_T)



def mnożenie_macierzy_kwadratowych(macierz_A, macierz_B):
    # mnoży się pierwszy rząd przez pierwszą kolumnę potem mnoży się  pierwszy rząd przez drugą kolumnę potem 3 rząd przz 3 kolumnę
    # potem drugi wiersz przez pierwszą kolumnę i tak do końca...
    # funkcja nie obsługuje macirzy prostokątnych
    

    rows_A = []
    columns_B = []

    for row in range(0, len(macierz_A)):
        columns_B.append([])
        for column in range(0, len(macierz_A)):
            if debug_code == True:
                print(macierz_B[column][row])
            columns_B[row].append(macierz_B[column][row])


    for column in range(0, len(macierz_A)):
        rows_A.append([])
        for row in range(0, len(macierz_A)):
            if debug_code == True:
                print(macierz_A[column][row])
            rows_A[column].append(macierz_A[column][row])
        
    wynik = []
    
    for wynik_row in range(0, len(macierz_A)):
        wynik.append([])
        for wynik_column in range(0, len(macierz_A)):
            suma = 0
            for pozycja in range(0, len(macierz_A)):
                suma += rows_A[wynik_row][pozycja]*columns_B[wynik_column][pozycja]
            wynik[wynik_row].append(suma)
            
    return wynik
    

def main():
    x = 1
    print("\n" * 30)
    while (x != 0):
                
        print("""Witaj w programie EKONOMIA napisanym przez Grzegorza Płonkę:

        1) Procent składany z kapitalizacją roczną
        2) Procent składany z kapitalizacją między okresową
        3) Prognozowanie ekonometryczne
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
        elif x == 3:
            print("\n" * 30)
            # metoda najmniejszych kwadratów jest dobrze opowiedziana na poniższym linku:
            # https://www.youtube.com/watch?v=N2Dzck8TmxY&list=WL&index=60&t=31s
            # y = a1x1 + a2x2 + a0
            # z poniższego wzoru a jest macirzą z współczynnikami alfa od góry alfa0, alfa1 itd...
            # a = (XtX)^(-1)*(XtY)

            # do programu trzeba wprowadzić macirz y zawierającą wyniki z x lat
            y = [3,3.5,5,4,3,4.5,6,5.5,4,7]
            # trzeba też wprowadzić x1,x2
            x = [[2,7],[2.5],[4,10],[3.5,8],[3,15],]



            #macierz = [[1,2,3,4,1],[5,6,7,8,1],[9,10,11,12,1],[13,14,15,16,1],[1,2,3,4,5]]
            #print(transpozycja_macierzy_kwadratowej(macierz))
            # macierz_A = [[-1,-2,3],[0,2,-1],[-1,3,0]]
            # macierz_B = [[1,5,1],[2,1,2],[3,2,3]]
            # print(mnożenie_macierzy_kwadratowych(macierz_A,macierz_B))
        

        else :
            pass
        
main()

