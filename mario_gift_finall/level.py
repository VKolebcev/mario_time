import platform

FILE_DIR = "./levels/1.txt"
BG_DIR = "./levels/bg.gif"


class Level:
    pathLevel: str

    def __init__(self, path=FILE_DIR):
        self.pathLevel = path

    def load(self):
        level = []
        with open(self.pathLevel) as file:
            lines_of_file = file.readlines()
            numbers_of_line = len(lines_of_file)
            index = 0
            while index != numbers_of_line - 1:
                if lines_of_file[index] == "[\n":
                    while lines_of_file[index] != "]":
                        index += 1
                        if lines_of_file[index] != "]":
                            end_line = lines_of_file[index].find("|")
                            level.append(lines_of_file[index][:end_line])

        return level
                                            
    def getPlatform(self):
        platforms = []
        x = y = 0
        for row in self.load():
            for col in row:
                if col == "-":
                    pf = platform.Platform(x, y)
                    platforms.append(pf)
                if col == "*":
                    db = platform.BlockDie(x, y)
                    platforms.append(db)
                x += platform.PLATFORM_WIDTH
            y += platform.PLATFORM_HEIGHT
            x = 0

        return platforms
