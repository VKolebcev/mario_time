import pygame

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
# Группируем ширину и высоту в одну переменную
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
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

        # Не движемся дальше левой границы
        l = min(0, l)
        # Не движемся дальше правой границы
        l = max(-(camera.width - WIN_WIDTH), l)
        # Не движемся дальше нижней границы
        t = max(-(camera.height - WIN_HEIGHT), t)
        # Не движемся дальше верхней границы
        t = min(0, t)

        return pygame.Rect(l, t, w, h)
