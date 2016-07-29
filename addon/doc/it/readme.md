# eMule #

*	Autori: Noelia, Chris, Alberto.
*	download [stable version][1]
*	download [development version][3]

Questo componente aggiuntivo migliora l'accessibilità di Emule con
NVDA. Contiene alcuni tasti rapidi per spostarsi all'interno delle varie
schede e fornisce informazioni utili su Emule.

Deriva dal componente aggiuntivo eMuleNVDASupport, sviluppato dalla stessa
autrice. è necessario disinstallare la vecchia versione, se presente, prima
di installare questa versione.

Testato su [eMule][2] 0.50a.

## Comandi rapidi: ##

*	control+shift+h: sposta il focus e il mouse sulla barra degli strumenti
  principale.
*	control+shift+t: Legge la finestra corrente.
*	Control+Shift+n: Sposta il focus sul campo Nome nella finestra Trova .
*	Control+shift+p: Nella finestra di ricerca , sposta il focus e il mouse
  nell'elenco dei parametri di ricerca 
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	control+NVDA+f: If the caret is located in a read only edit box, opens a
  find dialog to use the commands for searching text available in NVDA.
*	control+shift+l: Sposta il Navigatore ad Oggetti e il puntatore Mouse
  sull'intestazione di una colonna all'interno di un elenco.
*	control+shift+q: Legge attività recenti, primo elemento della barra di
  stato:
*	control+shift+w: Legge utenti e files, secondo elemento della barra di
  stato:
*	control+shift+e: Legge velocità di Download e Upload in eMule, terzo
  elemento della barra di stato:
*	control+shift+r: Legge connettività alle reti eD2K e Kad, quarto elemento
  della barra di stato:

## Esplorazione degli elenchi: ##

Negli elenchi di eMule è possibile navigare tra le colonne e le righe usando
alt+control+ frecce direzionali. In questo componente aggiuntivo sono
disponibili inoltre i seguenti comandi da tastiera:

*	nvda+control+1-0: Consente di leggere le prime 10 colonne.
*	nvda+shift+1-0: Consente di leggere le colonne corrispondenti, dalla
  undicesima alla ventesima.
*	nvda+shift+C: Copia negli appunti il contenuto dell'ultima colonna letta.

## Changes for 3.0 ##
*	 To search text in readonly edit boxes, now we can use the dialog and
   commands available in NVDA.

## Cambiamenti per la 2.0 ##
*	 L'aiuto sul componente aggiuntivo è disponibile dalla gestione
   componenti.

## Cambiamenti nella 1.2 ##
*	 When moving to the IRC messages, the selected text is reported properly.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.
*	 When moving mouse and focus to the toolbar, in some cases it was
   announced twice. This has been fixed.

## Cambiamenti per la 1.1 ##
*	 Fixed bug in eMule item under NVDA's help menu, when the user config
   folder name contains non latin characters.
*	 I tasti rapidi possono essere riassegnati utilizzando la finestra di
   dialogo gesti di immissione di NVDA.

## Changes for 1.0 ##
*	 Initial version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
