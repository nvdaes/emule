# eMule #

*	Autores: Noelia, Chris, Alberto.

Este complemento axuda a mellorar a accesivilidade do eMule co nVDA.  Tamén
proporciona ordes de teclado adicionais para moverte en diferentes ventás e
dar información util do eMule.

Baséase no complemento eMuleNVDASupport, desenvolvido polo mesmo
autor. Debes desinstalar o vello complemento para usar este, xa que ambos
teñen as pulsacións de teclado e as características comúns.

Tested on [eMule][1] 0.50a and 70b.

## Ordes de Teclado: ##

*	control+shift+h: Move o foco e o rato cara a barra de ferramentas
  principal.
*	control+shift+t: Le a ventá actual.
*	control+shift+n: Move o foco cara o campo de nome na ventá procurar.
*	control+shift+p: Na ventá de procurar, move o foco e o rato cara a lista
  de parámetros de procuras, ou opcións do campo de edición.
*	control+shift+b: Move o foco para a lista na ventá actual. Por exemplo
  utilizable na ventá Buscar, descargas na ventá de transferencia, etc.
*	control+shift+o: Move o foco para caixas  de só lectura no diálogo
  actual. Por exemplo, as mensaxes recibidas no IRC , servidores
  dispoñibles, etc.
*	control+NVDA+f: se o cursor está localizado nunha Caixa de edición de só
  lectura, abre un diálogo de busca para usar as ordes para procurar texto
  disponibles no NVDA.
*	control+shift+l: Move o navegador de obxectos e o rato cara as cabeceiras
  da lista actual.
*	control+shift+q: Le o primeiro obxecto na barra de estado; proporciona
  información acerca da actividade recente.
*	control+shift+w: Le o segundo obxecto da barra de estado; contén
  información acerca de ficheiros e usuarios no servidor actual.
*	control+shift+e: Le o terceiro obxecto da barra de estado; util para saber
  a velocidade de subida e de baixada.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Administrando columnas. ##

Cando estás dentro dunha lista, podes mover o cursor entre as filas e as
columnas usando alt+control+Flechas.  Neste complemento tamén están
dispoñibles as seguintes ordes de teclado:

*	nvda+control+1-0: Le as primeiras 10 columnas.
*	nvda+shift+1-0: Le as columnas 11 a 20.
*	nvda+shift+C: Copia o contido da última columna lida ó portapapeis.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Cambios para 7.0
* Compatible con NVDA 2023.1.

## Cambios para 6.0
*	Require NVDA 2022.1 ou posterior.

## Cambios para 5.0
*	Compatible con NVDA 2021.1.

## Cambios para 4.0 ##
*	Require NVDA 2019.3 ou posterior.

## Cambios para 3.0 ##
*	 To search text in the readonly edit boxes,  the find dialog  can be used,
   such as nvda+control+f to activate the find dialog.

## Cambios para 2.0 ##
*	 A axuda do complemento está dispoñible no Administrador de Complementos.

## Cambios para 1.2 ##
*	 Cando se cambia para as mensaxes de IRC, o texto seleccionado indícase
   correctamente.
*	 A combinación de teclas usada para pasar á lista de resultados de busca
   foi xeneralizada para poder mover o foco para calquera lista dispoñible
   na ventá actual.
*	 A orde usada para concentrar as mensaxes de IRC foi xeneralizada para
   desprazarse a calquera caixa de edición de só lectura, o que fai posible
   revisar a información de conexión no diálogo de servidores.
*	 Ó mover o rato e o foco a barra de tarefas, nalgúns casos anunciábase
   dúas veces. Esto foi correxido.

## Cambios para 1.1 ##
*	 Correxido un erro no elemento eMule no menú de axuda do NVDA, cando o
   nome do cartafol da configuración de usuario contén caracteres non
   latinos.
*	 Os atallos agora poden se reasignar utilizando o diálogo de xestos de
   entrada do NVDA.

## Cambios para 1.0 ##
*	 Versión inicial.



[[!tag dev stable]]

[1]: https://www.emule-project.net
