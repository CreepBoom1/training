#MODULES
from pygame import *
from map import *
#MUSIC AND COUNTERS
mixer.init()
init()
health = 3
tcount = 0
mixer.music.load("res/dungeon.mp3")
mixer.music.set_volume(0.1)
mixer.music.play()
money = mixer.Sound("res/money.ogg")
hurt = mixer.Sound("res/hurt.ogg")
hurt
#BG
window = display.set_mode((800, 800))
BACKGROUND_COLOR = (255, 0, 100)
window.fill(BACKGROUND_COLOR)
clock = time.Clock()
game = True


background_image = transform.scale(
    image.load('res/background.png'), (800, 800))

#ACTIVE
class Sprite:

    def __init__(self, image_name, x, y, width, height):
        self.image = transform.scale(
                image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction = 'right'
#MOVEMENT
    def move(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w]:
            self.rect.y -=5
        if pressed_keys[K_s]:
            self.rect.y += 5
        if pressed_keys[K_a]:
            self.rect.x -= 5
            if self.direction == 'right':
                self.direction = 'left'
                self.flip()
        if pressed_keys[K_d]:
            self.rect.x += 5
            if self.direction == 'left':
                self.direction = 'right'
                self.flip()

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def flip(self):
        self.image = transform.flip(self.image, True, False)
    def auto_move(self, x1, x2):
        if self.rect.x <= x1 or self.rect.x + self.rect.width > x2:
            self.speed *= -1
            self.flip()
        self.rect.x += self.speed

    def is_collide(self,sprite):
        return self.rect.colliderect(sprite.rect)
    def wall_collide(self,walls):
        pressed_keys = key.get_pressed()
        for wall in walls:
            if self.is_collide(wall):
                if pressed_keys[K_w]:
                    self.rect.y += 5
                if pressed_keys[K_s]:
                    self.rect.y -= 5
                if pressed_keys[K_a]:
                    self.rect.x += 5
                if pressed_keys[K_d]:
                    self.rect.x -= 5
#CHARACTERS
player = Sprite("res/player.png", 60,60,50,70)
enemy = Sprite("res/enemy3.png", 680,680,60,80)
enemy2 = Sprite("res/ghost.png", 300, 350, 50, 50)
treasure = Sprite("res/treasure.png", 400, 400, 70, 70)
health1 = Sprite("res/health.png", 0, -35, 150, 150)
health2 = Sprite("res/health.png", 50, -35, 150, 150)
health3 = Sprite("res/health.png", 100, -35, 150, 150)
tcount1 = Sprite("res/notreasure.png", 200, 7, 50, 50)
tcount2 = Sprite("res/notreasure.png", 250, 7, 50, 50)
tcount3 = Sprite("res/notreasure.png", 300, 7, 50, 50)
#GAME CYCLE
game_map = make_map()
while game:
    window.blit(background_image, (0, 0))
    for e in event.get():
        pressed_keys = key.get_pressed()
        if e.type == QUIT or pressed_keys[K_ESCAPE]:
            game = False
#WIN AND LOSS
    if player.is_collide(enemy) or player.is_collide(enemy2):
        player.image_name = "res/death.png"
        health -= 1
        hurt.play()
        time.wait(1000)
        player.rect.x = 60
        player.image_name = "res/player.png"
        player.rect.y = 60

    #TREASURE COUNT
    if tcount == 0:
        if player.is_collide(treasure):
            tcount += 1
            money.play()
            treasure.rect.x = enemy.rect.x
            treasure.rect.y = enemy.rect.y
    if tcount == 1:
        tcount1 = Sprite("res/treasure.png", 190, -1, 63, 63)
        if player.is_collide(treasure):
            tcount += 1
            money.play()
            treasure.rect.x = 60
            treasure.rect.y = 600
    if tcount == 2:
        tcount2 = Sprite("res/treasure.png", 240, -1, 63, 63)
        if player.is_collide(treasure):
            tcount += 1
            money.play()
            treasure.rect.x = 60
            treasure.rect.y = 500
    if tcount == 3:
        tcount3 = Sprite("res/treasure.png", 290, -1, 63, 63)
        text = font.SysFont("Freesansbold", 200).render("You won!", True, (0, 153, 0))
        window.blit(text, (80, 350))
        game = False
        display.update()
        time.wait(5000)
    for block in game_map:
        block.draw(window)
    #LOSS
    if health == 2:
        health3 = Sprite("res/nohealth.png", 100, -37, 150, 150)
    if health == 1:
        health2 = Sprite("res/nohealth.png", 50, -37, 150, 150)
    if health == 0:
        text = font.SysFont("Freesansbold", 200).render("You lost!", True, (201, 38, 38))
        window.blit(text, (80, 350))
        game = False
        display.update()
        time.wait(5000)
    #DRAW AND MOVEMENT IMPLEMENTATION
    player.move()
    player.draw()
    enemy.draw()
    enemy2.draw()
    enemy2.auto_move(200, 500)
    enemy.auto_move(100, 750)
    treasure.draw()
    health1.draw()
    health2.draw()
    health3.draw()
    tcount1.draw()
    tcount2.draw()
    tcount3.draw()
    player.wall_collide(game_map)
    display.update()
    clock.tick(60)
