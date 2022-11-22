import pygame
import pyganim

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника

ANIMATION_BLOCK_TELEPORT = ['levels/portal1.png',
                            'levels/portal2.png']

ANIMATION_PRINCESS = ['levels/princess_l.png',
                      'levels/princess_r.png']

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH,
                                     PLATFORM_HEIGHT))
        self.image = pygame.image.load("levels/platform.png")
        self.rect = pygame.Rect(x, y,
                                PLATFORM_WIDTH,
                                PLATFORM_HEIGHT)

class BlockDie(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("levels/dieBlock.png")

class BlockTeleport(Platform):
    def __init__(self, x, y, goX, goY):
        super().__init__(x, y)
        self.goX = goX
        self.goY = goY

        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image.set_colorkey(pygame.Color(PLATFORM_COLOR))

        bolt_anim = []
        for anim in ANIMATION_BLOCK_TELEPORT:
            bolt_anim.append((anim, 1))

        self.boltAnim = pyganim.PygAnimation(bolt_anim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

class Princess(Platform):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image.set_colorkey(pygame.Color(PLATFORM_COLOR))

        bolt_anim = []
        for anim in ANIMATION_PRINCESS:
            bolt_anim.append((anim, 600))

        self.boltAnim = pyganim.PygAnimation(bolt_anim)
        self.boltAnim.play()

    def update(self):
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.boltAnim.blit(self.image, (0, 0))