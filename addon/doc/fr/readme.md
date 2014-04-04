# eMule #

*	Autheurs : Noelia, Chris, Alberto.
*	Télécharger [version stable][1]
*	Télécharger  [version de développement][3]

Ce module complémentaire rend Emule plus accessible avec NVDA en ajoutant
des raccourcis clavier pour avoir des informations ou activer des fenêtre
particulières.

Basé sur le module eMuleNVDASupport du même autheur. Désinstallez d'abord
eMuleNVDASupport qui créerait des conflits de raccourcis clavier.

Testé avec [eMule][2] 0.50a.

## Touches de raccourcis : ##

*	control+maj+h: amaine la souris et le focus sur la barre d'outils
  principale.
*	control+maj+t: Lie la fenêtre en cours.
*	control+maj+n: Déplace le focus sur le champ Nom de la fenêtre Rechercher.
*	control+maj+p: Dans la fenêtre de recherche, déplace le focus et la souris
  à la liste des paramètres de recherche, ou modifie les options des champs.
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	contrôle + NVDA + f: Si le curseur est situé dans une zone d'édition en
  lecture seule, ouvre une boîte de dialogue de Recherche.
*	Contrôle + F3: Recherche l'occurrence suivante du texte que vous avez
  cherché auparavant dans la zone d'édition en lecture seule.
*	Contrôle + maj + F3: Recherche l'occurrence suivante du texte que vous
  avez cherché auparavant dans la zone d'édition en lecture seule.
*	Ctrl + Maj + L: Déplace l'objet de navigation et la souris aux les
  en-têtes de la liste actuelle.
*	Ctrl + Maj + Q: Lit le premier objet dans la barre d'état, fournit des
  informations sur l'activité récente.
*	Ctrl + Maj + W: Lit le second objet de la barre d'état, contient des
  informations sur les fichiers et les utilisateurs sur le serveur actuel.
*	Ctrl + Maj + E: Lit le troisième objet de la barre d'état; utile pour
  connaître la vitesse d'Upload / Download.
*	Ctrl + Maj + r: Affiche Le quatrième objet de la barre d'état, les
  rapports sur la connexion de réseau eD2K et Kad.

## Gestion des colonnes. ##

Lorsque vous êtes dans une liste, vous pouvez déplacer le curseur entre les
lignes et les colonnes en utilisant Alt + Ctrl + Flèches. Dans ce module les
touches de raccourci suivantes sont également disponibles :

*	NVDA + control +1-0: Lit les 10 premières colonnes.
*	NVDA + maj +1-0: Lit colonnes 11 à 20.
*	NVDA + Maj + C: Copie le contenu de la dernière colonne lue dans le
  presse-papiers.

## Changements pour la version 1.2 ##
*	 Lors du déplacement pour les messages IRC, le texte sélectionné est
   indiqué correctement.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.

## Changements pour la version 1.1 ##
*	 Correction d'un bug dans l'élément eMule sous le menu d'aide de NVDA,
   lorsque le nom du dossier configuration utilisateur contient des
   caractères non latins.
*	 Les raccourcis peuvent maintenant être réaffectées à l'aide de la boîte
   de dialogue gestes d'entrée NVDA.

## Changements pour la version 1.0 ##
*	 Première version.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev

