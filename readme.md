# eMule #

*	Authors: Noelia, Chris, Alberto.

This add-on helps to improve accessibility of eMule with nVDA.
It also provides additional keyboard commands for moving in different windows and gives Useful information about eMule.

It's based on the eMuleNVDASupport add-on, developed by the same author. You should uninstall that old add-on to use this one, since both have common keystrokes and features.

Tested on [eMule][1] 0.50a and 70b.

## Key Commands: ##

*	control+shift+h: Moves focus and mouse to main toolbar.
*	control+shift+t: Reads the current window.
*	control+shift+n: Moves the focus to the Name field in the Find window.
*	control+shift+p: In the Search window, moves focus and mouse to the list of search parameters, or edit field options.
*	control+shift+b: Move the focus to the list in the current window. For example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current window. For example the IRC received messages, available Servers, etc.
*	control+NVDA+f: If the caret is located in a read only edit box, opens a find dialog to use the commands for searching text available in NVDA.
*	control+shift+l: Moves the navigator object and mouse to the headers of the current list.
*	control+shift+q: Reads the first object in the status bar; provides information about recent activity.
*	control+shift+w: Reads the second object of the status bar; contains information about files and users on the current server.
*	control+shift+e: Reads the third object of the status bar; useful to know the UpLoad/DownLoad speed.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Managing columns. ##

When within a list, you can move the caret between the rows and columns using alt+control+ Arrows.
In this Add-on the following key commands are also available:

*	nvda+control+1-0: Reads the first 10 columns.
*	nvda+shift+1-0: Reads columns 11 to 20.
*	nvda+shift+C: Copies the contents of the last read column to the clipboard.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the [labelAutofinderCore project](https://github.com/ABuffEr/labelAutofinderCore) developed by Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an alternative approach to read sliders (off by default).

## Changes for 7.0
* Compatible with NVDA 2023.1.

## Changes for 6.0
*	Requires NVDA 2022.1 or later.

## Changes for 5.0
*	Compatible with NVDA 2021.1.

## Changes for 4.0 ##
*	Requires NVDA 2019.3 or later.

## Changes for 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used, such as nvda+control+f to activate the find dialog.

## Changes for 2.0 ##
*	 Add-on help is available from the Add-ons Manager.

## Changes for 1.2 ##
*	 When moving to the IRC messages, the selected text is reported properly.
*	 The keystroke used for moving to the Search results list has been generalized to be able to move focus to any available list in the current window.
*	 The command used to focus the IRC messages has been generalized to move to any read-only edit box, making it possible to review connection information in the Servers window.
*	 When moving mouse and focus to the toolbar, in some cases it was announced twice. This has been fixed.

## Changes for 1.1 ##
*	 Fixed bug in eMule item under NVDA's help menu, when the user config folder name contains non latin characters.
*	 Shortcuts can now be reassigned using the NVDA gesture input dialog.

## Changes for 1.0 ##
*	 Initial version.

[1]: http://www.emule-project.net
