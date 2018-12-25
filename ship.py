import pygame

class Ship(object):
    def __init__(self,screen):
        '''初始化飞船，并设定其初始位置'''
        self.screen=screen



        #加载飞船图像，并获取其外接矩形
        self.image=pygame.image.load('images/img/plane_2.png')
        self.screen_image=pygame.image.load('images/bg_2.jpg')
        self.rect=self.image.get_rect()#获取飞船外接矩形
        self.screen_rect=screen.get_rect()#获取表示屏幕的矩形
        self.screen_image_rect=self.screen_image.get_rect()


        #将每艘新飞船放在屏幕底部中央
        self.screen_image_rect.centerx=self.screen_rect.centerx
        self.screen_image_rect.bottom = self.screen_rect.bottom
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom


        #移动标示
        self.moving_right=False
        self.moving_left=False

        self.moving_up = False
        self.moving_down = False



    def update(self):
        ''' 根据移动标示移动飞船'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=1
        if self.moving_left and self.rect.left>0:
            self.rect.centerx-=1
        if self.moving_up and self.rect.top>0:
            self.rect.centery-=1
        if self.moving_down and self.rect.bottom<640:
            self.rect.centery+=1

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.centerx=self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
       '''在指定位置绘制飞船'''
       self.screen.blit(self.screen_image, self.screen_image_rect)
       self.screen.blit(self.image, self.rect)  # blitme（），根据self.rect将图片绘制到屏幕上。
