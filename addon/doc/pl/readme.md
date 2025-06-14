# eMule #

*	Autorzy: Noelia, Chris, Alberto.

Ten dodatek pomaga poprawić dostępność eMule z nVDA.  Zawiera również
dodatkowe polecenia klawiaturowe do poruszania się w różnych oknach i daje
Przydatne informacje o eMule.

Opiera się na dodatku eMuleNVDASupport, opracowanym przez tego samego
autora. Powinieneś odinstalować ten stary dodatek, aby użyć tego, ponieważ
oba mają wspólne naciśnięcia i funkcje.

Tested on [eMule][1] 0.50a and 70b.

## Skróty klawiszowe: ##

*	control+shift+h: przenosi mysz i punkt uwagi do głównego paska narzędzi.
*	control+shift+t: odczytuje bieżące okno.
*	control+shift+n: przenosi punkt uwagi do pola nazwy w oknie znajdowania.
*	control+shift+p: w oknie wyszukiwania, przenosi mysz i punkt uwagi do
  listy parametrów, albo opcji pola edycji.
*	control+shift+b: przenosi punkt uwagi do listy w aktualnym
  oknie. Przydatne do listy wyników w oknie wyszukiwania, listy pobierań w
  oknie transfer itd.
*	control+shift+o: przenosi punkt uwagi do pól edycji tylko do odczytu,
  znajdujących się w aktualnym oknie, np. otrzymane wiadomości IRC, dostępne
  serwery itd.
*	control+NVDA+f: Jeśli karetka znajduje się w polu edycji tylko do odczytu,
  otwiera okno dialogowe znajdowania, aby użyć poleceń do wyszukiwania
  tekstu dostępnych w NVDA.
*	control+shift+l: przenosi obiekt nawigatora i wskaźnik myszy do nagłówków
  aktualnej listy.
*	control+shift+q: odczytuje pierwszy obiekt na pasku stanu; dostarcza
  informację o ostatniej aktywności.
*	control+shift+w: odczytuje drugi obiekt na pasku stanu; zawiera informacje
  o plikach i użytkownikach na aktualnym serwerze.
*	control+shift+e: odczytuje trzeci obiekt na pasku stanu; użyteczne aby
  poznać prędkość pobierania i wysyłania.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Zarządzanie kolumnami. ##

Kiedy znajdujesz się na liście, możesz przemieszczać kursor pomiędzy liniami
i kolumnami używając klawisza alt+control+ Strzałki.  Dostępne są również
następujące polecenia klawiszowe w tym dodatku:

*	nvda+control+1-0: czyta pierwsze 10 kolumn.
*	nvda+shift+1-0: czyta kolumny do 20.
*	nvda+shift+C: kopiuje do schowka treść ostatnio przeczytanej kolumny.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Zmiany w wersji 6.0
* Kompatybilny z NVDA 2023.1.

## Zmiany w wersji 6.0
*	Wymaga NVDA 2022.1 lub nowszego.

## Zmiany dla wersji 5.0
*	Kompatybilny z NVDA 2021.1.

## Zmiany dla wersji 4.0 ##
*	Wymaga NVDA w wersji 2019.3 lub nowszej.

## Zmiany dla 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Zmiany dla 2.0 ##
*	 Pomoc dodatku dostępna w oknie zarządzania dodatkami.

## Zmiany dla 1.2 ##
*	 Po przejściu do wiadomości IRC, zaznaczony tekst jest prawidłowo
   odczytywany.
*	 Komenda przechodzenia do wyników wyszukiwania została uogólniona i
   przenosi punkt uwagi do jakiejkolwiek pierwszej dostępnej listy w
   aktualnym oknie.
*	 Komenda przechodzenia do wiadomości IRC została uogólniona i  teraz
   umożliwia przejście do jakiegokolwiek pola tylko do odczytu  dzięki czemu
   można przeglądać informacje o połączeniach w oknie serwera.
*	 Po przemieszczeniu myszy lub punktu uwagi do paska narzędzi, w niektórych
   sytuacjach był oznajmiany podwójnie. Zostało to naprawione.

## Zmiany dla 1.1 ##
*	 Poprawiony błąd polecenia Emule w menu Pomoc NVDA, gdy nazwa folderu
   konfiguracyjnego użytkownika zawierała znaki z poza alfabetu łacińskiego.
*	 Skróty klawiszowe mogą być modyfikowane przy użyciu okna Zdarzeń wejścia
   w menu NVDA.

## Zmiany dla 1.0 ##
*	 Pierwsza wersja.



[[!tag dev stable]]

[1]: https://www.emule-project.net
