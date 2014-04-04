# eMule #

*	Tekijät: Noelia, Chris, Alberto.
*	Lataa [vakaa versio][1]
*	Lataa [kehitysversio][3]

Tämä lisäosa auttaa parantamaan eMulen saavutettavuutta NVDA:lla
käytettäessä.  Lisäksi se tarjoaa lisänäppäinkomentoja eri ikkunoissa
liikkumiseen sekä antaa hyödyllistä tietoa eMulesta.

Perustuu saman tekijän kehittämään eMuleNVDASupport-lisäosaan. Sinun tulisi
poistaa se tämän version käyttämiseksi, sillä molemmissa on yhteisiä
näppäinkomentoja ja ominaisuuksia.

Testattu [eMule][2]n 0.50a-versiossa.

## Näppäinkomennot: ##

*	Control+Shift+H: Siirtää kohdistuksen ja hiiren päätyökaluriville.
*	Control+Shift+T: Lukee nykyisen ikkunan.
*	Control+Shift+N: Siirtää kohdistuksen Haku-ikkunan Nimi-kenttään.
*	Control+Shift+P: Siirtää kohdistuksen ja hiiren Haku-ikkunassa
  hakuparametrien listaan tai eri vaihtoehtojen muokkauskenttiin.
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	Control+NVDA+F: Avaa etsintävalintaikkunan, mikäli kohdistin on vain luku
  -muokkausruudussa.
*	Control+F3: Etsii vain luku -muokkausruuduista aiemmin etsityn tekstin
  seuraavan esiintymän.
*	Control+Shift+F3: Etsii vain luku -muokkausruuduista aiemmin etsityn
  tekstin edellisen esiintymän.
*	Control+Shift+L: Siirtää navigointiobjektin ja hiiren nykyisen listan
  otsikoihin.
*	Control+Shift+Q: Lukee tilarivillä ensimmäisenä olevan objektin, joka
  antaa tietoja viimeaikaisesta toiminnasta.
*	Control+Shift+W: Lukee tilarivillä toisena olevan objektin, joka sisältää
  tietoja nykyisellä palvelimella olevista tiedostoista ja käyttäjistä.
*	Control+Shift+E: Lukee tilarivillä kolmantena olevan objektin, joka
  sisältää lähetys- ja latausnopeudet.
*	Control+Shift+R: Lukee tilarivillä neljäntenä olevan objektin, jossa on
  tietoa eD2K- ja Kad-verkkojen yhteyden tilasta.

## Sarakkeiden hallinta ##

Kohdistinta voidaan siirtää rivien ja sarakkeiden välillä listassa oltaessa
Alt+Ctrl+nuolinäppäimiä käyttäen.  Tässä lisäosassa ovat käytettävissä
lisäksi seuraavat näppäinkomennot:

*	NVDA+Control+1-0: Lukee ensimmäiset 10 saraketta.
*	NVDA+Shift+1-0: Lukee sarakkeet väliltä 11-20.
*	NVDA+Shift+C: Kopioi viimeksi luetun sarakkeen sisällön leikepöydälle.

## Muutokset versiossa 1.2 ##
*	 Valittu teksti luetaan oikein IRC-viesteihin siirryttäessä.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.

## Muutokset versiossa 1.1 ##
*	 Korjattu NVDA:n ohjevalikossa olevan eMule-valikkokohteen vika, jossa
   käyttäjän asetuskansio sisältää muita kuin latinalaisia merkkejä.
*	 Pikanäppäinten uudelleenmäärittely on nyt mahdollista NVDA:n
   syöte-eleiden valintaikkunaa käyttäen.

## Muutokset versiossa 1.0 ##
*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev

