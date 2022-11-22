#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import pyganim
import platform
import monsters

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз

ANIMATION_DELAY = 1
ANIMATION_RIGHT = ['levels/r1.png',
                   'levels/r2.png',
                   'levels/r3.png',
                   'levels/r4.png',
                   'levels/r5.png']
ANIMATION_LEFT = ['levels/l1.png',
                  'levels/l2.png',
                  'levels/l3.png',
                  'levels/l4.png',
                  'levels/l5.png']
ANIMATION_JUMP_LEFT = [('levels/jl.png', ANIMATION_DELAY)]
ANIMATION_JUMP_RIGHT = [('levels/jr.png', ANIMATION_DELAY)]
ANIMATION_JUMP = [('levels/j.png', ANIMATION_DELAY)]
ANIMATION_STAY = [('levels/0.png', ANIMATION_DELAY)]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # скорость перемещения. 0 - стоять на месте
        self.xvel = 0
        # скорость вертикального перемещения
        self.yvel = 0
        # Начальная позиция Х
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.image.set_colorkey(pygame.Color(COLOR))

        bolt_anim = []
        for anim in ANIMATION_RIGHT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(bolt_anim)
        self.boltAnimRight.play()

        bolt_anim = []
        for anim in ANIMATION_LEFT:
            bolt_anim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(bolt_anim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

        # прямоугольный объект
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.left = False
        self.right = False
        self.up = False
        self.onGround = False  # На земле ли я?
        self.winner = False

    def update(self, platforms):
        if self.up:
            # прыгаем, только когда можем оттолкнуться от земли
            if self.onGround:
                self.yvel = -JUMP_POWER
            elif not self.onGround and not (self.left or self.right):
                self.image.fill(pygame.Color(COLOR))
                self.boltAnimJump.blit(self.image, (0, 0))

        if self.left:
            self.xvel = -MOVE_SPEED  # Лево = x- n
            self.image.fill(pygame.Color(COLOR))
            if self.onGround:
                if self.up and not self.onGround:
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
                else:
                    self.boltAnimLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))

        if self.right:
            self.xvel = MOVE_SPEED  # Право = x + n
            self.image.fill(pygame.Color(COLOR))
            if self.onGround:
                if self.up and not self.onGround:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimRight.blit(self.image, (0, 0))
            else:
                self.boltAnimJumpRight.blit(self.image, (0, 0))

        # стоим, когда нет указаний идти
        if not (self.left or self.right):
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        # Мы не знаем, когда мы на земле
        self.onGround = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            # если есть пересечение платформы с игроком
            if pygame.sprite.collide_rect(self, p):

                if isinstance(p, platform.BlockDie) \
                        or isinstance(p, monsters.Monster):
                    self.die()
                if isinstance(p, platform.BlockTeleport):
                    self.teleporting(p.goX, p.goY)
                if isinstance(p, platform.Princess):
                    self.winner = True

                if xvel > 0:  # если движется вправо
                    # то не движется вправо
                    self.rect.right = p.rect.left

                if xvel < 0:  # если движется влево
                    # то не движется влево
                    self.rect.left = p.rect.right

                if yvel > 0:  # если падает вниз
                    # то не падает вниз
                    self.rect.bottom = p.rect.top
                    # и становится на что-то твердое
                    self.onGround = True
                    # и энергия падения пропадает
                    self.yvel = 0

                if yvel < 0:  # если движется вверх
                    # то не движется вверх
                    self.rect.top = p.rect.bottom
                    # и энергия прыжка пропадает
                    self.yvel = 0

    def move(self, event):
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_LEFT:
            self.left = True
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_RIGHT:
            self.right = True
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_UP:
            self.up = True

        if event.type == pygame.KEYUP and \
            event.key == pygame.K_LEFT:
            self.left = False
        if event.type == pygame.KEYUP and \
            event.key == pygame.K_RIGHT:
            self.right = False
        if event.type == pygame.KEYUP and \
            event.key == pygame.K_UP:
            self.up = False

    def die(self):
        pygame.time.wait(500)
        self.teleporting(100, 100)

    def teleporting(self, goX, goY):
        self.rect.x += goX
        self.rect.y += goY
