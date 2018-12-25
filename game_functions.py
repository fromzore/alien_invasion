import sys
import pygame
from bullet import Bullet
from Alien import Alien
from time import sleep

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=ai_settings.screen_height-alien_height-alien_height/2-ship_height
    number_row=int(available_space_y/(alien_height))-1
    return number_row

def creat_fleet(ai_settings,screen,ship,aliens):#fleet舰队
    '''创建外星人群'''
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings,screen,aliens,alien_number,row_number)


def get_number_aliens_x(ai_settings,alien_width):
    available_space_x=ai_settings.screen_width-alien_width/2
    number_alien_x=int(available_space_x/(alien_width))-1
    return number_alien_x

    #创建第一行外星人
def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
        #创建第一个外星人并将其加入当前行
        alien=Alien(ai_settings,screen)
        alien_width = alien.rect.width
        alien.x=alien_width/4+alien_width*alien_number*6/4
        alien.rect.y=alien.rect.height/4+alien.rect.height*row_number*5/4
        alien.rect.x=alien.x
        aliens.add(alien)
# def g_music():
#     pygame.mixer.init()
#     # 加载音乐
#     pygame.mixer.music.load("images/music.mp3")
#     while True:
#         # 检查音乐流播放，有返回True，没有返回False
#         # 如果没有音乐流则选择播放
#         if pygame.mixer.music.get_busy() == False:
#             pygame.mixer.music.play()

def check_keydown_events(event,ship,ai_settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key==pygame.K_SPACE:
       fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:  # 如果用户点叉号，则退出
        sys.exit()


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship,ai_settings,screen,stats,sb,play_button,bullets,aliens):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event,ship,ai_settings,screen,bullets)
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()#返回一个元祖，其中包含玩家单击鼠标时的x和y坐标
                check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''在玩家点击play按钮时开始游戏'''
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)#检查鼠标单击位置是否在play按钮的rect内

    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏鼠标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship_number()


        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并让飞船居中
        creat_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()


def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果还没有达到限制，就发射一颗子弹'''
    #创建新子弹，并将其加入到班组bullets中
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    # screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():#这里因为之前的是绘制飞船时绘制的屏幕，所以for循环只能在ship绘制之后
        bullet.draw_bullet()
    aliens.draw(screen)
    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
   # 删除消失的子弹
    for bullet in bullets.copy():
            if bullet.rect.top<=0:
                bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #检查是否有子弹击中了外星人
    #如果这样，就删除相应的子弹和外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens)==0:
        #如果整群外星人都被消灭，就提高一个等级
        #删除现有子弹并新建一群外星人,加快游戏节奏
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level+=1
        sb.prep_level()
        creat_fleet(ai_settings,screen,ship,aliens)

def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    '''响应外星人撞到的飞船'''
    if stats.ship_left>0:
        #将ship_left减一
        stats.ship_left-=1
        sb.prep_ship_number()

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人，并将飞船放到屏幕地段中央
        creat_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

        #暂停
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    '''更新外星人群中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)


def check_fleet_edges(ai_settings,aliens):
    '''有外星人到达边缘时采取相应的措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    '''将整群外星人下移，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人端'''
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #像飞船被撞一样处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

def check_high_score(stats,sb):
    '''检查是否产生了新的最高分'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.prep_high_score()