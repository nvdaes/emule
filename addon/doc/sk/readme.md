# eMule #

*	Autori: Noelia, Chris, Alberto.

Tento doplnok zlepšuje prístupnosť programu eMule s NVDA. Poskytuje užitočné
klávesové skratky a informácie z okien a prostredia Emule.

Je postavený na staršom aplikačnom module pre eMule od toho istého
autora. odporúčame vám starý aplikačný modul odstrániť, keďže majú spoločné
klávesové skratky a funkcie.

Tested on [eMule][1] 0.50a and 70b.

## klávesové skratky: ##

*	ctrl+shift+h: Presunie myš a fokus do hlavného panela nástrojov.
*	ctrl+shift+t: prečíta aktuálne okno.
*	ctrl+shift+n: Presunie fokus do poľa názov v okne hľadania.
*	ctrl+shift+p: Presunie fokus na zoznam parametrov alebo do editačného poľa
  s možnosťami v okne hľadania.
*	ctrl+shift+b: Presunie fokus do zoznamu v aktuálnom okne. Funguje
  napríklad v okne hľadania, v okne so sťahovaním a podobne.
*	ctrl+shift+o: Presunie kurzor do editačného poľa iba na čítanie. Napríklad
  do okna s IRC správami, dostupnými servermi a podobne.
*	ctrl+NVDA+f: Ak ste v editačnom poli iba na čítanie, otvorí štandardné
  okno hľadania, ktoré poznáte z NVDA.
*	ctrl+shift+l: presunie navigačný objekt a myš na hlavičku pre aktuálny
  zoznam.
*	ctrl+shift+q: Prečíta prvý objekt na stavovom riadku; informáciu o
  poslednej aktivite.
*	ctrl+shift+w: Prečíta druhý objekt na stavovom riadku; informácie o
  súboroch a používateľoch na aktuálnom serveri.
*	ctrl+shift+e: prečíta tretí objekt na stavovom riadku; rýchlosť sťahovania
  a posielania.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## práca so stĺpcami. ##

Na pohyb po riadkoch a stĺpcoch v zozname môžete použiť ctrl+alt+šípky. V
doplnku sú dostupné aj tieto skratky:

*	nvda+ctrl+1-0: Prečíta prvých 10 stĺpcov.
*	nvda+shift+1-0: Číta stĺpce 11-20.
*	nvda+shift+C: Skopíruje posledný prečítaný stĺpec do schránky.


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

## Zmeny vo verzii 4.0 ##
*	Vyžaduje NVDA od verzie 2019.3.

## Zmeny vo verzii 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Zmeny vo verzii 2.0 ##
*	 Návod k doplnku nájdete v správcovi doplnkov.

## Zmeny vo verzii 1.2 ##
*	 Pri pohybe v IRC správach je správne oznamovaný vybratý text.
*	 Skratka na prechod do výsledkov hľadania bola upravená tak, že prechádza
   do akého koľvek zoznamu v aktuálnom okne.
*	 Skratka na prechod k správam IRC bola upravená tak, že prechádza do
   ľubovolného editačného poľa, takže je možné čítať informácie o spojení v
   okne servera.
*	 NVDA viac opakovane nečíta obsah panela nástrojov, ak naň presuniete
   fokus alebo myš.

## Zmeny vo verzii 1.1 ##
*	 opravená chyba v pomocníkovy Emule, ktorá sa objavovala, ak názov
   priečinka s používateľskými dátami obsahoval iné ako ascii znaky.
*	 Skratky sa dajú meniť v dialógu klávesové skratky.

## Zmeny vo verzii 1.0 ##
*	 prvé vydanie.



[[!tag dev stable]]

[1]: https://www.emule-project.net
