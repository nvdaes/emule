# eMule #

*	Készítők: Noelia, Chris, Alberto.
*	Letöltés [stabil verzió][1]
*	Letöltés [fejlesztői verzió][3]

Ez a kiegészítő hatékonyabb hozzáférést biztosít az eMule programhoz.

A bővítmény az eMuleNVDASupport kiegészítőre épül, melyet szintén a jelen
kiegészítő fejlesztője készített. Használat előtt kérjük távolítsa el a
régebbi kiegészítőt.

Tesztelve az [eMule][2] 0.50a programmal.

## Billentyűparancsok: ##

*	control+shift+h: az egérkurzort és a fókuszt a fő eszköztárhoz helyezi.
*	control+shift+t: felolvassa az aktuális ablakot.
*	control+shift+n: a fókuszt a keresőablak Név mezőjére helyezi.
*	control+shift+p: a fókuszt a keresőablak paraméterlistájához, vagy a
  szerkesztőmező beállításaihoz helyezi.
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	control+NVDA+f: Ha a kurzor egy csak olvasható szerkesztőmezőn áll,
  megnyit egy keresőablakot.
*	control+f3: A csak olvasható szerkesztőmezőkben megkezdett keresés
  következő előfordulására lép.
*	control+shift+f3: A csak olvasható szerkesztőmezőkben megkezdett keresés
  előző előfordulására lép.
*	control+shift+l: A navigátor- és az egérkurzort az aktuális lista
  fejlécéhez helyezi.
*	control+shift+q: felolvassa az első elemet az állapotsoron, mely a
  legutóbbi tevékenységről tájékoztat.
*	control+shift+w: felolvassa a második elemet az állapotsoron, mely a
  jelenlegi kiszolgáló fájlokkal és felhasználókkal kapcsolatos információit
  tartalmazza.
*	control+shift+e: felolvassa a harmadik elemet az állapotsoron, mely a le-
  és feltöltési sebességet tartalmazza.
*	control+shift+r: felolvassa a negyedik elemet az állapotsoron, mely az
  eD2K és Kad hálózatok kapcsolódási állapotát tartalmazza.

## Oszlopok kezelése. ##

Egy oszlopokat tartalmazó listában általában az alt+control+nyíl billentyűk
használhatóak sor és oszlop navigációhoz. Ebben a kiegészítőben a következő
parancsok is elérhetőek:

*	nvda+control+1-0: felolvassa az első 10 oszlopot.
*	nvda+shift+1-0: Felolvassa a 11-től 20-ig található oszlopokat.
*	nvda+shift+C: az utoljára felolvasott oszlop tartalmát a vágólapra
  másolja.

## Az 1.2 verzió változásai ##
*	 Amikor az IRC üzeneteken navigálunk, a kijelölt szöveg felolvasásra
   kerül.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.

## Az 1.1 verzió változásai ##
*	 Javítva az Emule elem a súgó menüben, hiba történt ha a felhasználói
   konfigurációs fájl nem latin karaktereket tartalmazott.
*	 A billentyűparancsok átállíthatóak a beviteli parancsok párbeszédablakán.

## Az 1.0 verzió változásai ##
*	 Az első kiadás.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev

