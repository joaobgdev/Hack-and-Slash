from __future__ import annotations
import pygame

from sala_base import SalaBase
from enemy import InimigoMelee

#procura na pasta sprites
enemy2 = pygame.image.load("sprites/enemy2.png")
enemy2 = pygame.transform.scale_by(enemy2, 3)

class Sala1(SalaBase):

    CLAMP_MIN_X = 190
    def __init__(self, superficie: pygame.Surface, sprite_raio: pygame.Surface):
        super().__init__(superficie)
        self.CLAMP_MAX_X = self.largura - 70
        
        self.sprite_raio = sprite_raio
        self.booster_x = self.largura // 2  # meio da sala
        
        #altura
        self.booster_y = 450
        
        self.booster_largura = self.sprite_raio.get_width()
        self.booster_altura = self.sprite_raio.get_height()
        self.booster_coletado = False
        
        self.inimigos = [
            #alterar as cordenadas se necessario
            #Inimigo 1
            # y muda a altura da base
            #alterei 1
            InimigoMelee(x=800, y=600, patrulha_min=600, patrulha_max=1000, sprite=enemy2),
            
            #Inimigo 2
            InimigoMelee(x=2000, y=600, patrulha_min=1800, patrulha_max=2200, sprite=enemy2)
        ]

    def update(self, time_delta: float, player, space, volume_sfx: float = 1.0, damage_sfx=None, speed_sfx=None):
        player.update(space, time_delta)
        self.clamp_player(player)
        
        player_rect = pygame.Rect(
            player.body.position.x - 48,
            player.body.position.y - 160,
            96,
            320
        )

        for inimigo in self.inimigos:
            inimigo.update(time_delta, player.body.position.x)
            
            if inimigo.hitbox_ataque and not inimigo.ja_causou_dano:
                if player_rect.colliderect(inimigo.hitbox_ataque):
                    player.levar_dano(1)
                    inimigo.ja_causou_dano = True
                    if damage_sfx:
                        damage_sfx.set_volume(volume_sfx)
                        damage_sfx.play()

            if (player.atacando and player.hitbox_ataque and inimigo.vivo
                    and not player.acertou_ataque):
                if player.hitbox_ataque.colliderect(inimigo.get_rect()):
                    inimigo.levar_dano()
                    player.acertou_ataque = True

        
        if not self.booster_coletado:
            booster_rect = pygame.Rect(
                self.booster_x - self.booster_largura // 2,
                self.booster_y - self.booster_altura // 2,
                self.booster_largura,
                self.booster_altura
            )
            
            if player_rect.colliderect(booster_rect):
                self.booster_coletado = True
                player.booster_ativo = True
                player.booster_timer = 5.0
                if speed_sfx:
                    speed_sfx.set_volume(volume_sfx)
                    speed_sfx.play()

    def draw(self, screen: pygame.Surface, player, camera_x: int, pos_x: int, pos_y: int, time_delta: float = 0):
        screen.fill((0, 0, 0))
        screen.blit(self.superficie, (-camera_x, 10))
            
        player.draw(screen, pos_x, pos_y)


        if not self.booster_coletado:
            x_tela = (self.booster_x - self.booster_largura // 2) - camera_x
            y_tela = self.booster_y - self.booster_altura // 2
            
            screen.blit(self.sprite_raio, (x_tela, y_tela))
            
        for inimigo in self.inimigos:
            inimigo.draw(screen, camera_x)

        player.draw(screen, pos_x, pos_y)

    def checar_saida(self, player_x: float, screen: pygame.Surface, E_gui: pygame.Surface):
        super().checar_saida(player_x, screen, E_gui)