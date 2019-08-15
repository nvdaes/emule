# eMule #

*	Autores: Noelia, Chris, Alberto.
*	NVDA compatibility: 2017.3 to 2019.2
*	baixe a [versão estável][1]
*	baixe a [versão de desenvolvimento][3]

Este complemento serve para melhorar a acessibilidade do eMule com o
NVDA. Fornece também teclas adicionais de comando para mover-se nas
diferentes janelas e dá informações úteis do eMule.

É baseado no complemento eMuleNVDASupport, desenvolvido pelo mesmo
autor. Você deve desinstalar o antigo complemento para usar este aqui, visto
que ambos possuem recursos e teclas de atalho em comum.

Testado no [eMule][2] 0.50a.

## Teclas de comando: ##

*	control+shift+h: Moves foco e mouse para a barra de ferramentas principal.
*	control+shift+t: Lê a janela atual.
*	control+shift+n: Moves o foco para o campo nome na janela pesquisar.
*	control+shift+p: Na janela pesquisar, moves foco e mouse para a lista de
  parâmetros de pesquisa, ou opções do campo editar.
*	control+shift+b: Move o foco para a lista presente na janela atual, útil
  por exemplo na janela pesquisar.
*	control+shift+o: Move o foco para os campos de edição somente-leitura na
  janela atual, por exemplo as mensagens recebidas por IRC, servidores
  disponíveis, etc.
*	control+NVDA+f: Se o cursor estiver posicionado numa caixa de edição
  somente leitura, abre um diálogo de busca para uso dos comandos de busca
  de texto fornecidos pelo NVDA.
*	control+shift+l: Moves objeto de navegação e mouse para os cabeçalhos da
  lista atual.
*	control+shift+q: Lê o primeiro objeto da barra de status; Fornece
  informações de atividades recentes.
*	control+shift+w: Lê o segundo objeto da barra de status; dá informações de
  arquivos e usuários no servidor atual.
*	control+shift+e: Lê o terceiro objeto da barra de status; útil para saber
  a velocidade de Upload e DownLoad.
*	control+shift+r: Lê o quarto objeto da barra de status; anuncia como estão
  as conexões às redes eD2K e Kad.

## Mexer com colunas. ##

Quando estiver numa lista, pode mover o cursor pelas linhas e colunas usando
alt+control+ setas.  Neste complemento, estão também disponíveis as
seguintes teclas de comando:

*	nvda+control+1-0: Lê as primeiras 10 colunas.
*	nvda+shift+1-0: Lê as colunas de 11 a 20.
*	nvda+shift+C: Copia o conteúdo da última coluna lida para a área de
  transferência.

## Mudanças na 3.0 ##
*	 Para buscar textos em caixas de edição somente leitura, pode-se agora
   usar o diálogo e os comandos fornecidos pelo NVDA.

## Mudanças na 2.0 ##
*	 A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.2 ##
*	 Ao mover-se para as mensagens de IRC, o texto selecionado é devidamente
   anunciado.
*	 A tecla de atalho usada para mover para a lista de resultados da busca
   foi generalizada para ser capaz de mover o foco para qualquer lista
   presente na janela atual.
*	 O comando usado para focar as mensagens de IRC foi generalizado para
   mover a qualquer campo de edição somente-leitura, tornando-o capaz de
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

[1]: https://addons.nvda-project.org/files/get.php?file=em

[2]: https://www.emule-project.net

[3]: https://addons.nvda-project.org/files/get.php?file=em-dev
