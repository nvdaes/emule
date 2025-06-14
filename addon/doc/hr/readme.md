# eMule #

*	Autori: Noelia, Chris, Alberto.

Ovaj dodatak poboljšava pristupačnostof eMule programa uz pomoć NVDA
čitača. Također pruža dodatne tipkovničke prečace za premještanje po
različitim prozorima i daje korisne informacije u eMuleu.

Ovaj je dodatak baziran na dodatku eMuleNVDASupport, kojeg je razvio isti
autor. Stari se dodatak mora deinstalirati, kako bi se mogao koristiti ovaj
dodatak, jer oba dodatka imaju zajedničke tipkovničke prečace i značajke.

Tested on [eMule][1] 0.50a and 70b.

## Tipkovnički prečaci: ##

*	kontrol+šift+h: Premješta fokus i miša na glavnu alatnu traku.
*	kontrol+šift+t: Čita trenutačni prozor.
*	kontrol+šift+n: Premješta fokus na polje za ime u prozoru pretrage.
*	kontrol+šift+p: U prozoru pretrage, premješta fokus i miša na popis
  parametara pretrage ili na opcije uređivačkog polja.
*	kontrol+šift+b: Premješta fokus na popis u trenutačnom prozoru. Na
  primjer, korisno u prozoru pretrage, preuzimanja u prozoru transfera, itd.
*	kontrol+šift+o: Premješta fokus na polja za uređivanje koja su samo za
  čitanje u trenutačnom prozoru. Na primjer, IRC primljene poruke, dostupni
  poslužitelji, itd.
*	kontrol+NVDA+f: Ako se kursor nalazi u polju za uređivanje koje je samo za
  čitanje, otvara se dijalog za pretragu s NVDA naredbama za traženje
  teksta.
*	kontrol+šift+l: Premješta navigacijski objekt i miša na zaglavlja
  trenutačnog popisa.
*	kontrol+šift+q: Šita prvi objekt u statusnoj traci; pruža informacije o
  nedavnoj aktivnosti.
*	kontrol+šift+w: Čita drugi objekt statusne trake; sadrži informacije o
  datotekama i korisnicima na trenutačnom poslužitelju.
*	kontrol+šift+e: Čita treći objekt statusne trake; korisno, kad se želi
  doznati brzina slanja/preuzimanja.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Upravljanje stupcima. ##

Kad se nalaziš unutar popisa, možeš premještati kursor između stupaca i
redaka pomoću alt+control+strelice. U ovom dodatku su dostupni i slijedeći
prečaci:

*	nvda+kontrol+1-0: Čita prvih deset stupaca.
*	nvda+šift+1-0: Čita jedamaesti do dvadeseti stupac.
*	nvda+šift+C: Kopira sadržaj zadnje pročitanog stupca u međuspremnik.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Promjene u verziji 7.0
* Kompatibilno s NVDA 2023.1.

## Promjene u verziji 6.0
*	Zahtijeva NVDA 2022.1 ili noviju verziju.

## Promjene u verziji 5.0
*	Kompatibilno s NVDA 2021.1.

## Promjene u verziji 4.0 ##
*	Zahtijeva NVDA 2019.3 ili noviju verziju.

## Promjene u verziji 2.0 ##
*	 Za traženje teksta u poljima koja su samo za čitanje, moguće je koristiti
   dijaloški okvir pretrage, kao što je „nvda+kontrol+f”, za aktiviranje
   dijaloga pretrage.

## Promjene u verziji 2.0 ##
*	 Pomoć za dodatak je dostupna unutar upravljača dodataka.

## Promjene u verziji 1.2 ##
*	 Prilikom premještanja na IRC poruke, označeni se tekst čita ispravno.
*	 Tipkovnički prečac za prijelaz na popis rezultata pretraživanja je sada
   poopćen, kako bi se fokus mogao premjestiti na bilo koji dostupni popis u
   trenutačnom prozoru.
*	 Prečac koji se koristi za fokusiranje IRC poruka je sada poopćen, kako bi
   se omogućilo premještanje na bilo koje polje za uređivanje koje je samo
   za čitanje, čime se omogućuje pregled informacija o povezivosti u prozoru
   Poslužitelji.
*	 Prilikom premještanja miša ili fokusa na alatnu traku, u nekim se
   slučajevima ovo izgovaralo dvaput. To je sada ispravljeno.

## Promjene u verziji 1.1 ##
*	 Ispravljena greška u e mule stavci izbornika unutar  NVDA izbornika
   pomoć, kada korisnička mapa konfiguracije sadrži nelatinične znakove.
*	 Prečace je sada moguće prenamijeniti, koristeći dijaloški okvir ulazne
   geste u NVDA izborniku.

## Promjene u verziji1.0 ##
*	 Prva verzija.



[[!tag dev stable]]

[1]: https://www.emule-project.net
