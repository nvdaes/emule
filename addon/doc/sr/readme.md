# eMule #

*	Autori: Noelia, Chris, Alberto.
*	Preuzmi[stabilnu verziju][1]
*	Preuzmi[verziju u razvoju][3]

Ovaj dodatak poboljšava pristupačnost programa eMule sa NVDA.  Takođe pruža
dodatne komande za premeštanje na različite prozore i dobijanje korisnih
informacija o eMule.

Baziran je na dodatku eMuleNVDASupport, programiran od strane istog
autora. Morate ukloniti taj dodatak kako biste koristili ovaj, zbog toga što
oba dodatka imaju slične karakteristike i prečice.

Testirano na [eMule][2] 0.50a.

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
*	control+shift+r: Čita četvrti objekat statusne trake; prijavjuje
  povezivanja na eD2K i Kad mrežu.

## Upravljanje kolona ##

Kada ste u listi, možete pomerati kursor između kolona i redova koristeći
alt+control+ strelice.  U ovom dodatku sledeće komande su takođe dostupne:

*	nvda+control+1-0: čita prvih deset kolona.
*	nvda+shift+1-0: Čita kolone 11 do 20.
*	nvda+shift+C: Kopira sadržaj zadnje pročitane kolone u privremenu
  memoriju.

## Promene u 3.0 ##
*	 Za pretragu teksta u poljima koja su samo za čitanje, sada možete
   koristiti NVDA komande

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

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
