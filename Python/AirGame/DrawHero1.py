import pygame
pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
# 1 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2 blit绘制图像
screen.blit(bg, (0, 0))
# 3 update更新图像显示
# pygame.display.update()
# 英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 可以在所有绘制工作完成之后，统一调用update方法
pygame.display.update()
while True:
	pass
pygame.quit()