# eMule #

*	Autori: Noelia, Chris, Alberto.
*	preuzmite [Stabilnu inačicu][1]
*	preuzmite [razvojnu inačicu][3]

Ovaj dodatak unaprjeđuje pristupačnostof eMule programa uz pomoć nVDA.
također osigurava dodatne tipkovničke prečace za premještanje po različitim
prozorima i daje korisne informacije u eMuleu.

Ovaj je dodatak baziran na dodatku eMuleNVDASupport, kojeg je razvio isti
autor. Trebali biste ukloniti taj stari dodatak kako biste mogli koristiti
ovaj dodatak, zbog toga što oba dodatka imaju zajedničke tipkovničke prečace
i značajke.

testirano na [eMule][2] 0.50a.

## Tipkovnički Prečaci: ##

*	control+shift+h: Premješta fokus i miš na glavnu alatnu traku.
*	control+shift+t: Čita trenutni prozor.
*	control+shift+n: premješta fokus na polje za upisivanje imena u prozoru
  pretrage.
*	control+shift+p: u prozoru traži, premješta fokus i miš na popis
  parametara pretrage, i opcija uređivačkog polja.
*	control+shift+b: Premješta fokus na popis u trenutnom prozoru. na primjer,
  korisno u prozoru pretrage, preuzimanja u prozoru transferi, itd.
*	control+shift+o: premjesti fokus na polja za uređivanje koja su samo za
  čitanje u trenutnom prozoru. Na primjer, irc primljene poruke, dostupni
  poslužitelji, itd.
*	control+NVDA+f: ako se kursor nalazi u polju za uređivanje koje je samo za
  čitanje, otvara se dijalog za pretragu.
*	control+shift+l: premješta objekt navigacije i miš na zaglavlja trenutnog
  popisa.
*	control+shift+q: čita prvi objekt u statusnoj traci; daje informaciju o
  nedavnoj aktivnosti.
*	control+shift+w: čita drugi objekt statusne trake; sadrži informacije o
  datotekama i korisnicima na trenutnom poslužitelju.
*	control+shift+e: čita treći objekt statusne trake; korisno kada se želi
  doznati upload/DownLoad brzina.
*	control+shift+r: čita četvrtu objekt statusne trake; izvještava o
  povezivosti ed2k i Kad mreže.

## upravljanje stupcima. ##

Kad se nalazite unutar popisa, možete premještavati kursor između stupaca i
redaka koristeći alt+control+ strelice.  u ovom dodatku slijedeće su prečice
također dostupne:

*	nvda+control+1-0: čita prvih deset redaka.
*	nvda+shift+1-0: čita od 11 do 20 retka.
*	nvda+shift+C: kopira sadržaj zadnje pročitanog stupca u međuspremnik.

## Promjene u inačici 2.0 ##
*	 Za pretraživanje teksta u poljima koja su samo za čitanje, sada možete
   koristiti dijaloški okvir i NVDA komande.

## promjene u inačici 2.0 ##
*	 Pomoč za dodatak dostupna je unutar upravitelja dodataka.

## promjene u inačici 1.2 ##
*	 Kada se premještate po porukama IRC, označeni se tekst čita ispravno.
*	 Tipkovnički prečac za rezultate pretraživanja sada je poopćen kako bi se
   fokus mogao pomicati do bilo kojeg dostupnog popisa u trenutnom prozoru.
*	 Prečac koji se koristi za fokusiranje IRC porukka sada je poopćen kako
   biste se mogli premještati na bilo koje polje za uređivanje koje je samo
   za čitanje, što vam omogućuje pregled informacija o povezivosti u prozoru
   poslužitelji.
*	 Kad pomičete fokus ili miš na alatnu traku, u nekim slučajevima je ovo
   bilo izgovoreno dvaput. ovo je sada ispravljeno.

## promjene u inačici 1.1 ##
*	 Ispravljena greška u e mule stavci izbornika unutar  NVDA izbornika
   pomoć, kada korisnička mapa konfiguracije sadrži nelatinične znakove.
*	 Prečaci se sada mogu mjenjati koristeći dijaloški okvir ulazne geste u
   nvda izborniku.

## promjene u inačici1.0 ##
*	 prva inačica.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
