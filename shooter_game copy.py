from pygame import *
import random as rndm
import time as tm


mixer.init()
font.init()

window = display.set_mode((700, 500))
display.set_caption('Догонялки')

background = transform.scale(image.load('fon.jpeg'), (700, 500))

ball = transform.scale(image.load('2.webp'), (50, 50))

raketka1 = transform.scale(image.load('3.png'), (50, 300))

raketka2 = transform.scale(image.load('4.jpg'), (50, 300))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=10, w = 65, h = 65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if keys_pressed[K_RIGHT] and self.ret.x < 600:
            self.rect.x += self.speed
        if keys_pressed[K_d] and self.rect.x < 600:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= -50:
            self.kill()


lost = 0

ded = 0

# kick.play()

FPS = 120

fps = FPS*2

fire_time = FPS/10

font1 = font.SysFont('Arial', 36)

enemy_z_ = []


text_lost_ufos = font1.render(
    'Пропущено: ' + str(lost), 1, (255, 255, 255)
)

text_ded_ufos = font1.render(
    'Заанигилировано: ' + str(ded), 1, (255, 255, 255)
)


game = True

game_process = True

while game:
    keys_pressed = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))

    display.update()