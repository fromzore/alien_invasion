class Settings(object):
    '''存储这个游戏的所有设置类'''

    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width=512
        self.screen_height=640
        # self.bg_color=(230,250,250)
        #子弹设置
        self.bullets_allowed=3
        #外星人设置
        self.fleet_drop_speed=10
        self.ship_limit=3
        #以什么样的速度加快游戏节奏
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor=0.4
        self.fleet_direction = 1  # 1表示右移，-1表示左移
        #记分
        self.alien_points=1

    def increase_speed(self):
        '''提高速度设置'''
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale