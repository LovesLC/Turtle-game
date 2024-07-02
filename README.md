## Descrição Técnica
Este jogo implementado em Python com a biblioteca Turtle simula uma competição entre um jogador e um computador. Ambos movem robôs representados por tartarugas em um grid 5x5. O jogador insere comandos ('U', 'D', 'L', 'R') para mover sua tartaruga cor-de-rosa, enquanto o computador gera aleatoriamente comandos para sua tartaruga azul. O objetivo é alcançar a posição [5, 5] primeiro. O resultado, número de movimentos e vencedor são exibidos na tela após cada rodada.

## Funcionalidades Implementadas:
### Inicialização e Configuração:

 - Define o tamanho do grid como 5x5 e o tamanho de cada célula como 50 pixels.
 - Configura a interface Turtle com fundo azul claro e título apropriado.
### Desenho do Grid:

 - Utiliza Turtle para desenhar linhas que formam o grid na tela, facilitando a visualização do jogo.
### Movimentação dos Robôs:

 - Métodos para mover a tartaruga do jogador e do computador com base nos comandos inseridos ou gerados aleatoriamente.
### Interação com o Jogador:

 - Utiliza uma caixa de diálogo para que o jogador insira uma sequência de comandos válidos para mover sua tartaruga.
### Geração Aleatória de Comandos:

 - Gera aleatoriamente uma sequência de comandos para movimentar a tartaruga do computador.
### Exibição de Resultados:

 - Após cada rodada, exibe na tela o número de movimentos realizados por cada jogador e o resultado da rodada (quem alcançou [5, 5] primeiro ou se houve empate).
## Estrutura do Código:
 - Classes:

 - CuteRobotGame: Contém métodos para inicialização, desenho do grid, criação e movimentação das tartarugas, além de gerenciar a lógica do jogo.
 - Função Principal:

 - main(): Cria uma instância de CuteRobotGame, inicia o jogo e exibe os resultados na tela Turtle.
### Requisitos:
 - Python 3.x
 - Biblioteca turtle
### Uso:
 - Execução:
 - Execute o script Python para iniciar o jogo.
 - Insira os comandos ('U', 'D', 'L', 'R') quando solicitado para o jogador.
 - Acompanhe o progresso do jogo na tela Turtle.
### Autor:
João Victor da Silva

Contribuições:
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorias ou correções.
