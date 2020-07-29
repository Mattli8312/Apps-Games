import pygame, random, math
pygame.init()
from Asteroids import Meteors
class Blaster():
    def __init__(self,x,y,a):
        self.x,self.y = x,y
        self.angle, self.vel = a, 3
        self.hit = False
    def Generate(self, surf):
        self.Fly()
        pygame.draw.circle(surf,(0,255,255),(round(self.x),round(self.y)),6)
        pygame.draw.circle(surf,(255,255,255),(round(self.x),round(self.y)),4)
    def Fly(self):
        if not(self.hit):
            self.y -= math.cos(self.angle*math.pi/180) * self.vel
            self.x -= math.sin(self.angle*math.pi/180) * self.vel
class Saucer():
    def __init__(self,w,h,name):
        self.x,self.y = random.randint(-1,0), random.randint(50,Meteors.height-50)
        self.w,self.h,self.lvl = w,h,2
        self.burst, self.fr = 0, 30
        self.bullets, self.hit = [], False
        self.vel = 2 if self.x == 0 else - 2
        self.image = pygame.transform.scale(pygame.image.load(name).convert(),(w,h))
        self.image.set_colorkey((0,0,0))
    def Execute(self,surf,player_1):
        if not(self.hit):
            self.Auto()
            self.Fire(player_1)
            surf.blit(self.image,(self.x,self.y))
        else:
            if Meteors.Levels >= self.lvl:
                self.hit = False
                self.lvl += 2
                if self.fr >= 15: self.fr -= 1
    def RapidFire(self,surf):
        for b in self.bullets: b.Generate(surf)
    def Auto(self):
        if self.x > Meteors.width: self.x = 0
        elif self.x<0: self.x = Meteors.width
        if self.y >= Meteors.height: self.y = 0
        elif self.y<0: self.y = Meteors.height
        self.x += self.vel
    def Fire(self, player1):
        self.burst += 1
        if self.burst >= self.fr:
            if self.y > player1.y:
                for i in range(3):
                    self.bullets.append(Blaster(self.x,self.y,random.randint(-1,1)*10))
            else:
                for i in range(3):
                    self.bullets.append(Blaster(self.x,self.y,random.randint(17,19)*10))
            self.burst = 0
        for b in self.bullets:
            if b.hit: self.bullets.pop(self.bullets.index(b))
    def Shot(self, bullets):
        for b in bullets:
            if b.x >= self.x and b.x <= self.x + self.w:
                if b.y >= self.y and b.y <= self.y + self.h:
                    b.hit = False
                    self.hit = True
                    Meteors.Score += 500
                    break
        return bullets
