S.O.N.E.G.A.

Trabalho em grupo da cadeira Programação I.

integrantes: Miguel Arcanjo de Lima Silva, Ariadny Barreto Nelson, Arthur Viegas Proenca

S.O.N.E.G.A. é um jogo de aventura de texto, jogado no terminal, em que o jogador escolhe o caminho digitando números.

Você é Marlene Peixes, a única zeladora dos escritórios da BAZINGA CORP. Hoje é o aniversário de 12 anos da sua filha e você só quer sair mais cedo. Seu chefe, o Doutor Wag. A. Bündo Bichstenbäuer, não pensa assim e você acaba caindo num calabouço debaixo da empresa.

Para sair de lá, é preciso reunir as peças de uma arma especial, a S.O.N.E.G.A. (Super Onda Neutralizadora Extintora de Gerentes Asnos): GATILHO, CANO, TAMBOR, CABO e CÃO. A ARMAÇÃO já está com o Marcelo.

O jogo tem dois finais:
Final 4-A: a jogadora chega ao Capítulo 3 com todas as peças.
Final 4-B: a jogadora chega ao Capítulo 3 sem alguma das peças.

Para rodar o projeto, baixe ou clone o repositorio em seu computador e rode python main.py no seu terminal.

Controles: 
Digite o número de uma das opções mostradas para escolher..
o save é automatico caso o jogo feche do nada, ao reabrir aparece a opção continuar ou novo jogo.
O save fica no arquivo save.json, na pasta do projeto, e é apagado quando o jogo termina

ESTRUTURA: 

main.py: dicionário de cenas, sistema de save e loop principal do jogo.
funcoes/funcoes.py: todas as cenas do jogo(cada uma é uma função) e a funcao de perguntar
dialogos/textos.py: os textos do roteiro.
dialogos/desenhos.py: os desenhos em ASCII.
personagens/personagens.py: os dados da personagem (inventário).

Bibliotecas: 
apenas as bibliotecas padroes do python foram usadas: 
time, json e os

RESPONSABILIDADES: 
MIguel --> responsavel por definir como seria criado a "estrutura" para rodar o codigo, programar proriamente dito, revisar e testar.
Arthur --> resposanvel pela criacao total do roteiro da historia e participar da criacao de cenas do jogo no codigo
Ariadny --> responsavel pela criacao total dos desenhos usados e participar da criacao de cenas do jogo no codigo

o codigo é separado por arquivos que contem pastas cada uma com uma funcionalidade unica, o jogo funciona atraves de funcoes, cada lugar da historia é uma funcao no codigo, dentro das funcoes acontecem a historia daquela cena e fica para o usuario escolher oque vai fazer naquela cena, cada escolha do usuario é um RETURN na funcao que aponta para outro cenario (que foi escolhido pelo jogador)


