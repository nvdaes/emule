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
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	control+NVDA+f: Ak ste v editačnom poli iba na čítanie, otvorí okno
  hľadania.
*	control+f3: Nájde najbližší výskyt hľadaného reťazca.
*	control+shift+f3: Nájde predchádzajúci výskyt hľadaného reťazca.
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

## Zmeny vo verzii 1.2 ##
*	 Pri pohybe v IRC správach je správne oznamovaný vybratý text.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.

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

