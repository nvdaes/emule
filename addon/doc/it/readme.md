# eMule 0.50A #

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
*	Control+shift+b: sposta il focus sull'elenco dei risultati nella finestra
  di ricerca.
*	control+shift+z: Sposta il puntatore Mouse e Focus alla barra dei menu
  della finestra principale, consentendo di spostarsi con TAB.
*	control+shift+o: Sposta il focus sulla finestra messaggi nella chat Irc.
*	control+NVDA+f: Se il cursore si trova in un campo editazione di sola
  lettura, apre una finestra di dialogo per la ricerca di testo.
*	control+f3: Se il cursore si trova in un campo editazione di sola lettura,
  trova il testo successivo alla posizione del cursore.
*	control+shift+f3: Se il cursore si trova in un campo editazione di sola
  lettura, trova il testo precedente alla posizione del cursore.
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
*	NVDA+control+shift+h: Apre la Documentazione, se non è disponibile per la
  lingua selezionata verrà visualizzata la guida in inglese.

## Esplorazione degli elenchi: ##

Negli elenchi di eMule è possibile navigare tra le colonne e le righe usando
alt+control+ frecce direzionali. In questo componente aggiuntivo sono
disponibili inoltre i seguenti comandi da tastiera:

*	nvda+control+1-0: Consente di leggere le prime 10 colonne.
*	nvda+shift+1-0: Consente di leggere le colonne corrispondenti, dalla
  undicesima alla ventesima.
*	nvda+shift+C: Copia negli appunti il contenuto dell'ultima colonna letta.

## Changes for 1.1 ##
*	 Fixed bug in eMule item under NVDA's help menu, when the user config
   folder name contains non latin characters.
*	 Shortcuts can now be reassigned using the NVDA gesture input dialog.

## Changes for 1.0 ##
*	 Initial version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev
