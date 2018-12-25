import sys
import pygame
from settings import Settings
from ship import Ship
from Alien import Alien
import game_functions as gf
from pygame.sprite import Group
from  game_stas import GameStats
from  button import  Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()#初始化背景设置，让Pygame能够正长工作
    # screen=pygame.display.set_mode((1200,800))#实参（1200，800）是一个元组，制定了游戏窗口的尺寸
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #创建一艘新飞船
    ship=Ship(screen)
    #创建一个用于存储子弹的编组
    bullets=Group()
    #创建一个外星人
    aliens=Group()
    #创建play按钮
    play_button=Button(ai_settings,screen,"Play")
    gf.creat_fleet(ai_settings,screen,ship,aliens)
    # gf.g_music()

    #设置背景色
    #bg_color=(230,250,250)

    #开始游戏的主循环
    while True:
        gf.check_events(ship,ai_settings,screen,stats,sb,play_button,bullets,aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()