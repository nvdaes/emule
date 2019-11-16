# eMule #

*	Autores: Noelia, Chris, Alberto.
*	NVDA compatibility: 2017.3 to 2019.2
*	baixar [versão estável] [1]
*	baixar [versão de desenvolvimento] [3]

Este extra ajuda a melhorar a acessibilidade do eMule com o nVDA. Também
fornece comandos de teclado adicionais para se mover em diferentes janelas e
fornece informações úteis do eMule.

Baseia-se no extra do eMuleNVDASupport, desenvolvido pelo mesmo autor. deve
desinstalar esse complemento antigo para usar este, uma vez que ambos
comandos e recursos comuns.

Testado no [eMule][2] 0.50a.

## Comandos: ##

*	control+shift+h: move o foco e o rato para a barra de ferramentas
  principal.
*	control+shift+t: lê a janela actual.
*	control+shift+n: move o foco para o campo Nome na janela Localizar.
*	control+shift+p: na janela Pesquisar, move o foco e o rato para a lista de
  parâmetros de pesquisa ou edita as opções de campo.
*	control+shift+b: move o foco para a lista na janela atual. Por exemplo,
  utilizável na janela de pesquisa, downloads na janela de transferência,
  etc.
*	control+shift+o: move o foco para caixas de edição somente leitura na
  janela actual. Por exemplo, o IRC recebeu mensagens, Servidores
  disponíveis, etc.
*	control+NVDA+f: se o cursor estiver localizado numa caixa de edição
  somente leitura, abre uma caixa de diálogo de pesquisa para usar os
  comandos para pesquisar texto disponível no NVDA.
*	control+shift+l: move o objecto do navegador e o rato para os cabeçalhos
  da lista actual.
*	control+shift+q: lê o primeiro objecto na barra de status; fornece
  informações sobre actividades recentes.
*	control+shift+w: lê o segundo objecto da barra de status; contém
  informações sobre ficheiros e utilizadores no servidor actual.
*	control+shift+e: lê o terceiro objecto da barra de status; útil para
  conhecer a velocidade de UpLoad / DownLoad.
*	control+shift+r: lê o quarto objecto da barra de status; relatórios sobre
  a conexão da rede eD2K e Kad.

## Gerir colunas: ##

Quando numa lista, pode mover o cursor entre as linhas e colunas usando alt
+ control + Setas. Neste extra, os seguintes comandos de teclas também estão
disponíveis:

*	Control+nvda+1-0: lê as 10 primeiras colunas.
*	nvda+shift+1-0: lê as colunas de 11 a 20.
*	nvda+shift+C: Copia o conteúdo da última coluna lida para a área de
  transferência.

## Alterações para 3.0 ##
*	 Para pesquisar texto em caixas de edição legíveis, agora podemos usar a
   caixa de diálogo e os comandos disponíveis no NVDA.

## Mudanças para 2.0 ##
*	 A ajuda adicional está disponível no Gestor de extras.

## Alterações para 1.2 ##
*	 Ao mudar para as mensagens do IRC, o texto seleccionado é lido
   corretamente.
*	 O comando de tecla usado para mover para a lista de resultados da
   Pesquisa foi generalizado para poder mover o foco para qualquer lista
   disponível na janela actual.
*	 O comando usado para focar as mensagens do IRC foi generalizado para
   mover para qualquer caixa de edição somente leitura, possibilitando a
   revisão de informações de conexão na janela de Servidores.
*	 Ao mover o rato e focar a barra de ferramentas, em alguns casos,  era
   anunciado duas vezes. esse aspecto foi corrigido.

## Alterações para 1.1 ##
*	 Foi corrigido um bug no item do eMule no menu de ajuda do NVDA, quando o
   nome da pasta de configuração do utilizador contém caracteres não
   latinos.
*	 Os atalhos agora podem ser reatribuídos usando a caixa de diálogo de
   entrada de comandos do NVDA.

## Alterações para 1.0 ##
*	 Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
