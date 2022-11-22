#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
import player
import level
import camera


def main():
    pygame.init()

    screen = pygame.display.set_mode(camera.DISPLAY)
    pygame.display.set_caption("Арнольд и платформы")
    bg = pygame.image.load(level.BG_DIR)

    hero = player.Player(55, 55)
    timer = pygame.time.Clock()

    animated_entities = pygame.sprite.Group()
    tp = level.platform.BlockTeleport(128, 512, -50, 0)

    mn = player.monsters.Monster(190, 200, 2, 3, 150, 15)

    pr = level.platform.Princess(400, 300)


    monsters = pygame.sprite.Group()

    entities = pygame.sprite.Group()
    level_1 = level.Level()
    platforms = level_1.getPlatform()
    entities.add(hero)
    entities.add(tp)
    animated_entities.add(tp)
    platforms.append(tp)

    entities.add(mn)
    platforms.append(mn)
    monsters.add(mn)

    entities.add(pr)
    platforms.append(pr)
    animated_entities.add(pr)

    for platform in platforms:
        entities.add(platform)

    total_level_width = len(level_1.load()[0]) * \
                        level.platform.PLATFORM_WIDTH
    total_level_height = len(level_1.load()) * \
                         level.platform.PLATFORM_HEIGHT

    main_camera = camera.Camera(total_level_width,
                                total_level_height)

    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(1)
            hero.move(event)

        screen.blit(bg, (0, 0))
        hero.update(platforms)
        main_camera.update(hero)
        for entity in entities:
            screen.blit(entity.image, main_camera.apply(entity))

        animated_entities.update()
        monsters.update(platforms)
        pygame.display.update()

        if hero.winner:
            raise SystemExit(1)



if __name__ == "__main__":
    main()
