import pygame, math
from Asteroids import Meteors, Alien_Ships
pygame.init()
class Fonts():
    def __init__(self,x,y,size,txt,style,color):
        self.x,self.y = x,y
        self.f = pygame.font.SysFont(style,size,True)
        self.text = self.f.render(txt,False,(color))
    def Generate(self,surf):
        surf.blit(self.text, (self.x,self.y))
class Triangles():
    def __init__(self,x,y):
        self.x,self.y = x,y
        self.image = pygame.transform.scale(pygame.image.load("Images/Lives.png").convert(),(20,20))
        self.image.set_colorkey((0,0,0))
    def Generate(self,surf):
        surf.blit(self.image, (self.x,self.y))
class Bullets():
    def __init__(self,x,y,angle):
        self.x,self.y = x,y
        self.hit = False
        self.a,self.vel = angle, 15
    def Draw(self,surf):
        self.Auto()
        pygame.draw.circle(surf,(0,0,128),(round(self.x),round(self.y)),10)
        pygame.draw.circle(surf,(255,255,255), (round(self.x),round(self.y)), 6)
    def Auto(self):
        if self.x > 0 and self.x < Meteors.width:
            self.x -= self.vel*math.sin(self.a*math.pi/180)
        else: self.hit = True
        if self.y > 0 and self.y < Meteors.height:
            self.y -= self.vel*math.cos(self.a*math.pi/180)
        else: self.hit = True
class Ships():
    def __init__(self,x,y,w,h,name,key):
        self.x,self.y = x,y
        self.w,self.h = w,h
        self.fr, self.c = 5,4
        self.k, self.ammo = key, []
        self.lives, self.alive = [], True
        for i in range(Meteors.Lives):
            self.lives.append(Triangles((i)*20+5,30))
        self.a = self.vel = 0
        self.image = pygame.transform.scale(pygame.image.load(name).convert(), (self.w, self.h))
    def Generate(self,surf):
        self.Manual()
        self.Update_Lives()
        if len(self.lives) <= 0: self.alive = False
        img = pygame.transform.rotozoom(self.image,self.a,1)
        img.set_colorkey(self.k)
        for a in self.ammo:
            a.Draw(surf)
            if a.hit: self.ammo.pop(self.ammo.index(a))
        for l in self.lives:
            l.Generate(surf)
        surf.blit(img, img.get_rect(center=(self.x,self.y)))
    def Update_Lives(self):
        if len(self.lives) != Meteors.Lives:
            if len(self.lives) < Meteors.Lives: self.lives.append(Triangles(self.lives[len(self.lives)-1].x+20,30))
            else: self.lives.pop(len(self.lives)-1)
    def Manual(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.c += 1
            if self.c >= self.fr and len(self.ammo) < 5:
                self.ammo.append(Bullets(self.x,self.y,self.a))
                self.c = 0
        if keys[pygame.K_LEFT]: self.a += 10
        elif keys[pygame.K_RIGHT]: self.a -= 10
        if keys[pygame.K_UP]:
            self.Acceleration(0)
        elif keys[pygame.K_DOWN]:
            self.Acceleration(1)
        else: self.Acceleration(2)
        self.y -= math.cos(self.a * math.pi / 180) * self.vel
        self.x -= math.sin(self.a * math.pi / 180) * self.vel
        if self.x < 0: self.x = Meteors.width
        if self.x > Meteors.width: self.x = 0
        if self.y < 0: self.y = Meteors.height
        if self.y > Meteors.height: self.y = 0
    def Acceleration(self,gear):
        if gear == 0:
            if self.vel <= 10: self.vel += 1
        elif gear == 1:
            if self.vel >= -10: self.vel -= 1
        else:
            if self.vel > 0: self.vel -= 0.5
            elif self.vel < 0: self.vel += 0.5
    def Collide(self, Boulder):
        for b in Boulder.boulders:
            if b.x >= self.x - self.w//2 and b.x <= self.x + self.w//2:
                if b.y >= self.y - self.h//2 and b.y <= self.y + self.h//2:
                    Meteors.Lives -= 1
                    self.x, self.y = Meteors.width//2, Meteors.height//2
    def Shot(self,NPC):
        for b in NPC.bullets:
            if b.x >= self.x - self.w//2 and b.x <= self.x + self.w//2:
                if b.y >= self.y - self.h//2 and b.y <= self.y + self.h//2:
                    Meteors.Lives -= 1
                    self.x, self.y = Meteors.width//2, Meteors.height//2
def GamePage(surf):
    Scoreboard = Fonts(10,10,15,str(Meteors.Score),"comicsansms",(0,255,255))
    Scoreboard.Generate(surf)
def Menu(surf):
    Title = Fonts(120,100,50,("Asteroids"),"Bahnschrift",(0,255,255))
    Button = Fonts(150,180,15,("Press Space to play"), "Courier", (0,255,255))
    Title.Generate(surf)
    Button.Generate(surf)
def main():
    win = pygame.display.set_mode((Meteors.width,Meteors.height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids")
    mp = run = True
    player_1 = Ships(Meteors.width // 2, Meteors.height // 2, 20, 20, "Images/Shooter.png", (0, 0, 0))
    NPC = Alien_Ships.Saucer(30,15,"Images/AlienShip.png")
    NPC_respawnLv = 1
    Boulder = Meteors.Meteor()
    while run:
        clock.tick(30)
        win.fill((0,0,0))
        if mp: Menu(win)
        else:
            GamePage(win)
            player_1.Generate(win)
            NPC.Execute(win,player_1)
            NPC.RapidFire(win)
            Boulder.Execute(win)
            player_1.ammo = Boulder.Hit(player_1.ammo)
            player_1.ammo = NPC.Shot(player_1.ammo)
            player_1.Collide(Boulder)
            player_1.Shot(NPC)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mp = False
        pygame.display.update()
    pygame.quit()
main()