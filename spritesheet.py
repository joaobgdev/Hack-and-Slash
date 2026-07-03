from __future__ import annotations
import pygame

class Spritesheet:
   
    def __init__(self, image: pygame.Surface):
        self.sheet = image.convert_alpha()

#get image pega um unico frame da spritesheet
    def get_image(self, frame: int, row: int, width: int, height: int, scale: float, color: tuple):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (frame * width, row * height, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color)
        return image

#get animation chama get image várias vezes em um loop e retorna uma lista de frames, fazendo a animação
    def get_animation(self, row: int, num_frames: int, width: int, height: int, scale: float,color: tuple):
        return [self.get_image(frame, row, width, height, scale, color) for frame in range(num_frames)]
