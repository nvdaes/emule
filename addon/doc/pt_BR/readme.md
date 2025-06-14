# eMule #

*	Autores: Noelia, Chris, Alberto.

Esse complemento ajuda a melhorar a acessibilidade do eMule com nVDA. Ele
também fornece comandos adicionais do teclado para mover-se em diferentes
janelas e fornece informações úteis sobre o eMule.

É baseado no complemento eMuleNVDASupport, desenvolvido pelo mesmo
autor. Você deve desinstalar esse complemento antigo para usá-lo, pois ambos
possuem pressionamentos de tecla e recursos comuns.

Tested on [eMule][1] 0.50a and 70b.

## Teclas de comando: ##

*	control+shift+h: Move foco e mouse para a barra de ferramentas principal.
*	control+shift+t: Lê a janela atual.
*	control+shift+n: Move o foco para o campo nome na janela pesquisar.
*	control+shift+p: Na janela pesquisar, move foco e mouse para a lista de
  parâmetros de pesquisa, ou opções do campo editar.
*	control+shift+b: Move o foco para a lista presente na janela atual, útil
  por exemplo na janela pesquisar, downloads na janela Transferir, etc.
*	control+shift+o: Move o foco para os campos de edição somente-leitura na
  janela atual, por exemplo as mensagens recebidas por IRC, servidores
  disponíveis, etc.
*	control+NVDA+f: Se o cursor estiver posicionado numa caixa de edição
  somente leitura, abre um diálogo de busca para uso dos comandos de busca
  de texto fornecidos pelo NVDA.
*	control+shift+l: Move objeto de navegação e mouse para os cabeçalhos da
  lista atual.
*	control+shift+q: Lê o primeiro objeto da barra de status; Fornece
  informações de atividades recentes.
*	control+shift+w: Lê o segundo objeto da barra de status; dá informações de
  arquivos e usuários no servidor atual.
*	control+shift+e: Lê o terceiro objeto da barra de status; útil para saber
  a velocidade de UpLoad/DownLoad.
*	control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
* Not assigned: Toggles the usage of an alternative approach to read sliders.

## Gerenciando colunas. ##

Quando estiver numa lista, pode mover o cursor pelas linhas e colunas usando
alt+control+ setas.  Neste complemento, estão também disponíveis as
seguintes teclas de comando:

*	nvda+control+1-0: Lê as primeiras 10 colunas.
*	nvda+shift+1-0: Lê as colunas de 11 a 20.
*	nvda+shift+C: Copia o conteúdo da última coluna lida para a área de
  transferência.


## Changes for 20.0.0
* Some edit boxes and sliders are labelled, thanks to the
  [labelAutofinderCore
  project](https://github.com/ABuffEr/labelAutofinderCore) developed by
  Alberto Buffolino, one of the authors of this add-on.
* A command (not assigned) has been added to toggle the usage of an
  alternative approach to read sliders (off by default).

## Mudanças na 7.0
* Compatível com o NVDA 2023.1.

## Mudanças na 6.0
*	Requer NVDA 2022.1 ou posterior.

## Mudanças na 5.0
*	Compatível com o NVDA 2021.1.

## Mudanças na 4.0 ##
*	Requer NVDA 2019.3 ou posterior.

## Mudanças na 3.0 ##
*	 Para pesquisar texto nas caixas de edição somente leitura, a caixa de
   diálogo localizar pode ser usada, como nvda+control+f para ativar a caixa
   de diálogo localizar.

## Mudanças na 2.0 ##
*	 A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.2 ##
*	 Ao mover-se para as mensagens de IRC, o texto selecionado é devidamente
   anunciado.
*	 A tecla de atalho usada para mover para a lista de resultados da busca
   foi generalizada para ser capaz de mover o foco para qualquer lista
   presente na janela atual.
*	 O comando usado para focalizar as mensagens de IRC foi generalizado para
   mover a qualquer campo de edição somente leitura, tornando-o capaz de
   explorar informações de conexão na janela de servidores.
*	 Ao mover o mouse e o foco para a barra de ferramentas, em alguns casos
   isso era anunciado duas vezes. Corrigido.

## Mudanças na 1.1 ##
*	 Corrigido erro no item eMule no menu de ajuda do NVDA quando o nome da
   pasta de opções do usuário contém caracteres não-latinos.
*	 Atalhos agora podem ser reatribuídos usando o diálogo de gestos para
   entrada do NVDA.

## Mudanças na 1.0 ##
*	 Versão inicial.



[[!tag dev stable]]

[1]: https://www.emule-project.net
