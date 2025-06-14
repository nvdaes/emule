# eMule #

*	Forfattere: Noelia, Chris, Alberto.

Dette tilføjelsesprogram hjælper med at forbedre tilgængeligheden til eMule
med NVDA. Det igver også ekstra tastaturkommandoer til at flytte rundt i
forskellige vinduer, samt giver nyttig information om eMule.

Programmet er baseret på tilføjelsesprogrammet eMuleNVDASupport, som er
udviklet af samme forfatter. Du skal afinstallere det gamle
tilføjelsesprogram for at kunne bruge denne version, da de har kommandoer og
funktioner til fælles.

Tested on [eMule][1] 0.50a and 70b.

## Tastaturkommandoer ##

*	Control+Shift+h: Flytter fokus og mus til hovedværktøjslinjen.
*	Control+Shift+t: Læser det aktuelle vindue.
*	Control+Shift+n: Flytter fokus til navnefeltet i søgevinduet.
*	Control+Shift+p: I søgevinduet: Flytter fokus og mus til listen over
  søgeparametre ellerredigering af feltindstillinger.
*	Control+Shift+b: Flyt fokus til listen i det aktuelle vindue, brugbart
  f.eks. i søgevinduet eller til downloads i overførselsvinduet.
*	Control+Shift+o: Flyt fokus til skrivebeskyttede editfelter i det aktuelle
  vindue, f.eks. "IRC received messages", "available Servers" osv.
*	Control+NVDA+f: Åbner en søgedialog, hvis markøren er placeret i et
  skrivebeskyttet editfelt.
*	Control+Shift+l: Flytter navigatorobjektet og musen til overskrifterne på
  den aktuelle liste.
*	Control+Shift+q: Læser første objekt på statuslinjen; Giver information om
  seneste aktivitet.
*	Control+Shift+w: Læser det andet objekt på statuslinjen; Indeholder
  oplysning om filer og brugere på den aktuelle server.
*	Control+Shift+e: Læser tredje objekt på statuslinjen;
  Upload/download-hastighed.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Styring af kolonner. ##

I en liste kan du flytte markøren rundt i rækker og kolonner med
Alt+Control+piletaster. I dette tilføjelsesprogram kan du også bruge
følgende tastaturkommandoer:

*	NVDA+Control+1-0: Læser de første 10 kolonner.
*	NVDA+Shift+1-0: Læser kolonne 11-20.
*	NVDA+Shift+c: Kopierer indholdet i den sidst læste kolonne til
  udklipsholderen.


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

## Ændringer i4.0 ##
*	Kræver NVDA 2019.3 eller nyere.

## Ændringer i 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Ændringer i 2.0 ##
*	 Hjælp til tilføjelsesprogrammet er til rådighed fra styring af
   tilføjelsesprogrammer.

## Ændringer i 1.2 ##
*	 Når man flytter til IRC-meddelelserne, bliver den valgte tekst annonceret
   rigtigt.
*	 Det tastetryk, som bruges til at gå til listen over søgeresultater, er
   blevet generaliseret, så man kan flytte til en hvilken som helst liste i
   det aktuelle vindue.
*	 Den kommando, som bruges til at bringe fokus til irc-meddelelserne, er
   blevet generaliseret til at gå til et hvilket som helst skrivebeskyttet
   editfelt. På den måde kan man læse forbindelsesoplysningerne i
   servervinduet.
*	 Når man flytter mus og fokus til værktøjslinjen, blev denne i nogle
   tilfælde annonceret to gange. Dette er blevet løst.

## Ændringer i 1.1 ##
*	 Rettet fejl i emnet eMule under NVDAs hjælpemenu, når navnet på mappen
   med NVDAs brugerkonfigurationer indeholder ikke-latinske tegn.
*	 Genvejstaster kan nu ændres i NVDAs dialog til inputbevægelser.

## Ændringer i 1.0 ##
*	 Første version.



[[!tag dev stable]]

[1]: https://www.emule-project.net
