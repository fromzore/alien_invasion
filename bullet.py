import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''一个对飞船发射子弹进行管理的类'''

    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen=screen
        self.bullet_image = pygame.image.load('images/bullet.png')
        self.rect = self.bullet_image.get_rect()
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float( self.rect.y)
        self.speed_factor=ai_settings.bullet_speed_factor


    def update(self):
        '''向上移动子弹'''
        #更新表示子弹位置的小数值
        self.rect.centery-=self.speed_factor

    def draw_bullet(self):
        self.screen.blit(self.bullet_image, self.rect)