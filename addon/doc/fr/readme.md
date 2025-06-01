# eMule #

*	Autheurs : Noelia, Chris, Alberto.

Cette extension permet d'améliorer l'accessibilité d'eMule avec NVDA. Elle
fournit également des commandes clavier supplémentaires pour se déplacer
sous différentes fenêtres et donne des informations utiles sur eMule.

Elle est basée sur l'extension eMuleNVDASupport, développé par le même
auteur. Vous devez désinstaller cette ancienne extension pour utiliser
celle-ci, car les deux ont des touches et des fonctionnalités communes.

Testé avec [eMule][1] 0.50a.

## Touches de raccourcis : ##

*	control+maj+h : amène la souris et le focus sur la barre d'outils
  principale.
*	control+maj+t : Lit la fenêtre en cours.
*	control+maj+n : Déplace le focus sur le champ Nom de la fenêtre
  Rechercher.
*	control+maj+p : Dans la fenêtre de recherche, déplace le focus et la
  souris à la liste des paramètres de recherche, ou modifie les options des
  champs.
*	control+maj+b : Déplace le focus à la liste des résultats dans la fenêtre
  de recherche. Utilisable par exemple dans la fenêtre de recherche, les
  Transferts de téléchargements, etc.
*	Ctrl + Maj + o : Déplace le focus aux zones d'édition en lecture seule
  dans la fenêtre courante. Par exemple, les messages IRC reçus, Serveurs
  disponibles, etc.
*	contrôle + NVDA + f : Si le curseur est situé dans une zone d'édition en
  lecture seule, ouvre un dialogue de Recherche afin d'utiliser les
  commandes pour la recherche de texte disponible dans NVDA.
*	Ctrl + Maj + L : Déplace l'objet de navigation et la souris aux en-têtes
  de la liste actuelle.
*	Ctrl + Maj + Q : Lit le premier objet dans la barre d'état, fournit des
  informations sur l'activité récente.
*	Ctrl + Maj + W : Lit le second objet de la barre d'état, contient des
  informations sur les fichiers et les utilisateurs sur le serveur actuel.
*	Ctrl + Maj + E: Lit le troisième objet de la barre d'état; utile pour
  connaître la vitesse d'Envoi / Téléchargement.
*	Ctrl + Maj + r: Affiche Le quatrième objet de la barre d'état, les
  rapports sur la connexion de réseau eD2K et Kad.

## Gestion des colonnes. ##

Lorsque vous êtes dans une liste, vous pouvez déplacer le curseur entre les
lignes et les colonnes en utilisant Alt + Ctrl + Flèches. Dans ce module les
touches de raccourci suivantes sont également disponibles :

*	NVDA + control +1-0 : Lit les 10 premières colonnes.
*	NVDA + maj +1-0 : Lit colonnes 11 à 20.
*	NVDA + Maj + C : Copie le contenu de la dernière colonne lue dans le
  presse-papiers.

## Changements pour la version 7.0
* Compatible avec NVDA 2023.1.

## Changements pour la version 6.0
*	Nécessite NVDA 2022.1 ou version ultérieure.

## Changements pour la version 5.0
*	Compatible avec NVDA 2021.1.

## Changements pour la version 4.0 ##
*	Nécessite NVDA 2019.3 ou version ultérieure.

## Changements pour la version 3.0 ##
*	 Pour rechercher du texte dans les zones d'édition en lecture seule, le
   dialogue Rechercher peut être utilisée, tel comme nvda+control+f pour
   activer le dialogue Rechercher.

## Changements pour la version 2.0 ##
*	 L'aide de l'extension est disponible à partir du Gestionnaire
   d'Extensions.

## Changements pour la version 1.2 ##
*	 Lors du déplacement aux messages IRC, le texte sélectionné est indiqué
   correctement.
*	 La combinaison de touches utilisée pour le déplacement à la liste de
   résultats de recherche a été généralisée pour pouvoir déplacer le focus à
   toutes les listes disponibles dans la fenêtre courante.
*	 La commande utilisée pour mettre en focus les messages IRC a été
   généralisée pour se déplacer sur toutes les zones d'édition en lecture
   seule, ce qui permet de consulter les informations de connexion dans la
   fenêtre des serveurs.
*	 Lors du déplacement de la souris et le focus à la barre d'outils, dans
   certains cas, il a été annoncé deux fois. Ce problème a été corrigé.

## Changements pour la version 1.1 ##
*	 Correction d'un bug dans l'élément eMule sous le menu d'aide de NVDA,
   lorsque le nom du dossier configuration utilisateur contient des
   caractères non latins.
*	 Les raccourcis peuvent maintenant être réaffectés à l'aide du dialogue
   gestes de commande NVDA.

## Changements pour la version 1.0 ##
*	 Première version.

[[!tag dev stable]]

[1]: https://www.emule-project.net
