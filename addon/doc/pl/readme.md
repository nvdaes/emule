# eMule 0.50A #

*	Autorzy: Noelia, Chris, Alberto.
*	Pobierz [wersja stabilna][1]
*	Pobierz [wersja rozwojowa][3]

Ten dodatek poprawia dostępność programu eMule w NVDA.  Dostarcza
dodatkowych klawiszy skrótów przemieszczających do różnych okien, oraz
prezentuje użyteczne informacje o Emule.

Bazuje na dodatku eMuleNVDASupport, stworzonym przez tego samego
autora. Powinieneś odinstalować stary dodatek aby używać tego, ponieważ
obydwa mają wspólne klawisze skrótu i funkcje.

Przetestowany na [eMule][2] 0.50a.

## Skróty klawiszowe: ##

*	control+shift+h: przenosi mysz i punkt uwagi do głównego paska narzędzi.
*	control+shift+t: odczytuje bieżące okno.
*	control+shift+n: przenosi punkt uwagi do pola nazwy w oknie znajdowania.
*	control+shift+p: w oknie wyszukiwania, przenosi mysz i punkt uwagi do
  listy parametrów, albo opcji pola edycji.
*	control+shift+b: przenosi punkt uwagi do listy wyników w oknie
  wyszukiwania.
*	control+shift+z: przenosi punkt uwagi i mysz do kontekstowego paska
  narzędzi. Mozesz wyjść z paska narzędzi przy pomocy klawisza Tab.
*	control+shift+o: przenosi punkt uwagi do okna otrzymanych wiadomości IRC.
*	control+NVDA+f: jeśli kursor systemowy znajduje się w polu edycji tylko do
  odczytu, otwiera okno Znajdź.
*	control+f3: znajduje następne wystąpienie tekstu ostatnio wyszukiwanego w
  polach edycji tylko do odczytu.
*	control+shift+f3: znajduje poprzednie wystąpienie tekstu ostatnio
  wyszukiwanego w polach edycji tylko do odczytu.
*	control+shift+l: przenosi obiekt nawigatora i wskaźnik myszy do nagłówków
  aktualnej listy.
*	control+shift+q: odczytuje pierwszy obiekt na pasku stanu; dostarcza
  informację o ostatniej aktywności.
*	control+shift+w: odczytuje drugi obiekt na pasku stanu; zawiera informacje
  o plikach i użytkownikach na aktualnym serwerze.
*	control+shift+e: odczytuje trzeci obiekt na pasku stanu; użyteczne aby
  poznać prędkość pobierania i wysyłania.
*	control+shift+r: odczytuje czwarty obiekt na pasku stanu; raport z
  połączenia z siecią eD2K i Kad.
*	NVDA+control+shift+h: otwiera dokumentację. jeśli nie jest dostępna w
  twoim języku, otwiera dokumentację w języku angielskim.

## Zarządzanie kolumnami. ##

Kiedy znajdujesz się na liście, możesz przemieszczać kursor pomiędzy liniami
i kolumnami używając klawisza alt+control+ Strzałki.  Dostępne są również
następujące polecenia klawiszowe w tym dodatku:

*	nvda+control+1-0: czyta pierwsze 10 kolumn.
*	nvda+shift+1-0: czyta kolumny do 20.
*	nvda+shift+C: kopiuje do schowka treść ostatnio przeczytanej kolumny.

## Zmiany dla 1.1 ##
*	 Poprawiony błąd polecenia Emule w menu Pomoc NVDA, gdy nazwa folderu
   konfiguracyjnego użytkownika zawierała znaki z poza alfabetu łacińskiego.
*	 Skróty klawiszowe mogą być modyfikowane przy użyciu okna Zdarzeń wejścia
   w menu NVDA.

## Zmiany dla 1.0 ##
*	 Pierwsza wersja.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
