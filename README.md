# Hack and Slash

## Visão Geral

Hack and Slash é um jogo de ação e plataforma 2D ambientado em um mundo cyberpunk, combinando elementos tecnológicos futuristas com uma estética inspirada no Y2K.

## Ambientação

O jogo se passa em um grande prédio corporativo de alta tecnologia. O cenário mistura neon, implantes cibernéticos, inteligência artificial e elementos visuais característicos da cultura digital dos anos 2000.

## Premissa

A protagonista é uma ciborgue assassina de aluguel que possui uma espada equipada com inteligência artificial capaz de se comunicar com ela. Após receber um contrato para eliminar o diretor de uma poderosa corporação, ela invade o prédio da empresa para cumprir sua missão. No entanto, antes de chegar ao seu alvo, será necessário superar os sistemas de segurança, explorar o complexo e enfrentar os perigos que protegem o chefe da organização.

## Instruções

## Arquitetura do Projeto

📁 Projeto
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
* [Kamilla Menezes - krms](https://github.com/kamillaarm)
* [Lucas Medrado - lms16](https://github.com/lucmedrado)
* [Sofia Sobreira - ssm](https://github.com/sofiisobreira)

## Conceitos utilizados

## Desafios, erros e aprendizados
