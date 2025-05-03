from pygame import *
import random as rndm
import time as tm


mixer.init()
font.init()

window = display.set_mode((700, 500))
display.set_caption('Догонялки')

background = transform.scale(image.load('fon.jpg'), (700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=10, w = 65, h = 200):
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
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
    
    def update2(self):
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed


class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=10, w = 65, h = 200):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
        self.ball_x = self.speed
        self.ball_y = self.speed

    def update(self):
        self.rect.y -= self.ball_y
        self.rect.x -= self.ball_x

        if self.rect.x <= 0:
            self.ball_y *= -1

        if self.rect.x >= 500:
            self.ball_y *= -1

        if self.rect.x <= 50:
            self.ball_x *= -1

        if self.rect.x >= 550:
            self.ball_x *= -1


lost = 0

ded = 0

# kick.play()

FPS = 120

fps = FPS*2

fire_time = FPS/10

font1 = font.SysFont('Arial', 36)

enemy_z_ = []


p1 = Player('3.png', 50, 250)

p2 = Player('4.jpg', 550, 250)

b1 = Ball('2.jpg', 300, 250, 10, 50, 50)


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


    p1.reset()
    p1.update()

    p2.reset()
    p2.update2()

    b1.reset()
    b1.update()


    display.update()