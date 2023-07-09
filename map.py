from pygame import*
import math
game_map = [
    # 1   2    3    4   5    6     7    8    9   10    11   12   13    14   15
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', "_", "_", "A", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "_", "_", "A", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "_", "_", "A", "_", "_", "A", "A", "A", "A", "A", "A", "_", "_", 'A'],
    ['A', "_", "_", "A", "_", "_", "A", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "_", "_", "A", "_", "_", "A", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "_", "_", "_", "_", "_", "A", "_", "_", "A", "A", "A", "A", "A", 'A'],
    ['A', "_", "_", "_", "_", "_", "A", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "A", "A", "A", "_", "_", "A", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "_", "_", "_", "_", "_", "A", "A", "A", "A", "A", "A", "_", "_", 'A'],
    ['A', "_", "_", "_", "_", "_", "A", "_", "_", "A", "_", "A", "_", "_", 'A'],
    ['A', "_", "_", "A", "A", "A", "A", "_", "_", "A", "_", "A", "_", "_", 'A'],
    ['A', "_", "_", "_", "_", "_", "-", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
]

class Block:

    def __init__(self, color, x, y, width, height, image_name):

        self.color = color
        self.rect = Rect(x, y, width, height)
        self.image = transform.scale(
            image.load(image_name),
            (width, height)
        )
    def draw(self, window):
        draw.rect(window, self.color, self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y))


def make_map():
    SIZE = 810 / 15
    result = []
    y = 0
    for i in range(len(game_map)):
        x = 0
        ryadok = game_map[i]
        for block in ryadok:
            if block == "A":
                new_block = Block((100, 100, 100), math.ceil(x), y, 60, 60, "res/wall.png")
                result.append(new_block)
            x += SIZE
        y += SIZE
    return result