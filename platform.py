import pygame
import pyganim

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника

ANIMATION_BLOCK_TELEPORT = [
    'levels/portal2.png',
    'levels/portal1.png']

ANIMATION_PRINCESS = [
    'levels/princess_l.png',
    'levels/princess_r.png']


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(
            (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = pygame.image.load("levels/platform.png")
        self.rect = pygame.Rect(
            x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load("levels/dieBlock.png")


class BlockTeleport(Platform):
    def __init__(self, x, y, goX, goY):
        Platform.__init__(self, x, y)
        # координаты назначения перемещения
        self.goX = goX
        # координаты назначения перемещения
        self.goY = goY
        boltAnim = []
        for anim in ANIMATION_BLOCK_TELEPORT:
            boltAnim.append((anim, 1))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(pygame.Color("#7686FF"))
        self.boltAnim.blit(self.image, (0, 0))


class Princess(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        boltAnim = []
        for anim in ANIMATION_PRINCESS:
            boltAnim.append((anim, 600))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(pygame.Color("#7686FF"))
        self.boltAnim.blit(self.image, (0, 0))