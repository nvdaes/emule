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

## Tastenkürzel: ##

*	strg+Umschaltt+h: verschiebt den Fokus und die Maus auf die
  Hauptsymbolleiste.
*	Steuerung+Umschalt+t: ließt das aktuelle Fenster.
*	strg+Umschalt+n: Verschiebt den Fokus in das Feld "name" im Suchfenster
*	strg+Umschalt+p: Bewegt den Fokus im Suchfenster in die Liste der
  Suchparameter
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	strg+NVDA+f: Wenn sich der Systemcursor in einem schreibgeschützten
  Eingabefeld befindet, wird ein Suchfeld geöffnet.
*	strg+f3: sucht nach dem nächsten Vorkommen des Textes, den Sie mit
  nvda+strg+f gesucht haben.
*	strg+Umschalt+f3: sucht nach dem vorigen Vorkommen des Textes, den Sie mit
  nvda+strg+f gesucht haben.
*	Steuerung+Umschalt+l: bewegt den Navigator und die Maus zur Überschrift
  der aktuellen Liste.
*	strg+Umschalt+q: Zeigt das erste Objekt in der Statuszeile (die letzten
  Aktivitäten) an
*	strg+umschalt+w: zeigt das zweite Objekt auf der Statuszeile an (Dateien
  und Nutzer auf dem aktuellen Server)
*	strg+umschalt+e: zeigt das dritte Objekt der Statuszeile an (die
  Datenübertragungsraten)
*	strg+Umschalt+r: Zeigt das vierte Element der Statuszeile an
  (Informationen zu Verbindungen mit ed2k- und Kademia-Netzwerken)

## Spalten verwalten. ##

Wenn sich der Fokus in einer Liste befindet, können Sie strg+alt+Pfeiltasten
verwenden, um sich zwischen den Zeilen und Spalten zu bewegen. Golgende
Befehle sind außerdem verfügbar:

*	NVDA+Steuerung+1-0: Ließt die ersten 10 Spalten.
*	NVDA+Umschalt+1-0: Ließt die Spalten 11 bis 20.
*	NVDA+Umschalt+c: kopiert die Inhalte der zuletzt gesprochenen Spalte in
  die Zwischenablage.

## Änderungen bis 2.0 ##
*	 Die Hilfe zur Erweiterung ist über den Erweiterungs-Manager verfügbar.

## Änderungen bis 1.2 ##
*	 Wenn Sie sich zu den IRC-Nachrichten bewegen, wird ausgewählter Text
   vorgelesen.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.
*	 When moving mouse and focus to the toolbar, in some cases it was
   announced twice. This has been fixed.

## Änderungen bis 1.1 ##
*	 Fehler im Eintrag Emule im NVDA-Hilfe-Menü behoben, wenn der Namen des
   Benutzerverzeichnises nicht-lateinische Zeichen enthällt.
*	 Tastenkombinationen können nun mittels des Dialogs Eingaben neu
   zugewiesen werden.

## Änderungen bis 1.0 ##
*	 Ehrstveröffentlichung.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
