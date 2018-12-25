import pygame.font

class Scoreboard(object):
    '''显示得分信息的类'''

    def __init__(self,ai_settings,screen,stats):
        '''初始化显示得分涉及的属性'''
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        #显示得分信息时使用的字体设置
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,18)
        self.bg_color=(0,130,150)

        #准备初始得分图像和最高分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship_number()

    def prep_score(self):
        '''将得分转换为一副渲染的图像'''
        score_str="Score:"+"{:,}".format(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.bg_color)

        #将得分放在屏幕右上角
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-10
        self.score_rect.top=10

    def prep_high_score(self):
        '''将最高分转换为渲染图像'''
        high_score_str="HighScore:"+"{:,}".format(self.stats.high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.bg_color)

        #将最高分放在屏幕顶部中央
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.top=self.score_rect.top
        self.high_score_rect.centerx=self.screen_rect.centerx

    def prep_level(self):
        '''将等级转换为一副渲染的图像'''
        self.level_image=self.font.render(("Level:"+str(self.stats.level)),True,self.text_color,self.bg_color)

        #将得分放在屏幕右上角
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+5

    def prep_ship_number(self):
        '''将飞船数量转换为一副渲染的图像'''
        self.shipnumber_image = self.font.render(("ShipNumber:" + str(self.stats.ship_left)), True, self.text_color, self.bg_color)

        # 将得分放在屏幕左上角
        self.shipnumber_rect = self.shipnumber_image.get_rect()
        self.shipnumber_rect.left = self.screen_rect.left+5
        self.shipnumber_rect.top = self.score_rect.top



    def show_score(self):
        '''在屏幕上显示当前得分和最高分'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.shipnumber_image,self.shipnumber_rect)