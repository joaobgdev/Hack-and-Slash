# Hack and Slash

## Visão Geral

Hack and Slash é um jogo de ação e plataforma 2D ambientado em um mundo cyberpunk, combinando elementos tecnológicos futuristas com uma estética inspirada no Y2K.

## Ambientação

O jogo se passa em um grande prédio corporativo de alta tecnologia. O cenário mistura neon, implantes cibernéticos, inteligência artificial e elementos visuais característicos da cultura digital dos anos 2000.

## Premissa

A protagonista é uma ciborgue assassina de aluguel que possui uma espada equipada com inteligência artificial capaz de se comunicar com ela. Após receber um contrato para eliminar o diretor de uma poderosa corporação, ela invade o prédio da empresa para cumprir sua missão. No entanto, antes de chegar ao seu alvo, será necessário superar os sistemas de segurança, explorar o complexo e enfrentar os perigos que protegem o chefe da organização.

## Instruções

### Como executar o jogo

Para executar o jogo, é necessário ter o Python instalado no computador (versão 3.13).

### Instalação das dependências

O jogo utiliza algumas bibliotecas. Entretanto, não é necessário instalar cada biblioteca individualmente. Todas as dependências já estão listadas no arquivo requirements.txt.

Após clonar ou baixar o projeto, abra um terminal na pasta do projeto e execute o seguinte comando:
```bash
pip install -r requirements.txt
```
Esse comando instalará automaticamente todas as bibliotecas necessárias para o funcionamento do jogo.

### Executando o jogo

Depois que a instalação das dependências for concluída, execute o arquivo principal do projeto utilizando o Python.
```bash
python main.py
```
## 📁 Arquitetura do Projeto

```
│
├── 📁 fonts                  # Fonte utilizada na interface
├── 📁 gui                    # Interface gráfica
├── 📁 logo                   # Logotipo do jogo
├── 📁 sounds                 # Efeitos sonoros e músicas
├── 📁 sprites                # Sprites e imagens dos personagens e objetos
│
├── 🎮 Núcleo do jogo
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── game.py               # Loop principal e gerenciamento do jogo
│   └── audio_manager.py      # Controle de reprodução de sons
    └── spritesheet.py        # Manipulação de spritesheets
│
├── 👤 Entidades
│   ├── player.py             # Implementação do jogador
│   ├── enemy.py              # Implementação dos inimigos
│   └── serra.py              # Obstáculo do tipo serra
│   
│
└── 🗺️ Cenários
    ├── fase1.py              # Sala do tutorial
    ├── sala_geral.py         # Sala geral
    ├── sala1.py              # Primeira sala
    ├── sala2.py              # Segunda sala
    └── sala3.py              # Terceira sala

```


## Galeria do Projeto
<img width="1788" height="1000" alt="Screenshot 2026-07-02 220911" src="https://github.com/user-attachments/assets/4afb7d50-dad7-45a6-a3d8-baafd0b89f98" />
<img width="1784" height="969" alt="Screenshot 2026-07-02 220950" src="https://github.com/user-attachments/assets/0849fb7d-e247-4eae-9723-d85d95f864df" />

## Bibliotecas e Ferramentas utilizadas

**Bibliotecas utilizadas:**
* Pygame: Biblioteca que permite criação de jogos e interfaces visuais através do Python.
* Pymunk: Responsável pela física e sistema de colisões.
* Pygame_gui: Usado para implementação de botões e interfaces interativas.
* Pytweening: Usado para criar animações fluidas através de funções matemáticas.
* Colorsys: Usado para gerenciamento de cores e filtros.
* Random: Usado para criar eventos e efeitos randômicos durante a gameplay.
* Math: Usado para gerenciar funções matemáticas de maneira simples (Usado somente no inimigo)
* Sys: Ajusta o funcionamento do jogo quando rodado em exe para evitar bugs.
* Pathlib: Facilita o acesso a pastas para receber sprites, sons e etc sem muita repetição de textos longos.
* Enum: Foi usado para guardar o estado atual do jogo (Salas, Menus) como um GameState enumerável e permitir fácil troca de GameStates.

