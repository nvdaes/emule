# eMule #

*	Autori: Noelia, Chris, Alberto.

Questo componente aggiuntivo migliora l'accessibilità di Emule con
NVDA. Contiene alcuni tasti rapidi per spostarsi all'interno delle varie
schede e fornisce informazioni utili su Emule.

Deriva dal componente aggiuntivo eMuleNVDASupport, sviluppato dalla stessa
autrice. E' necessario disinstallare la vecchia versione, se presente, prima
di installare questa versione.

Tested on [eMule][1] 0.50a and 70b.

## Comandi rapidi: ##

*	control+shift+h: sposta il focus e il mouse sulla barra degli strumenti
  principale.
*	control+shift+t: Legge la finestra corrente.
*	control+Shift+n: Sposta il focus sul campo Nome nella finestra Trova .
*	control+shift+p: Nella finestra di ricerca , sposta il focus e il mouse
  nell'elenco dei parametri di ricerca.
*	control+shift+b: sposta il focus sull'elenco nella finestra corrente. Per
  esempio, si sposta sui risultati nella finestra Cerca o nell'elenco dei
  download nella finestra Trasferimenti.
*	control+shift+o: sposta il focus nel campo editazione di sola lettura
  nella finestra corrente. Per esempio, si sposta nei messaggi ricevuti
  nella finestra IRC, etc.
*	control+NVDA+f: Se il cursore si trova in un campo editazione di sola
  lettura, apre la finestra di dialogo per la ricerca di testo di NVDA.
*	control+shift+l: Sposta il Navigatore ad Oggetti e il puntatore Mouse
  sull'intestazione di una colonna all'interno di un elenco.
*	control+shift+q: Legge attività recenti, primo elemento della barra di
  stato.
*	control+shift+w: Legge utenti e files del server attuale, secondo elemento
  della barra di stato.
*	control+shift+e: Legge velocità di Download e Upload in eMule, terzo
  elemento della barra di stato.
*	control+shift+r: Reads The fourth object of the status bar; reports on
  connecting of eD2K and Kad network.
*	Not assigned: Toggles the usage of an alternative approach to read
  sliders.

## Esplorazione degli elenchi. ##

Negli elenchi di eMule è possibile navigare tra le colonne e le righe usando
alt+control+ frecce direzionali. In questo componente aggiuntivo sono
disponibili inoltre i seguenti comandi da tastiera:

*	nvda+control+1-0: Consente di leggere le prime 10 colonne.
*	nvda+shift+1-0: Consente di leggere le colonne corrispondenti, dalla
  undicesima alla ventesima.
*	nvda+shift+C: Copia negli appunti il contenuto dell'ultima colonna letta.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Changes for 7.0
* Compatible with NVDA 2023.1.

## Changes for 6.0
*	Requires NVDA 2022.1 or later.

## Changes for 5.0
*	Compatible with NVDA 2021.1.

## Novità nella versione 4.0 ##
*	Richiede NVDA 2019.3 o superiore.

## Novità nella versione 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Novità nella versione 2.0 ##
*	 L'aiuto sul componente aggiuntivo è disponibile dal gestore componenti
   aggiuntivi.

## Novità nella versione 1.2 ##
*	 Quando ci si sposta sui messaggi IRC , il testo selezionato viene
   riportato correttamente.
*	 Il comando rapido  utilizzato per spostarsi alla lista dei risultati di
   Ricerca è stato generalizzato per essere in grado di spostare il focus in
   qualsiasi elenco nella finestra corrente.
*	 Il comando utilizzato per focalizzare i messaggi IRC è stato
   generalizzato per spostare il focus su qualsiasi campo editazione di sola
   lettura, il che rende possibile rivedere le informazioni di connessione
   nella finestra Server.
*	 Spostando il mouse e il focus sulla barra degli strumenti, in alcuni casi
   si aveva una doppia vocalizzazione. Questo problema è stato risolto.

## Novità nella versione 1.1 ##
*	 Risolto un problema nella voce Emule del menu Aiuto di NVDA, che si
   verificava quando il nome della cartella di configurazione utente
   conteneva caratteri non latini.
*	 I tasti rapidi possono ora essere riassegnati utilizzando la finestra di
   dialogo gesti e tasti di immissione di NVDA.

## Novità nella versione 1.0 ##
*	 Versione iniziale.



[[!tag dev stable]]

[1]: https://www.emule-project.net
