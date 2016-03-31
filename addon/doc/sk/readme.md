# eMule #

*	Autori: Noelia, Chris, Alberto.
*	Stiahnuť [stabilná verzia][1]
*	Stiahnuť [Vývojová verzia][3]

Tento doplnok zlepšuje prístupnosť programu eMule s NVDA. Poskytuje užitočné
klávesové skratky a informácie.

Je postavený na staršom aplikačnom module pre eMule od toho istého
autora. odporúčame vám starý aplikačný modul odstrániť, keďže majú spoločné
klávesové skratky.

Testované s [eMule][2] 0.50a.

## klávesové skratky: ##

*	control+shift+h: Presunie myš a fokus do hlavného panela nástrojov.
*	control+shift+t: prečíta aktuálne okno.
*	control+shift+n: Presunie fokus do poľa názov v okne hľadania.
*	control+shift+p: Presunie fokus na zoznam parametrov alebo do editačného
  poľa s možnosťami v okne hľadania.
*	control+shift+b: Presunie fokus do zoznamu v aktuálnom okne. Funguje
  napríklad v okne hľadania, v okne so sťahovaním a podobne.
*	control+shift+o: Presunie kurzor do editačného poľa iba na
  čítanie. Napríklad do okna s IRC správami, dostupnými servermi a podobne.
*	control+NVDA+f: If the caret is located in a read only edit box, opens a
  find dialog to use the commands for searching text available in NVDA.
*	control+shift+l: presunie navigačný objekt a myš na hlavičku pre aktuálny
  zoznam.
*	control+shift+q: Prečíta prvý objekt na stavovom riadku; informáciu o
  poslednej aktivite.
*	control+shift+w: Prečíta druhý objekt na stavovom riadku; informácie o
  súboroch a používateľoch na aktuálnom serveri.
*	control+shift+e: prečíta tretí objekt na stavovom riadku; rýchlosť
  sťahovania a posielania.
*	control+shift+r: prečíta štvrtý objekt na stavovom riadku; Oznámy stav
  pripájania do siete eD2K a Kad.

## práca so stĺpcami. ##

Na pohyb po riadkoch a stĺpcoch v zozname môžete použiť ctrl+alt+šípky. V
doplnku sú dostupné aj tieto skratky:

*	nvda+control+1-0: Prečíta prvých 10 stĺpcov.
*	nvda+shift+1-0: Číta stĺpce 11-20.
*	nvda+shift+C: Skopíruje posledný prečítaný stĺpec do schránky.

## Changes for 3.0 ##
*	 To search text in readonly edit boxes, now we can use the dialog and
   commands available in NVDA.

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

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
