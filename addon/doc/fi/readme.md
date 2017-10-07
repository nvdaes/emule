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
*	Control+Shift+B: Siirtää kohdistuksen nykyisessä ikkunassa olevaan
  listaan. Käyttökelpoinen esimerkiksi Haku-ikkunassa, Siirrot-ikkunan
  Lataukset-listassa jne.
*	Control+Shift+O: Siirtää kohdistuksen nykyisen ikkunan vain luku
  -muokkausruutuihin. Esimerkiksi vastaanotettuihin IRC-viesteihin,
  käytettävissä olevien palvelimien listaan jne.
*	Control+NVDA+F: Avaa etsintävalintaikkunan, jos kohdistin on vain luku
  -tyyppisessä muokkausruudussa.
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

## Muutokset versiossa 3.0 ##
*	 NVDA:ssa käytettävissä olevaa valintaikkunaa ja komentoja on nyt
   mahdollista käyttää tekstin etsimiseen vain luku -tyyppisistä
   muokkausruuduista.

## Muutokset versiossa 2.0 ##
*	 Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 1.2 ##
*	 Valittu teksti luetaan oikein IRC-viesteihin siirryttäessä.
*	 Hakutuloslistaan siirtävä näppäinkomento on yleistetty siirtämään
   kohdistus mihin tahansa käytettävissä olevaan listaan nykyisessä
   ikkunassa.
*	 IRC-viesteihin siirtävä näppäinkomento on yleistetty siirtämään mihin
   tahansa vain luku -muokkausruutuun, mikä mahdollistaa yhteyden tietojen
   tarkastelemisen Palvelimet-ikkunassa.
*	 Kun hiiri ja kohdistus siirrettiin työkalupalkkiin, se luettiin joissakin
   tapauksissa kahdesti. Tämä on korjattu.

## Muutokset versiossa 1.1 ##
*	 Korjattu NVDA:n ohjevalikossa olevan eMule-valikkokohteen vika, jossa
   käyttäjän asetuskansio sisältää muita kuin latinalaisia merkkejä.
*	 Pikanäppäinten uudelleenmäärittely on nyt mahdollista NVDA:n
   syötekomentojen valintaikkunaa käyttäen.

## Muutokset versiossa 1.0 ##
*	 Ensimmäinen versio.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
