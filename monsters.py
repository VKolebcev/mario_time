#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim

MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#2110FF"

ANIMATION_MONSTER = [
    'levels/fire1.png',
    'levels/fire2.png']


class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft, maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.image.set_colorkey(Color(MONSTER_COLOR))
        self.startX = x  # начальные координаты
        self.startY = y
        # максимальное расстояние, которое может пройти в одну сторону
        self.maxLengthLeft = maxLengthLeft
        # максимальное расстояние, которое может пройти в одну сторону, вертикаль
        self.maxLengthUp = maxLengthUp
        # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.xvel = left
        # скорость движения по вертикали, 0 - не двигается
        self.yvel = up
        boltAnim = []
        for anim in ANIMATION_MONSTER:
            boltAnim.append((anim, 1))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self, platforms):  # по принципу героя

        self.image.fill(Color(MONSTER_COLOR))
        self.boltAnim.blit(self.image, (0, 0))

        self.rect.y += self.yvel
        self.rect.x += self.xvel

        self.collide(platforms)

        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            # если прошли максимальное растояние, то идеи в обратную сторону
            self.xvel = -self.xvel
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            # если прошли максимальное растояние, то идеи в обратную сторону, вертикаль
            self.yvel = -self.yvel

    def collide(self, platforms):
        for p in platforms:
            # если с чем-то или кем-то столкнулись
            if sprite.collide_rect(self, p) and self != p:
                # то поворачиваем в обратную сторону
                self.xvel = - self.xvel
                self.yvel = - self.yvel