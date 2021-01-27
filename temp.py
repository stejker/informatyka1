
# Imię : Adam
# Nazwisko : Sawicki
# Kierunek : Energetyka Semestr I
# Zadanie : Szukanie Pomidorów

SZUKAMY = 'pomidor'
NAZWA_PLIKU = 'pomidorek.txt'


with open(NAZWA_PLIKU, encoding='utf-8') as plik:
    tekst = plik.read() # odczytuje plik
    
tekst = tekst.lower() # zmienia wszystkie litery w tekcie na małe

licznik = 0 # liczba pomidorów

i = 0 # pozycja litery w łańcuchu SZUKAMY

n = len(SZUKAMY) # długoć łańcucha SZUKAMY

j = 0 # pozycja litery w łańcuchu tekst

m = len(tekst) # długoć łańcucha tekst

while j < m:
    while j < m and tekst[j] != SZUKAMY[i]:
        j = j + 1
    
    licznik = licznik + 1 # zlicza liczbę pomidorów
    i = (i + 1) % n
    j = j + 1
    
licznik = licznik // 7  # dziele przez liczbę liter w słowie pomidor by otrzymać prawdziwy wynik

print('liczba występień = ', licznik)
