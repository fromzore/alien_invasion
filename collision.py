import pygame
from pygame.sprite import Sprite

class collision(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(collision,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image = pygame.image.load('images/img/boom_big.png')
        self.rect = self.image.get_rect()


    def alien_ship_collision(self):
            self.screen.blit(self.image, self.rect)

