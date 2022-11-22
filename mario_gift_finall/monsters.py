import pygame
import pyganim

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#2110FF"

ANIMATION_MONSTER = ['levels/fire1.png',
                     'levels/fire2.png']


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, left, up, max_length, max_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(pygame.Color(MONSTER_COLOR))
        self.rect = pygame.Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(pygame.Color(MONSTER_COLOR))

        self.startX = x
        self.startY = y

        self.xvel = left
        self.yvel = up

        self.max_length = max_length
        self.max_height = max_height

        bolt_anim = []
        for anim in ANIMATION_MONSTER:
            bolt_anim.append((anim, 1))

        self.boltAnim = pyganim.PygAnimation(bolt_anim)
        self.boltAnim.play()

    def update(self, platforms):
        self.image.fill(pygame.Color(MONSTER_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.x += self.xvel
        self.rect.y += self.yvel

        self.collide(platforms)

        if abs(self.startX - self.rect.x) > self.max_length:
            self.xvel = -self.xvel

        if abs(self.startY - self.rect.y) > self.max_height:
            self.yvel = -self.yvel

    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p) and self != p:
                self.xvel = -self.xvel
                self.yvel = -self.yvel