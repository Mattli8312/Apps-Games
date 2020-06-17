import pygame
import random
pygame.init()
clock = pygame.time.Clock()
fr = 0
amount = 2
Style = pygame.font.SysFont('Calibri', 20, True)
class sprite():
    def __init__(self, x, y, w, h, color, name, vel):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.name = name
        self.health = 100
        self.vel = vel
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, 20, 10))
        pygame.draw.rect(win, self.color, (self.x + 8, self.y - 10, 4, 20))
    def manual(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= 10
        elif keys[pygame.K_RIGHT] and self.x < width - self.w:
            self.x += 10
    def auto(self):
        if self.y > 0 and self.y < height:
            self.y += self.vel
    def ball(self, win):
        pygame.draw.circle(win, self.color, (self.x - 10, self.y), 3)
class stone():
    def __init__(self, x, y, w, h, color, health):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.size = round(self.w * 0.8)
        self.velx = random.randint(-2, 2)
        self.vel = 0
        self.health = health
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))
    def gravity(self):
        if self.y + self.h < height - 25:
            self.y += self.vel
            self.vel += 0.5
        else:
            self.vel *= -1
            self.vel += 1
            self.y += self.vel
    def healthbar(self, win):
        font = pygame.font.SysFont('Ariel', round(self.size), True)
        text = font.render(str(self.health), False, (255, 255, 255))
        win.blit(text, (self.x + 5, self.y + 5))
    def bounce(self):
        if self.x + self.w < width and self.x > 0:
            self.x += self.velx
        else:
            self.velx *= -1
            self.x += self.velx
def fire(player, surf, bullet):
    global fr, keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        fr += 1
    if fr >= 5:
        fr = 0
        bullet.append(sprite(player.x + 23, player.y, 5, 10, (0,0,0), 0, -20))
    for a in bullet:
        a.ball(surf)
        a.auto()
        if a.y <= 0:
            bullet.pop(bullet.index(a))
def boulders(bullets, surf, rocks, player):
    global scr, amount
    if len(rocks) < amount:
        luck = random.randint(0, 3)
        if luck == 3:
            rocks.append(stone(random.randint(20, 150), 0, 50, 50, (255, 128, 0), 100))
        else:
            rocks.append(stone(random.randint(20, 150),0,30,30,(0,0,0), 50))
    for rock in rocks:
        if rock.health > 0 and rock.y < height:
            rock.draw(surf)
            rock.healthbar(surf)
            rock.gravity()
            rock.bounce()
        else:
            rocks.pop(rocks.index(rock))
        for b in bullets:
            if b.x > rock.x and b.x < rock.x + rock.w:
                rock.w *= 0.9
                rock.h *= 0.9
                scr += rock.health
                rock.size = round(rock.size * 0.85)
                rock.health -= 10
                bullets.pop(bullets.index(b))
        if player.x > rock.x and player.x < rock.x + rock.w:
            if player.y > rock.y and player.y < rock.y + rock.h:
                player.health -= rock.health//10
def reset(rocks, Player):
    global amount, scr, Lvl
    amount = 2
    scr = 0
    Lvl = 1000
    for rock in rocks:
        rocks.pop(rocks.index(rock))
    Player.health = 100
def main():
    global width, height, bullet, scr, amount
    run = True
    width, height = 200, 400
    scr = 0
    Final_scr = 0
    Lvl = 1000
    win = pygame.display.set_mode((width, height))
    Player = sprite(width//2 - 25, height - 50, 20, 50, 0, 'GravityCannonImages\SpaceShip.png', 0)
    bullet = []
    rocks = []
    size = 20
    MainFont = pygame.font.SysFont('bahnschrift', 40, True)
    subFont = pygame.font.SysFont('Calibri', 15, True)
    RuleFont = pygame.font.SysFont('Calibri', 12, True)
    title = MainFont.render("Gravity", False, (0,0,0))
    subtitle = MainFont.render('Cannon', False, (0,0,0))
    StartButton = subFont.render("'Press space to play'", False, (0,0,0))
    RuleButton = subFont.render("'Press h for rules'", False, (0,0,0))
    rules = RuleFont.render("1. use left and right arrows to move", False, (0,0,0))
    rules2 = RuleFont.render("2. use space to fire at incoming rocks", False, (0,0,0))
    rules3 = RuleFont.render("3. if blocks hit you, you lose health", False, (0,0,0))
    Death1 = MainFont.render("You", False, (0,0,0))
    Death2 = MainFont.render("Have", False, (0,0,0))
    Death3 = MainFont.render("Died", False, (0,0,0))
    AgainButton = subFont.render("Press space to play again", False, (0,0,0))
    mainpage = True
    rulepage = False
    deathpage = False
    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            mainpage = False
            deathpage = False
            rulepage = False
        if keys[pygame.K_h]:
            rulepage = True
            mainpage = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if mainpage:
            win.fill((255,255,255))
            win.blit(title, (20, 60))
            win.blit(subtitle, (20, 100))
            win.blit(StartButton, (35, 200))
            win.blit(RuleButton, (35, 220))
            pygame.display.update()
        elif rulepage:
            win.blit(rules, (10, 240))
            win.blit(rules2, (10, 260))
            win.blit(rules3, (10, 280))
            pygame.display.update()
        elif deathpage:
            FinalScore = subFont.render("Score: " + str(Final_scr), False, (0, 0, 0))
            reset(rocks, Player)
            win.fill((255,255,255))
            win.blit(Death1, (50, 60))
            win.blit(Death2, (50, 100))
            win.blit(Death3, (50, 140))
            win.blit(FinalScore, (60, 200))
            win.blit(AgainButton, (20, 240))
            pygame.display.update()
        else:
            clock.tick(30)
            Final_scr = scr
            win.fill((255, 255, 255))
            Scoreboard = Style.render("Score: " + str(scr), False, (0, 0, 0))
            Healthboard = Style.render("Health" + str(Player.health), False, (0,0,0))
            win.blit(Scoreboard, (0,0))
            win.blit(Healthboard, (0,height - 20))
            pygame.draw.line(win, (0, 0, 0), (0, height - 25), (width, height - 25), 2)
            Player.draw(win)
            Player.manual()
            #Firing
            fire(Player, win, bullet)
            #Rock
            boulders(bullet, win, rocks, Player)
            #Score
            if scr > Lvl:
                Lvl *= 2
                amount += 1
            #Health
            if Player.health <= 0:
                deathpage = True
            pygame.display.update()
    pygame.quit()
main()