**Ferramentas:**
* Krita: Foi usado para desenhar todos os sprites originais do jogo.
* Sites de Assets, Músicas e SFX: Alguns dos Sound Effects foram criados com IA (Dash), outros foram instalados de sites como Pixabay e Audiio, as músicas do jogo também foram baixadas do Pixabay, a maioria dos Assets de pixel art não autorais foram baixados do itch.io

## Membros da equipe e suas funções

* [João Bernardo - jbgac](https://github.com/kinobruh) - Foi responsável pela criação de toda a parte visual do jogo, produzindo os sprites, cenários e demais elementos gráficos. Também participou ativamente da programação, implementando diversas funcionalidades do projeto.

* [Kamilla Menezes - krms](https://github.com/kamillaarm) - Auxiliou na programação do projeto, colaborando na implementação e nos testes das funcionalidades. Também foi responsável pela elaboração do README e pela preparação dos slides da apresentação.

* [Lucas Medrado - lms16](https://github.com/lucmedrado) - Atuou principalmente na programação do jogo, desenvolvendo grande parte das mecânicas, corrigindo erros e contribuindo para a organização do código.

* [Sofia Sobreira - ssm](https://github.com/sofiisobreira) - Auxiliou na programação, contribuindo para o desenvolvimento e a integração das funcionalidades. Além disso, participou da elaboração do README e da criação dos slides utilizados na apresentação do projeto.

## Conceitos utilizados

Durante o desenvolvimento do jogo, aplicamos diversos conceitos estudados na disciplina de Introdução à Programação, utilizando-os para implementar as principais mecânicas e organizar o código do projeto.

**Programação Orientada a Objetos (POO):** Utilizamos classes para representar e organizar os principais elementos do jogo, como a classe `Game`, responsável por controlar o funcionamento geral da aplicação. A POO permitiu dividir as responsabilidades do projeto, tornando o código mais organizado, modular e de fácil manutenção.

**Estruturas Condicionais (if / elif / else):** Foram utilizadas para controlar a lógica do jogo e a tomada de decisões. Com elas, implementamos a navegação entre os diferentes estados (menu, opções, jogo e saída), o tratamento das ações do jogador, a resposta aos eventos da interface e outras mecânicas do jogo.

**Funções:** Criamos funções para separar tarefas específicas, como o redimensionamento de imagens e o processamento de sprites. Essa organização evitou repetição de código, facilitou a reutilização de funcionalidades e tornou o projeto mais legível.

**Laços de Repetição (while e for):** O funcionamento do jogo é controlado por um laço `while`, responsável por manter a execução contínua da aplicação enquanto ela estiver aberta. Também utilizamos laços `for` para percorrer eventos do Pygame, processar animações e manipular coleções de elementos do jogo de forma eficiente.

## Desafios, erros e aprendizados

**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**

O maior desafio foi desenvolver o jogo utilizando o Pygame, que possui algumas limitações em relação a uma engine de jogos. Muitas funcionalidades, como o sistema de câmera e diversos elementos do jogo, precisaram ser implementadas manualmente. Além disso, a maior parte dos ajustes só podia ser feita testando o jogo repetidas vezes, já que era necessário executá-lo para verificar a posição dos objetos, colisões e outros detalhes visuais. Para lidar com isso, realizamos testes constantes, corrigimos os problemas conforme apareciam e fomos aperfeiçoando cada funcionalidade aos poucos.

**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**

O maior erro durante o projeto foi a dificuldade de organizar o código usando Programação Orientada a Objetos (POO). Como ainda estávamos aprendendo esse modelo de programação, tivemos dificuldades para estruturar as classes e fazer com que todos os arquivos do projeto funcionassem corretamente em conjunto. Para resolver isso, reorganizamos partes do código, fizemos ajustes durante o desenvolvimento e buscamos entender melhor como aplicar os conceitos de POO na prática.


**Quais as lições aprendidas durante o projeto?**

Durante o projeto, aprofundamos nossos conhecimentos em Python, principalmente sobre funções, constantes e organização do código. Também aprendemos a utilizar melhor a Programação Orientada a Objetos, entendendo como estruturar classes e fazer com que diferentes arquivos trabalhem juntos em um mesmo sistema. Além dos conhecimentos técnicos, aprendemos que testar o jogo com frequência e manter o código organizado facilita muito o desenvolvimento e a correção de erros.
