from pygame import *

wind = display.set_mode((700,500))
display.set_caption('Ping-Pong')

COLOR = (0,255,0)
wx = 3
wy = 3

class GameS(sprite.Sprite):
    def __init__(self, cart, x, y, sx,sy,  speed):
        super().__init__()
        self.image = transform.scale(image.load(cart),(sx,sy))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        wind.blit(self.image,(self.rect.x, self.rect.y))

class Playr(GameS):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y < 415:
            self.rect.y +=self.speed
    def ypdute(self):
        keys = key.get_pressed()
        
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys[K_k] and self.rect.y < 415:
            self.rect.y +=self.speed

clock = time.Clock()
FPS = 60

baru = transform.scale(image.load('Fon.png'),(700,500))
pl1 = Playr('Leftpl.png',0,100,50,140,5)
pl2 = Playr('Rightpl.png',660,100,50,140,5)
shar = GameS('Shar.png',60, 100,80,80,3)

game = True
finish = False

font.init()
font = font.Font(None,35)
l1 = font.render('Игрок 1 Проиграл',True,(180,0,0))
l2 = font.render('Игрок 2 Проиграл',True,(180,0,0))

while game:
    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        wind.blit(baru,(0,0))
        pl1.reset()
        pl2.reset()
        shar.reset()
        shar.rect.x += wx
        shar.rect.y += wy

        if shar.rect.y < 0 or shar.rect.y > 450:
            wy *= -1
        if sprite.collide_rect(pl1,shar) or sprite.collide_rect(pl2,shar):
            wx *= -1
        if shar.rect.x < 0:
            finish = True
            wind.blit(l1,(200,200))
            game = False
        if shar.rect.x > 700:
            finish = True
            wind.blit(l2k,(200,200))
            game = False

        pl1.update()
        pl2.ypdute()
        
    clock.tick(FPS)
    display.update()

       
