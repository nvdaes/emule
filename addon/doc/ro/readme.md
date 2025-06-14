# eMule #

*	Autori: Noelia, Chris, Alberto.

This add-on helps to improve accessibility of eMule with nVDA.  It also
provides additional keyboard commands for moving in different windows and
gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You
should uninstall that old add-on to use this one, since both have common
keystrokes and features.

Tested on [eMule][1] 0.50a and 70b.

## Comenzi de taste: ##

*	control+shift+h: Mută focalizarea și mausul la bara principală de unelte.
*	control+shift+t: Citește fereastra curentă.
*	control+shift+n: Mută focalizarea la câmpul Nume în fereastra de căutare.
*	control+shift+p: În fereastra de căutare, mută focalizarea și mausul la
  lista parametrilor de căutare sau la opțiunile câmpului de editare.
*	control+shift+b: Mutați focalizarea la lista din fereastra curentă. De
  exemplu, este utilizabil în fereastra de căutare, fereastra descărcărilor
  în transfer, etc.
*	control+shift+o: Mutați focalizarea pentru a citi doar casete de editare
  în fereastra curentă. De exemplu, Mesaje IRC primite, servere disponibile
  etc.
*	control+NVDA+f: Dacă caret-ul este localizat într-o casetă de editare doar
  citire, deschide un dialog găsit pentru a utiliza comenzile pentru
  căutarea de text disponibilă în NVDA.
*	control+shift+l: Mută obiectul navigator și mausul la antetele din lista
  curentă.
*	control+shift+q: Citește primul obiect în bara de stare; furnizează
  informații despre activitatea recentă.
*	control+shift+w: Citește al doilea obiect al barei de stare; conține
  informații despre fișiere și utilizatori pe serverul curent.
*	control+shift+e: Citește al treilea obiect al barei de stare; util pentru
  a ști viteza de încărcare/descărcare.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Gestionare coloane ##

Când vă aflați într-o listă, puteți muta caret-ul între rânduri și coloane
folosind alt+control+ săgeți.  În acest add-on, următoarele comenzi de taste
sunt de asemenea disponibile:

*	nvda+control+1-0: Citește primele 10 coloane.
*	nvda+shift+1-0: Citește coloanele de la 11 până la 20.
*	nvda+shift+C: Copiază conținutul ultimei coloane citite pe planșetă.


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

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Modificări aduse în versiunea 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Modificări aduse în versiunea 2.0 ##
*	 Ghidul add-on-ului este disponibil în managerul de add-on-uri.

## Modificări aduse în versiunea 1.2 ##
*	 Atunci când se deplasează la mesajele IRC, textul selectat este raportat
   în mod corespunzător.
*	 Combinațiile de taste utilizate pentru deplasarea la lista rezultatelor
   de căutare a fost generalizată să fie capabilă pentru deplasarea
   focalizării la orice listă disponibilă în fereastra curentă.
*	 Comanda folosită la focalizarea mesajelor IRC a fost generalizată pentru
   deplasarea la orice casetă de editare doar citire, ceea ce face posibilă
   revizuirea informațiilor de conectare în fereastra serverelor.
*	 Când deplasați mausul și focalizarea la bara principală de unelte, în
   unele cazuri era anunțat de două ori. Această eroare a fost reparată.

## Modificări aduse în versiunea 1.1 ##
*	 A fost reparată o eroare în elementul eMule din NVDA, meniul ajutor, când
   numele folderului user config conține caractere nelatine.
*	 Comenzile rapide pot fi reatribuite folosind dialogul gesturilor de
   intrare NVDA.

## Modificări aduse în versiunea 1.0 ##
*	 Versiunea inițială.



[[!tag dev stable]]

[1]: https://www.emule-project.net
