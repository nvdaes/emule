# eMule #

*	Tekijät: Noelia, Chris, Alberto.

Tämä lisäosa parantaa eMulen saavutettavuutta NVDA:lla käytettäessä.
Lisäksi se tarjoaa lisänäppäinkomentoja eMulen eri ikkunoissa liikkumiseen
sekä antaa hyödyllistä tietoa ohjelmasta.

Perustuu saman tekijän kehittämään eMuleNVDASupport-lisäosaan. Sinun tulisi
poistaa se tämän version käyttämiseksi, sillä molemmissa on yhteisiä
näppäinkomentoja ja ominaisuuksia.

Testattu [eMulen][1] versioissa 0.50a ja 70b.

## Näppäinkomennot: ##

*	Ctrl+Vaihto+H: Siirtää kohdistuksen ja hiiren päätyökaluriville.
*	Ctrl+Vaihto+T: Lukee nykyisen ikkunan.
*	Ctrl+Vaihto+N: Siirtää kohdistuksen Haku-ikkunan Nimi-kenttään.
*	Ctrl+Vaihto+P: Siirtää kohdistuksen ja hiiren Haku-ikkunassa
  hakuparametrien listaan tai eri vaihtoehtojen muokkauskenttiin.
*	Ctrl+Vaihto+B: Siirtää kohdistuksen nykyisessä ikkunassa olevaan
  listaan. Käyttökelpoinen esimerkiksi Haku-ikkunassa, Siirrot-ikkunan
  Lataukset-listassa jne.
*	Ctrl+Vaihto+O: Siirtää kohdistuksen nykyisen ikkunan vain luku
  -muokkausruutuihin. Esimerkiksi vastaanotettuihin IRC-viesteihin,
  käytettävissä olevien palvelimien listaan jne.
*	Ctrl+NVDA+F: Avaa etsintävalintaikkunan, jos kohdistin on vain luku
  -tyyppisessä muokkausruudussa.
*	Ctrl+Vaihto+L: Siirtää navigointiobjektin ja hiiren nykyisen listan
  otsikoihin.
*	Ctrl+Vaihto+Q: Lukee tilarivillä ensimmäisenä olevan objektin, joka antaa
  tietoja viimeaikaisesta toiminnasta.
*	Ctrl+Vaihto+W: Lukee tilarivillä toisena olevan objektin, joka sisältää
  tietoja nykyisellä palvelimella olevista tiedostoista ja käyttäjistä.
*	Ctrl+Vaihto+E: Lukee tilarivillä kolmantena olevan objektin, joka sisältää
  lähetys- ja latausnopeudet.
*	Ctrl+Vaihto+R: Lukee tilarivillä neljäntenä olevan objektin, jossa on
  tietoa eD2K- ja Kad-verkkojen yhteyden tilasta.
*	Ei määritetty: Ottaa käyttöön vaihtoehtoisen liukusäädinten lukutavan tai
  poistaa sen käytöstä.

## Sarakkeiden hallinta ##

Kohdistinta voidaan siirtää rivien ja sarakkeiden välillä listassa oltaessa
Alt+Ctrl+nuolinäppäimiä käyttäen.  Tässä lisäosassa ovat käytettävissä
lisäksi seuraavat näppäinkomennot:

*	NVDA+Ctrl+1-0: Lukee ensimmäiset 10 saraketta.
*	NVDA+Vaihto+1-0: Lukee sarakkeet väliltä 11-20.
*	NVDA+Vaihto+C: Kopioi viimeksi luetun sarakkeen sisällön leikepöydälle.


## Muutokset versiossa 20.0.0
* Osa muokkauskentistä ja liukusäätimistä on nimetty Alberto Buffolinon
  kehittämää
  [labelAutofinderCore-projektia](https://github.com/ABuffEr/labelAutofinderCore)
  hyödyntäen.
* Lisätty määrittämätön komento vaihtoehtoisen liukusäädinten lukutavan
  käyttöön ottamista tai käytöstä poistamista varten (oletuksena pois
  käytöstä).

## Muutokset versiossa 7.0
* Yhteensopiva NVDA 2023.1:n kanssa.

## Muutokset versiossa 6.0
*	Edellyttää NVDA 2022.1:tä tai uudempaa.

## Muutokset versiossa 5.0
*	Yhteensopiva NVDA 2021.1:n kanssa.

## Muutokset versiossa 4.0 ##
*	Edellyttää NVDA 2019.3:a tai uudempaa.

## Muutokset versiossa 3.0 ##
*	 Etsi tekstiä vain luku -tyyppisistä muokkausruuduista NVDA:n
   Etsi-valintaikkunaa, NVDA+Ctrl+F, käyttäen.

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
   Näppäinkomennot-valintaikkunaa käyttäen.

## Muutokset versiossa 1.0 ##
*	 Ensimmäinen versio.



[[!tag dev stable]]

[1]: https://www.emule-project.net
