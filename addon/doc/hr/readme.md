# eMule #

*	Autori: Noelia, Chris, Alberto.
*	NVDA compatibility: 2019.3 or later.
*	Preuzmi [stabilnu verziju][1]
*	Preuzmi [razvojnu verziju][3]
*	download [version compatible with NVDA 2017.3][4]

This add-on helps to improve accessibility of eMule with nVDA.  It also
provides additional keyboard commands for moving in different windows and
gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You
should uninstall that old add-on to use this one, since both have common
keystrokes and features.

Testirano na [eMule][2] 0.50a.

## Tipkovnički prečaci: ##

*	control+shift+h: Premješta fokus i miša na glavnu alatnu traku.
*	control+shift+t: Čita trenutačni prozor.
*	control+shift+n: Premješta fokus na polje za ime u prozoru pretrage.
*	control+shift+p: U prozoru pretrage, premješta fokus i miša na popis
  parametara pretrage ili na opcije uređivačkog polja.
*	control+shift+b: Premješta fokus na popis u trenutačnom prozoru. Na
  primjer, korisno u prozoru pretrage, preuzimanja u prozoru transfera, itd.
*	control+shift+o: Premješta fokus na polja za uređivanje koja su samo za
  čitanje u trenutačnom prozoru. Na primjer, IRC primljene poruke, dostupni
  poslužitelji, itd.
*	control+NVDA+f: Ako se kursor nalazi u polju za uređivanje koje je samo za
  čitanje, otvara se dijalog za pretragu s NVDA naredbama za traženje
  teksta.
*	control+shift+l: Premješta navigacijski objekt i miša na zaglavlja
  trenutačnog popisa.
*	control+shift+q: Šita prvi objekt u statusnoj traci; pruža informacije o
  nedavnoj aktivnosti.
*	control+shift+w: Čita drugi objekt statusne trake; sadrži informacije o
  datotekama i korisnicima na trenutačnom poslužitelju.
*	control+shift+e: Čita treći objekt statusne trake; korisno, kad se želi
  doznati brzina slanja/preuzimanja.
*	control+shift+r: Čita četvrti objekt statusne trake; izvještava o
  povezivosti ed2k i Kad mreže.

## Upravljanje stupcima. ##

Kad se nalaziš unutar popisa, možeš premještati kursor između stupaca i
redaka pomoću alt+control+strelice. U ovom dodatku su dostupni i slijedeći
prečaci:

*	nvda+control+1-0: Čita prvih deset stupaca.
*	nvda+shift+1-0: Čita jedamaesti do dvadeseti stupac.
*	nvda+shift+C: Kopira sadržaj zadnje pročitanog stupca u međuspremnik.

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Promjene u verziji 2.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

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

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
