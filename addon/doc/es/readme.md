# eMule #

*	Autores: Noelia, Chris, Alberto.
*	descarga [versión estable][1]
*	Descargar [versión de desarrollo][3]

Este complemento te ayuda a mejorar la accesibilidad de eMule con
NVDA. También proporciona comandos de teclado adicionales para moverse en
diferentes ventanas y da información útil de eMule.

Se basa en el complemento eMuleNVDASupport, desarrollado por el mismo
autor. Debes desinstalar el viejo complemento para usar este, ya que ambos
tienen los mismos atajos de teclado y características.

Probado en [eMule] [2] 0.50A.

## Órdenes de teclado: ##

*	control+shift+h: mueve el foco y el ratón a la barra de herramientas
  principal.
*	control+shift+t: lee la ventana actual.
*	control+shift+n: Mueve el foco al campo nombre en la ventana de Búsqueda.
*	control+shift+p: En la ventana de Búsqueda, mueve el foco y el ratón a la
  lista de parámetros de búscqueda, o al campo de edición de opciones .
*	control+shift+b: Move the focus to the list in the current window. For
  example usable in the Search window, downloads in Transfer window, etc.
*	control+shift+o: Move the focus to read-only edit boxes in the current
  window. For example the IRC received messages, available Servers, etc.
*	control+NVDA+f: Si el cursor se pone en un cuadro de edición de sólo
  lectura, abre un diálogo de búsqueda.
*	control+f3: Encuentra la siguiente aparición del texto que hayas buscado
  previamente en cuadros de edición de sólo lectura.
*	control+shift+f3: Busca la anterior aparición del texto que hayas buscado
  previamente en cuadros de edición de sólo lectura.
*	control+shift+l: Mueve el navegador de objetos y el ratón a los
  encabezados de la lista actual.
*	control+shift+q: Lee el primer objeto en la barra de estado; proporciona
  información acerca de la actividad reciente.
*	control+shift+w: Lee el segundo objeto de la barra de estado; contiene
  información acerca de ficheros y usuarios en el servidor actual.
*	control+shift+e: Lee el tercer objeto de la barra de estado; útil para
  saber la velocidad de subida y bajada.
*	control+shift+r: Lee el cuarto objeto de la barra de estado; informa sobre
  la conexión de las redes Kad y eD2K.

## Administrando columnas. ##

Cuando estés dentro de una lista, puedes mover el cursor  entre las filas y
las columnas utilizando alt+control+Flechas.  En este complemento también
están disponibles las siguientes órdenes de teclado:

*	NVDA+control+1-0: Lee las primeras 10 columnas.
*	NVDA+shift+1-0: Lee las columnas 11 a 20.
*	NVDA+shift+C: Copia el contenido de la última columna leída al
  portapapeles.

## Cambios para 1.2 ##
*	 Al moverse a los mensajes del IRC, el texto seleccionado se anuncia
   apropiadamente.
*	 The keystroke used for moving to the Search results list has been
   generalized to be able to move focus to any available list in the current
   window.
*	 The command used to focus the IRC messages has been generalized to move
   to any read-only edit box, making it possible to review connection
   information in the Servers window.

## Cambios para 1.1 ##
*	 Solucionado un problema en el elemento eMule en el menú Ayuda de NVDA,
   cuando el nombre de la carpeta de configuración de usuario contiene
   caracteres no latinos.
*	 Los atajos ahora pueden reasignarse utilizando el diálogo gestos de
   entrada de NVDA.

## Cambios para 1.0 ##
*	 Versión inicial.

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=em

[2]: http://www.emule-project.net

[3]: http://addons.nvda-project.org/files/get.php?file=em-dev

