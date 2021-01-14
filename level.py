import platform

FILE_DIR = "levels/1.txt"
BG_DIR = "levels/bg.gif"


class Level:
    pathLevel: str

    def __init__(self, path=FILE_DIR):
        self.pathLevel = path

    def load(self):
        level = []
        with open(self.pathLevel) as file:
            linesOfFile = file.read().split("\n")
            numberOfLines = len(linesOfFile)
            index = 0
            # идем по всем строкам в файле
            while (index != numberOfLines - 1):
                # если нашли символ начала уровня
                if linesOfFile[index] == "[":
                    # то, пока не нашли символ конца уровня
                    while linesOfFile[index] != "]":
                        index += 1
                        # и если нет символа конца уровня
                        if linesOfFile[index] != "]":
                            # то ищем символ конца строки
                            endLine = linesOfFile[index].find("|")
                            # и добавляем в уровень строку от начала до символа "|"
                            level.append(linesOfFile[index][0: endLine])
        return level

    def getPlatform(self):
        platforms = []
        x = y = 0  # координаты
        for row in self.load():  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = platform.Platform(x, y)
                    platforms.append(pf)
                if col == "*":
                    bd = platform.BlockDie(x, y)
                    platforms.append(bd)

                # блоки платформы ставятся на ширине блоков
                x += platform.PLATFORM_WIDTH
            # то же самое и с высотой
            y += platform.PLATFORM_HEIGHT
            x = 0  # на каждой новой строчке начинаем с нуля

        return platforms

    def getPrincess(self, entities, animatedEntities, platforms):
        x = y = 0  # координаты
        for row in self.load():  # вся строка
            for col in row:  # каждый символ
                if col == "P":
                    pr = platform.Princess(x, y)
                    entities.add(pr)
                    platforms.append(pr)
                    animatedEntities.add(pr)

                # блоки платформы ставятся на ширине блоков
                x += platform.PLATFORM_WIDTH
            # то же самое и с высотой
            y += platform.PLATFORM_HEIGHT
            x = 0  # на каждой новой строчке начинаем с нуля