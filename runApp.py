#-*- coding: windows-1250 -*-
'''tu opis techniczny, dok�adny co i jak si� dzieje'''
import glob
import os

print """tu nale�y doda� opis, co robi, jak robi i po co
to wa�ne\n"""


lista_plikow = glob.glob('*.txt') #modu� glob.glob tworzy list� pli�w, w nawiassach podajemy �cie�k�
                                # tu wystarczy '*.txt' - lista wszystkich plik�w txt w folderze,
                                # w kt�rym jest program
if lista_plikow == []: # sprawdza czy s� pliki, je�li nie to lista_plikow jest pusta
    raw_input("Nie ma plik�w")
    exit()
else:
    print 'Lista plik�w w folderze:' # wy�wietla w konsoli tekst 'lista.. bala bla bal'
    licznik=0
    for plik in lista_plikow: #p�tla for -> dla ka�dego emelentu (tu pliku) z listy (lista_plikow) zr�b:
        licznik +=1             # licznik+1(bo indeks listy jest od 0)
        print licznik, plik # wy�wietl licznik oraz nazw� pliku

index_nawy_pliku =  raw_input('Aby zakonczyc wpisz: koniec\nlub podaj numer pliku: ')

while True:
    if index_nawy_pliku == 'koniec':
        raw_input('Koniec, dowolny klawisz aby zako�czy�')
        exit()

    try:
        index_nawy_pliku = int(index_nawy_pliku)-1
        if index_nawy_pliku == -1: # w�asny wyj�tek, bo gdy index == -1 to odwo�uje si� do ostatniego elementu listy
            raise
        nazwa_pliku = lista_plikow[index_nawy_pliku]
        print "Wybrano plik:", nazwa_pliku
        break # przerywa dzia�anie p�tli
    except:
        print 'Podano z�� warto��'
        index_nawy_pliku =  raw_input('Podaj numer pliku: ')


korekta = raw_input('Aby zakonczyc wpisz: koniec\nlub podaj warto��: ')


while True:
    if korekta == 'koniec':
        raw_input('Koniec, dowolny klawisz aby zako�czy�')
        exit()
    try:
        korekta = float(korekta)
        print "Wybrano wartosc:", korekta
        break
    except:
        print 'Podano z�� warto��'
        korekta = raw_input('Podaj poprawn� warto��: ')


plik_wyjsciowy = raw_input('Podaj nazw� pliku wyj�ciowego\n[enter]\t->\t domy�lna nazwa:\twynikowy.txt\n<nazwa bez rozszerzenia>: ')


if plik_wyjsciowy == '':
    plik_wyjsciowy = 'wynik.txt'
elif plik_wyjsciowy == 'koniec':
    raw_input('Koniec, dowolny klawisz aby zako�czy�')
else:
    plik_wyjsciowy = plik_wyjsciowy+'.txt'


os.system('cls')


print '\n'*50

print "Wybrano plik:", nazwa_pliku
print "Wybrano wartosc:", korekta
print "Wybrano plik wyj�ciowy:", plik_wyjsciowy

plik_zrodlowy = open(nazwa_pliku) #mo�na tak pracowa� z plikiem, tylko trzeba pami�ta� zamkn��
with open(plik_wyjsciowy, 'w') as f: # lub tak (wtedy z plik automatycznie zostanie zamkni�ty)
    for linia in plik_zrodlowy:
        linia = linia.rstrip('\n') # usuwa znak ko�ca linii
        linia = linia.split(';') # dzieli linie na list�, separatorem jest ;
        id_wartosci = linia[0] #pobiera element z 1. kolumny (index 0)
        wartosc = linia[1] #pobiera element z 2. kolumny (index 1)
        przelicz = linia[2] #pobiera element z 3. kolumny (index 2)
        if przelicz == 'K': # jesli 'K' w 3 kolumnie to:
            nowa_wartosc = float(wartosc) + korekta #float(x) zamienia tekst (string) na liczbe zmienno przecinkow�
            nowa_wartosc = str(nowa_wartosc)
        else:
                nowa_wartosc = wartosc

        print id_wartosci, wartosc, nowa_wartosc, przelicz
        # f.write(id_wartosci+';'+nowa_wartosc+';'+przelicz+'\n')
        f.write(';'.join([id_wartosci, nowa_wartosc, przelicz+'\n']))

plik_zrodlowy.close()

raw_input('koniec')





