import pygame

# Объявляем переменные
WIN_WIDTH = 800
WIN_HEIGHT = 640

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


class Camera:
    def __init__(self, width, height):
        self.camera_func = self.camera_configure
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

    @staticmethod
    def camera_configure(camera, target_rect):
        _, _, w, h = camera
        x, y, _, _ = target_rect
        x, y = -x + WIN_WIDTH / 2, -y + WIN_HEIGHT / 2

        x = min(0, x)
        x = max(-(camera.width - WIN_WIDTH), x)

        y = min(0, y)
        y = max(-(camera.height - WIN_HEIGHT), y)

        return pygame.Rect(x, y, w, h)

