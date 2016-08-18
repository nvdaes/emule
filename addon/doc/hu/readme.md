# eMule #

*	Készítők: Noelia, Chris, Alberto.
*	Letöltés [stabil verzió][1]
*	Letöltés [fejlesztői verzió][3]

Ez a kiegészítő hatékonyabb hozzáférést biztosít az eMule
programhoz. Billenytyűparancsokat ad a különböző ablakokban való
navigáláshoz, és hasznos információkat tesz elérhetővé az eMule programban.

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
*	control+shift+b: a fókuszt az aktuális ablakban elérhető listára
  helyezi. Ez hasznos a keresési ablakban, a letöltéseknél az átvitel
  ablakban, stb.
*	control+shift+o: A fókuszt az aktuális ablakban elérhető csak olvasható
  szerkesztőmezőre helyezi. Például IRC fogadott üzenetek, elérhető
  szerverek, stb.
*	control+NVDA+f: Ha a kurzor egy csak olvasható szerkesztőmezőn áll,
  megnyit egy keresőablakot.
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

## A 3.0 verzió változásai ##
*	 A csak olvasható szerkesztőmezőkben az NVDA-ban elérhető
   billentyűparancsokkal kereshetünk.

## Az 2.0 verzió változásai ##
*	 A kiegészítő súgója elérhető a Bővitménykezelő párbeszédablakából is.

## Az 1.2 verzió változásai ##
*	 Amikor az IRC üzeneteken navigálunk, a kijelölt szöveg felolvasásra
   kerül.
*	 A billentyűparancs, amely eddig a fókuszt csak a keresési találatok
   listájára helyezte, most már bármilyen, az aktuális ablakban elérhető
   listára át tudja helyezni azt.
*	 A parancs, ami eddig csak az IRC üzenetekre helyezte át a fókuszt,
   immáron bármely más csak olvasható szerkesztőmezőre is át tudja helyezni
   azt, ezáltal lehetővé vált a kapcsolódási információk áttekintése a
   szerverek ablakában.
*	 Amikor az egér és a fókusz az eszköztárra került, némely esetben az
   információ kétszer került kimondásra. A hiba kijavításra került.

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
