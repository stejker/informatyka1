
# Imię : Adam
# Nazwisko : Sawicki
# Kierunek : Energetyka Semestr I
# Zadanie : Szukanie Pomidorów

SZUKAMY = 'pomidor'
NAZWA_PLIKU = 'pomidorek.txt'


with open(NAZWA_PLIKU, encoding='utf-8') as plik:
    tekst = plik.read()
    
tekst = tekst.lower()

licznik = 0

i = 0
n = len(SZUKAMY)

j = 0


while True:
    try:
        while tekst[j] != SZUKAMY[i]:
            j = j + 1
            
        licznik = licznik + 1
        i = (i + 1) % n
        j = j + 1
    except:
        break
    
print('liczba występień = ', licznik)
    