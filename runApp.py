#-*- coding: windows-1250 -*-
'''tu opis techniczny, dokładny co i jak się dzieje'''
import glob
import os

print """tu należy dodać opis, co robi, jak robi i po co
to ważne\n"""


lista_plikow = glob.glob('*.txt') #moduł glob.glob tworzy listę pliów, w nawiassach podajemy ścieżkę
                                # tu wystarczy '*.txt' - lista wszystkich plików txt w folderze,
                                # w którym jest program
if lista_plikow == []: # sprawdza czy są pliki, jeśli nie to lista_plikow jest pusta
    raw_input("Nie ma plików")
    exit()
else:
    print 'Lista plików w folderze:' # wyświetla w konsoli tekst 'lista.. bala bla bal'
    licznik=0
    for plik in lista_plikow: #pętla for -> dla każdego emelentu (tu pliku) z listy (lista_plikow) zrób:
        licznik +=1             # licznik+1(bo indeks listy jest od 0)
        print licznik, plik # wyświetl licznik oraz nazwę pliku

index_nawy_pliku =  raw_input('Aby zakonczyc wpisz: koniec\nlub podaj numer pliku: ')

while True:
    if index_nawy_pliku == 'koniec':
        raw_input('Koniec, dowolny klawisz aby zakończyć')
        exit()

    try:
        index_nawy_pliku = int(index_nawy_pliku)-1
        if index_nawy_pliku == -1: # własny wyjątek, bo gdy index == -1 to odwołuje się do ostatniego elementu listy
            raise
        nazwa_pliku = lista_plikow[index_nawy_pliku]
        print "Wybrano plik:", nazwa_pliku
        break # przerywa działanie pętli
    except:
        print 'Podano złą wartość'
        index_nawy_pliku =  raw_input('Podaj numer pliku: ')


korekta = raw_input('Aby zakonczyc wpisz: koniec\nlub podaj wartość: ')


while True:
    if korekta == 'koniec':
        raw_input('Koniec, dowolny klawisz aby zakończyć')
        exit()
    try:
        korekta = float(korekta)
        print "Wybrano wartosc:", korekta
        break
    except:
        print 'Podano złą wartość'
        korekta = raw_input('Podaj poprawną wartość: ')


plik_wyjsciowy = raw_input('Podaj nazwę pliku wyjściowego\n[enter]\t->\t domyślna nazwa:\twynikowy.txt\n<nazwa bez rozszerzenia>: ')


if plik_wyjsciowy == '':
    plik_wyjsciowy = 'wynik.txt'
elif plik_wyjsciowy == 'koniec':
    raw_input('Koniec, dowolny klawisz aby zakończyć')
else:
    plik_wyjsciowy = plik_wyjsciowy+'.txt'


os.system('cls')


print '\n'*50

print "Wybrano plik:", nazwa_pliku
print "Wybrano wartosc:", korekta
print "Wybrano plik wyjściowy:", plik_wyjsciowy

plik_zrodlowy = open(nazwa_pliku) #można tak pracować z plikiem, tylko trzeba pamiętać zamknąć
with open(plik_wyjsciowy, 'w') as f: # lub tak (wtedy z plik automatycznie zostanie zamknięty)
    for linia in plik_zrodlowy:
        linia = linia.rstrip('\n') # usuwa znak końca linii
        linia = linia.split(';') # dzieli linie na listę, separatorem jest ;
        id_wartosci = linia[0] #pobiera element z 1. kolumny (index 0)
        wartosc = linia[1] #pobiera element z 2. kolumny (index 1)
        przelicz = linia[2] #pobiera element z 3. kolumny (index 2)
        if przelicz == 'K': # jesli 'K' w 3 kolumnie to:
            nowa_wartosc = float(wartosc) + korekta #float(x) zamienia tekst (string) na liczbe zmienno przecinkową
            nowa_wartosc = str(nowa_wartosc)
        else:
                nowa_wartosc = wartosc

        print id_wartosci, wartosc, nowa_wartosc, przelicz
        # f.write(id_wartosci+';'+nowa_wartosc+';'+przelicz+'\n')
        f.write(';'.join([id_wartosci, nowa_wartosc, przelicz+'\n']))

plik_zrodlowy.close()

raw_input('koniec')





