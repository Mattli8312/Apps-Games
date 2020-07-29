import pygame, random, math
pygame.init()
width, height = 500, 400
Score, Lives = 0, 3
Levels = 0
Shapes = ["Images/Shape1.png","Images/Shape2.png"]
Quadrants = [[0,0],[0,height-100],[width-100,0],[width-100,height-100]]
class Rocks():
    def __init__(self,x,y,w,h,vel,ang):
        self.x,self.y = x,y
        self.w,self.h = w,h
        self.a,self.vel = ang, vel
        self.image = pygame.transform.scale(pygame.image.load(Shapes[random.randint(0,1)]).convert(),(w,h))
    def Generate(self,surf):
        self.Float()
        img = pygame.transform.rotozoom(self.image,self.a,1)
        img.set_colorkey((0,0,0))
        surf.blit(img, img.get_rect(center=(self.x,self.y)))
    def Float(self):
        if self.x < 0: self.x = width
        if self.x > width: self.x = 0
        if self.y < 0: self.y = height
        if self.y > height: self.y = 0
        self.y -= math.sin(self.a*math.pi/180) * self.vel
        self.x -= math.cos(self.a*math.pi/180) * self.vel
class Meteor():
    def __init__(self):
        self.boulders = []
        self.count = 2
        self.Reset()
    def Execute(self,surf):
        global Lives
        for b in self.boulders:
            b.Generate(surf)
        if len(self.boulders) <= 0:
            if self.count <= 10: self.count += 1
            if Lives < 6: Lives += 1
            self.Reset()
    def Reset(self):
        global Levels
        Levels += 1
        quad = Quadrants[random.randint(0,3)]
        for i in range(self.count):
            x = random.randint(0,100) + quad[0]
            y = random.randint(0,100) + quad[1]
            vel = random.randint(1, 2)
            angle = random.randint(0, 35)
            self.boulders.append(Rocks(x,y, 50, 50, vel, angle * 10))
    def Hit(self,bullets):
        global Score
        for b in bullets:
            for B in self.boulders:
                if b.x >= B.x - B.w//2 and b.x <= B.x + B.w//2:
                    if b.y >= B.y - B.h//2 and b.y <= B.y + B.h//2:
                        Score += B.w * 2
                        b.hit = True
                        self.Split(B)
        return bullets
    def Split(self, rock):
        self.boulders.pop(self.boulders.index(rock))
        if rock.w//2 > 10:
            self.boulders.append(Rocks(rock.x,rock.y,rock.w//2,rock.h//2,round(rock.vel*1.5),rock.a+10))
            self.boulders.append(Rocks(rock.x,rock.y,rock.w//2,rock.h//2,round(rock.vel*1.5),rock.a-10))