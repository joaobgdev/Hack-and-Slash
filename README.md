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
├── 📁 fonts                  # Fontes utilizadas na interface
├── 📁 gui                    # Interface gráfica
├── 📁 logo                   # Logotipos do jogo
├── 📁 sounds                 # Efeitos sonoros e músicas
├── 📁 sprites                # Sprites e imagens dos personagens e objetos
│
├── 🎮 Núcleo do jogo
│   ├── main.py               # Ponto de entrada da aplicação
│   ├── game.py               # Loop principal e gerenciamento do jogo
│   └── audio_manager.py      # Controle de reprodução de sons
│
├── 👤 Entidades
│   ├── player.py             # Implementação do jogador
│   ├── enemy.py              # Implementação dos inimigos
│   ├── serra.py              # Obstáculo do tipo serra
│   └── spritesheet.py        # Manipulação de spritesheets
│
├── 🗺️ Cenários
    ├── sala_base.py          # Classe base das salas
    ├── sala_geral.py         # Sala geral
    ├── sala1.py              # Primeira sala
    ├── sala2.py              # Segunda sala
    ├── sala3.py              # Terceira sala
    └── fase1.py              # Gerenciamento da primeira fase
```


## Galeria do Projeto
<img width="1788" height="1000" alt="Screenshot 2026-07-02 220911" src="https://github.com/user-attachments/assets/4afb7d50-dad7-45a6-a3d8-baafd0b89f98" />
<img width="1784" height="969" alt="Screenshot 2026-07-02 220950" src="https://github.com/user-attachments/assets/0849fb7d-e247-4eae-9723-d85d95f864df" />

## Ferramentas utilizadas

* Python: linguagem utilizada no desenvolvimento do projeto.
* Pygame-ce: responsável pela renderização gráfica, gerenciamento de eventos e execução do jogo.
* Pymunk: utilizado para implementar a física e o sistema de colisões.
* Pyganim: empregado no gerenciamento das animações dos personagens.
* Pyscroll: faz a renderização dos mapas e o sistema de câmera/scrolling.
* pygame_gui: utilizado na criação da interface gráfica e dos menus.
* Pytweening: empregado para animações e transições suaves na interface.
* PyTMX: serve para ler mapas criados no editor Tiled (.tmx) e usá-los no jogo.

## Membros da equipe e suas funções

* [João Bernardo - jbgac](https://github.com/kinobruh)

Foi responsável pela criação de toda a parte visual do jogo, produzindo os sprites, cenários e demais elementos gráficos. Também participou ativamente da programação, implementando diversas funcionalidades do projeto.

* [Kamilla Menezes - krms](https://github.com/kamillaarm)

Auxiliou na programação do projeto, colaborando na implementação e nos testes das funcionalidades. Também foi responsável pela elaboração do README e pela preparação dos slides da apresentação.

* [Lucas Medrado - lms16](https://github.com/lucmedrado)

Atuou principalmente na programação do jogo, desenvolvendo grande parte das mecânicas, corrigindo erros e contribuindo para a organização do código.

* [Sofia Sobreira - ssm](https://github.com/sofiisobreira)

Auxiliou na programação, contribuindo para o desenvolvimento e a integração das funcionalidades. Além disso, participou da elaboração do README e da criação dos slides utilizados na apresentação do projeto.
## Conceitos utilizados

Durante o desenvolvimento do jogo, aplicamos diversos conceitos estudados na disciplina de Introdução à Programação, utilizando-os para implementar as principais mecânicas e organizar o código do projeto.

**Programação Orientada a Objetos (POO):** Utilizamos classes para representar e organizar os principais elementos do jogo, como a classe `Game`, responsável por controlar o funcionamento geral da aplicação. A POO permitiu dividir as responsabilidades do projeto, tornando o código mais organizado, modular e de fácil manutenção.

**Estruturas Condicionais (if / elif / else):** Foram utilizadas para controlar a lógica do jogo e a tomada de decisões. Com elas, implementamos a navegação entre os diferentes estados (menu, opções, jogo e saída), o tratamento das ações do jogador, a resposta aos eventos da interface e outras mecânicas do jogo.

**Funções:** Criamos funções para separar tarefas específicas, como o redimensionamento de imagens e o processamento de sprites. Essa organização evitou repetição de código, facilitou a reutilização de funcionalidades e tornou o projeto mais legível.

**Laços de Repetição (while e for):** O funcionamento do jogo é controlado por um laço `while`, responsável por manter a execução contínua da aplicação enquanto ela estiver aberta. Também utilizamos laços `for` para percorrer eventos do Pygame, processar animações e manipular coleções de elementos do jogo de forma eficiente.

## Desafios, erros e aprendizados

**Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?**

O maior desafio foi conciliar o desenvolvimento do jogo com as provas, trabalhos e projetos de outras disciplinas, que aconteceram no mesmo período. Muitas vezes, tivemos pouco tempo para trabalhar no projeto. Para lidar com isso, dividimos as tarefas entre os integrantes, organizamos melhor o que precisava ser feito e aproveitamos o tempo disponível para desenvolver e testar o jogo. Assim, conseguimos concluir o projeto dentro do prazo.

**Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?**

O maior erro durante o projeto foi a dificuldade de organizar o código usando Programação Orientada a Objetos (POO). Como ainda estávamos aprendendo esse modelo de programação, tivemos dúvidas sobre como dividir as responsabilidades das classes e organizar melhor o código. Isso fez com que algumas partes precisassem ser refeitas. Para resolver esse problema, reorganizamos algumas classes, fizemos ajustes no código e buscamos entender melhor os conceitos de POO, deixando o projeto mais organizado e fácil de manter.


**Quais as lições aprendidas durante o projeto?**

A principal lição foi que organização e trabalho em equipe são fundamentais para o sucesso de um projeto. Também aprendemos que planejar melhor a estrutura do código, principalmente usando POO, evita problemas no futuro e facilita a implementação de novas funcionalidades. Além disso, o projeto nos ajudou a melhorar nossos conhecimentos em Python e Pygame e mostrou a importância da comunicação, da divisão de tarefas e do planejamento durante o desenvolvimento.
