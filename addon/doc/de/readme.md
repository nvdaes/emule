# eMule #
[[!meta title="eMule 0.50A"]]
[[!meta title="eMule 0.50A"]]

*	Authoren: Noelia, Chris, Alberto.
*	[stabile Version herunterladen][1]
*	[Testversion herunterladen][1]

Diese Erweiterung verbessert die Zugänglichkeit von Emule mit NVDA.  NVDA
stellt außerdem Tastenkombinationen zum Navigieren in verschiedene Fenster
von Emule zur Verfügung. 

Diese Erweiterung basiert auf EmuleNVDASupport. Sie sollten EmuleNVDASupport
deinstallieren, bevor Sie diese Erweiterung verwenden. Ursache hierfür sind
Überschneidungen bei der Verwendung von Tastenkombinationen und Funktionen
bei beiden Erweiterungen.

Getestet mit [eMule][2] 0.50a.

## Tastenbefehle: ##

*	Strg+Umschaltt+H: Verschiebt den Fokus und die Maus auf die
  Hauptsymbolleiste.
*	Strg+Umschalt+T: Liest das aktuelle Fenster aus.
*	Strg+Umschalt+N: Verschiebt den Fokus in das Feld "Name" im Suchfenster.
*	Strg+Umschalt+P: Bewegt den Fokus im Suchfenster in die Liste der
  Suchparameter.
*	Strg+Umschalt+B: Bewegt den Fokus in die Liste im aktuellen Fenster. Zum
  Beispiel verwendbar im Suchfenster, Downloads in Übertragungsfenster, etc.
*	Strg+Umschalt+O: Bewegt den Fokus zum schreibgeschützten Feld, im
  aktuellen Fenster. Zum Beispiel die empfangenen Nachrichten im IRC,
  verfügbare Server, etc.
*	Strg+NVDA+F: Wenn sich der Systemcursor in einem schreibgeschützten
  Eingabefeld befindet, wird ein Suchfeld geöffnet.
*	Strg+Umschalt+L: Bewegt den Navigator und die Maus zur Überschrift der
  aktuellen Liste.
*	Strg+Umschalt+Q: Zeigt das erste Element in der Statuszeile (die letzten
  Aktivitäten) an.
*	Strg+Umschalt+W: Zeigt das zweite Element auf der Statuszeile an (Dateien
  und Nutzer auf dem aktuellen Server).
*	Strg+Umschalt+E: Zeigt das dritte Element der Statuszeile an (die
  Datenübertragungsraten).
*	Strg+Umschalt+R: Zeigt das vierte Element der Statuszeile an
  (Informationen zu Verbindungen mit ed2k- und Kademia-Netzwerken).

## Spalten verwalten. ##

Wenn sich der Fokus in einer Liste befindet, können Sie sich mit
Strg+Alt+Pfeiltasten zwischen den Zeilen und Spalten bewegen. Folgende
Befehle sind außerdem verfügbar:

*	NVDA+Strg+1-0: Liest die ersten 10 Spalten.
*	NVDA+Umschalt+1-0: Liest die Spalten 11 bis 20.
*	NVDA+Umschalt+C: Kopiert die Inhalte der zuletzt gesprochenen Spalte in
  die Zwischenablage.

## Änderungen bis 3.0 ##
*	 Mit den NVDA-Befehlen können Sie jetzt auch die Suchergebnisse auslesen.

## Änderungen bis 2.0 ##
*	 Die Hilfe zur Erweiterung ist über die Erweiterungsverwaltung verfügbar.

## Änderungen bis 1.2 ##
*	 Wenn Sie sich zu den IRC-Nachrichten bewegen, wird ausgewählter Text
   vorgelesen.
*	 Mit der Tastenkombination können Sie mittlerweile anstatt nur die
   Suchergebnisse auch sämtliche Listen im aktuellen Fenster ansteuern.
*	 Der Befehl wurde zuvor generell zum Fokussieren der IRC-Nachrichten
   verwendet. Mittlerweile können Sie jetzt auch damit im Fenster der
   Verbindungen zu den Servern auslesen.
*	 Beim Bewegen der Maus und dem Fokus zur Werkzeugleiste wurde unter
   Umständen die Aktion doppelt angesagt. Dies ist nun behoben worden.

## Änderungen bis 1.1 ##
*	 Fehler im Eintrag Emule im NVDA-Hilfemenü behoben, wenn der Namen des
   Benutzerverzeichnises nicht-lateinische Zeichen enthiellt.
*	 Tastenkombinationen können nun mittels des Dialogs Eingaben neu
   zugewiesen werden.

## Änderungen bis 1.0 ##
*	 Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
