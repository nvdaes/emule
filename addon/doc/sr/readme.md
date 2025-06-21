# eMule #

*	Autori: Noelia, Chris, Alberto.

This add-on helps to improve accessibility of eMule with nVDA.  It also
provides additional keyboard commands for moving in different windows and
gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You
should uninstall that old add-on to use this one, since both have common
keystrokes and features.

Tested on [eMule][1] 0.50a and 70b.

## Glavne prečice ##

*	control+shift+h: Pomera fokus i miš na glavnu traku.
*	control+shift+t: Čita trenutni prozor.
*	control+shift+n: Premešta fokus na polje za unos imena u dijalogu za
  pretragu.
*	control+shift+p: U prozoru za pretragu, premešta fokus na listu
  podešavanja pretrage, ili opcije polja za uređivanje.
*	control+shift+b: Premešta fokus na listu u trenutnom prozoru. Na primer
  korisno u prozoru za pretragu, Preuzimanjima u prozoru za prebacivanje, i
  tako dalje.
*	control+shift+o: Premešta fokus na polja koja su samo za čitanje u
  trenutnom prozoru. Na primer IRC primljene poruke, dostupni serveri, i
  tako dalje.
*	control+NVDA+f: Ako je kursor u polju koje je samo za čitanje, otvara
  dijalog za pretragu kako biste koristili NVDA komande.
*	control+shift+l: Pomera miš i navigacioni objekat na zaglavlje trenutne
  liste.
*	control+shift+q: Čita prvi objekat na statusnoj traci; pruža informacije o
  poslednjim aktivnostima.
*	control+shift+w: Čita drugi objekat statusne trake; sadrži informacije o
  datotekama i korisnicima na trenutnom serveru.
*	control+shift+e: Čita treći objekat statusne trake; korisno kako biste
  znali trenutnu brzinu odpremanja i preuzimanja.
*	control+shift+r: Reads The fourth object of the status bar; reports on
  connecting of eD2K and Kad network.
*	Not assigned: Toggles the usage of an alternative approach to read
  sliders.

## Upravljanje kolona ##

Kada ste u listi, možete pomerati kursor između kolona i redova koristeći
alt+control+ strelice.  U ovom dodatku sledeće komande su takođe dostupne:

*	nvda+control+1-0: čita prvih deset kolona.
*	nvda+shift+1-0: Čita kolone 11 do 20.
*	nvda+shift+C: Kopira sadržaj zadnje pročitane kolone u privremenu
  memoriju.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Changes for 7.0
* Compatible with NVDA 2023.1.

## Changes for 6.0
*	Requires NVDA 2022.1 or later.

## Changes for 5.0
*	Compatible with NVDA 2021.1.

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Promene u 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Promene u 2.0 ##
*	 Pomoć za dodatak je dostupna iz menia za upravljanje dodacima.

## Promene u 1.2 ##
*	 Kada ste u IRC porukama, izabran tekst je ispravno pročitan.
*	 Prečica za prelazak na rezultate pretrage sada prelazi na bilo koju listu
   u trenutnom prozoru.
*	 Komanda za čitanje IRC poruka sada prelazi na bilo koje polje koje je
   samo za čitanje, tako da možete pregledati informacije o konekciji u bilo
   kom prozoru.
*	 Kada premestite fokus i miš na traku sa alatkama, u nekim slučajevima
   bila je izgovorena dva puta. Ovo je popravljeno.

## Promene u 1.1 ##
*	 Popravljen bag u eMule stavci u NVDA Meniju za pomoć, kada folder za
   korisnička podešavanja sadrži znakove koji nisu latinični.
*	 Prečice sada mogu biti promenjene u NVDA dijalogu za ulazne gestove.

## Promene u 1.0 ##
*	 Prva verzija



[[!tag dev stable]]

[1]: https://www.emule-project.net
