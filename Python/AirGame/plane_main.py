import pygame
from PlaneSprites import *

from test.Python.AirGame.PlaneSprites import CREATE_ENEMY_EVENT, BackGround, FRAME_PER_SEC, SCREEN_RECT


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print('游戏初始化')

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 4.设置定时器事件 -创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = BackGround(False)
        bg2 = BackGround(True)
        self.back_ground = pygame.sprite.Group(bg1, bg2)
        pass

    def start_game(self):
        print('游戏开始……')
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)

            # 2.时间监听
            self.__event_handler()

            # 3.碰撞检测
            self.__check_collide()

            # 4.更新/绘制精灵组
            self.__update_sprites()

            # 5.更新显示
            pygame.display.update()

            pass

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print('敌机出场……')

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        pass

    @staticmethod
    def __game_over():
        print('游戏结束')

        pygame.quit()  # 卸载所有模块
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
