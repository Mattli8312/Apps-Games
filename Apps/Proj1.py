import pygame
import random
gsf = 1
pygame.init()
winx = 380
winy = 460
win = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("PacMan")
clock = pygame.time.Clock()
#Scoreboard
pygame.font.init()
Font = pygame.font.SysFont('Ariel', 25, True)
#Pacmans
L = (pygame.transform.scale(pygame.image.load('L.jpg'), (15, 15)))
R = (pygame.transform.scale(pygame.image.load('R.jpg'), (15, 15)))
U = (pygame.transform.scale(pygame.image.load('U.jpg'), (15, 15)))
D = (pygame.transform.scale(pygame.image.load('D.jpg'), (15, 15)))
closed = pygame.transform.scale(pygame.image.load('Closed.jpg'), (15, 15))
t_mouth = 0
m_open = L
class block:
    def __init__(self, x, y, w, h):
        self.x = x * 20
        self.y = y * 20
        self.w = w * 20
        self.h = h * 20
        self.vel = 2
    def Pacman(self, win):
        global t_mouth, m_open
        pacs = [m_open, closed]
        win.blit(pacs[t_mouth//5], (self.x, self.y))
        t_mouth += 1
        if t_mouth >= 10:
            t_mouth = 0
    def drawall(self, win):
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.w, self.h))
class Pellet:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def circle(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.r)
class Mobs:
    def __init__(self, x, y, w, h, name, direction):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.direction = direction
        self.name = name
        self.vel = 2 * gsf
    def draw(self, win):
        self.image = pygame.transform.scale(pygame.image.load(self.name), (self.w, self.h))
        win.blit(self.image, (self.x, self.y))
    def move(self, win):
        if self.direction == 1:
            self.x -= self.vel
        elif self.direction == 2:
            self.x += self.vel
        elif self.direction == 3:
            self.y -= self.vel
        elif self.direction == 4:
            self.y += self.vel
    def hitbox(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.w, self.h), 1)
    def changedir(self, win):
        if self.direction == 1:
            self.x += self.vel
            self.direction = random.randint(3, 4)
        elif self.direction == 2:
            self.x -= self.vel
            self.direction = random.randint(3, 4)
        elif self.direction == 4:
            self.y -= self.vel
            self.direction = random.randint(1, 2)
        else:
            self.y += self.vel
            self.direction = random.randint(1, 2)
#Borders
w1 = block(0, 0, 19, 1)
w2 = block(18, 0, 1, 7)
w3 = block(15, 6, 4, 1)
w4 = block(15, 6, 1, 4)
w5 = block(15, 9, 4, 1)
w6 = block(15, 11, 4, 1)
w7 = block(15, 11, 1, 4)
w8 = block(15, 14, 4, 1)
w9 = block(18, 14, 1, 9)
w10 = block(17, 18, 2, 1)
w11 = block(0, 22, 19, 1)
w12 = block(0, 14, 1, 9)
w13 = block(0, 18, 2, 1)
w14 = block(0, 14, 4, 1)
w15 = block(3, 11, 1, 4)
w16 = block(0, 11, 4, 1)
w17 = block(0, 9, 4, 1)
w18 = block(3, 6, 1, 4)
w19 = block(0, 6, 4, 1)
w20 = block(0, 0, 1, 7)
w21 = block(9, 0, 1, 3)
#internal borders
w22 = block(2, 2, 2, 1)
w23 = block(5, 2, 3, 1)
w24 = block(11, 2, 3, 1)
w25 = block(15, 2, 2, 1)
w26 = block(2, 4, 2, 1)
w27 = block(5, 4, 1, 6)
w28 = block(5, 6, 3, 1)
w29 = block(7, 4, 5, 1)
w30 = block(9, 4, 1, 3)
w31 = block(13, 4, 1, 6)
w32 = block(11, 6, 3, 1)
w33 = block(15, 4, 2, 1)
w34 = block(7, 8, 2, 1)
w35 = block(10, 8, 2, 1)
w36 = block(7, 8, 1, 5)
w37 = block(11, 8, 1, 5)
w38 = block(7, 12, 5, 1)
w39 = block(5, 11, 1, 4)
w40 = block(13, 11, 1, 4)
w41 = block(7, 14, 5, 1)
w42 = block(9, 14, 1, 3)
w43 = block(5, 16, 3, 1)
w44 = block(11, 16, 3, 1)
w45 = block(2, 16, 2, 1)
w46 = block(3, 16, 1, 3)
w47 = block(15, 16, 2, 1)
w48 = block(15, 16, 1, 3)
w49 = block(7, 18, 5, 1)
w50 = block(9, 18, 1, 3)
w51 = block(5, 18, 1, 3)
w52 = block(2, 20, 6, 1)
w53 = block(13, 18, 1, 3)
w54 = block(11, 20, 6, 1)
walls = (w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12,
         w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23,
         w24, w25, w26, w27, w28, w29, w30, w31, w32, w33, w34,
         w35, w36, w37, w38, w39, w40, w41, w42, w43, w44, w45,
         w46, w47, w48, w49, w50, w51, w52, w53, w54)
run = True
collide = False
#PacmanControls
direction = 'Left'
left = True
right = True
up = True
down = True
#Status
complete = False
reset = True
game_run = True
timer = 0
timedial = False
while run:
    # window
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Generating Pellets
    if reset or complete:
        if reset:
            Lives = 3
            Score = 0
            gsf = 1
        Pellets = []
        px = 30
        py = 30
        for P in Pellets:
            Pellets.pop(Pellets.index(P))
        while py < winy - 20:
            while px < winx - 20:
                Pellets.append(Pellet(px, py, 3))
                px += 20
            px = 30
            py += 20
        reset = False
        complete = False
    #keys
    keys = pygame.key.get_pressed()
    # Stuff
    icon = block(9, 17, 0.75, 0.75)
    # Ghosts
    Blinky = Mobs(120, 140, 15, 15, 'Blinky.jpg', 2)
    Pinky = Mobs(120, 260, 15, 15, 'Pinky.jpg', 1)
    Inky = Mobs(240, 140, 15, 15, 'Inky.jpg', 2)
    Clyde = Mobs(240, 260, 15, 15, 'Clyde.jpg', 1)
    Ghosts = [Blinky, Pinky, Inky, Clyde]
    while not(collide) and run and not(complete) and not(timedial) and game_run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((0, 0, 0))
        ScoreBoard = Font.render("Score: " + str(Score), True, (255, 255, 255))
        Liveboard = Font.render("Lives: " + str(Lives), True, (255, 255, 255))
        icon.Pacman(win)
        #Level Complete
        if len(Pellets) <= 0:
            complete = True
        #Ghost Controls
        for g in Ghosts:
            g.draw(win)
            g.move(win)
            if g.x > icon.x and g.x < icon.x + icon.w:
                if g.y > icon.y and g.y < icon.y + icon.h:
                    collide = True
            if g.x + g.w > icon.x and g.x + g.w < icon.x + icon.w:
                if g.y > icon.y and g.y < icon.y + icon.h:
                    collide = True
            if g.x > icon.x and g.x < icon.x + icon.w:
                if g.y + g.h > icon.y and g.y + g.h < icon.y + icon.h:
                    collide = True
            if g.x + g.w > icon.x and g.x + g.w < icon.x + icon.w:
                if g.y + g.h > icon.y and g.y + g.h < icon.y + icon.h:
                    collide = True
        #Ghost Stabilization
        for wall in walls:
            for g in Ghosts:
                if g.x + 2 > wall.x and g.x + 2 < wall.x + wall.w:
                    if g.y + 2 > wall.y and g.y + 2 < wall.y + wall.h:
                        g.changedir(win)
                if g.x + g.w - 2 > wall.x and g.x + g.w - 2 < wall.x + wall.w:
                    if g.y + 2 > wall.y and g.y + 2 < wall.y + wall.h:
                        g.changedir(win)
                if g.x + 2 > wall.x and g.x + 2 < wall.x + wall.w:
                    if g.y + g.h - 2 > wall.y and g.y + g.h - 2 < wall.y + wall.h:
                        g.changedir(win)
        # walls
        for wall in walls:
            wall.drawall(win)
        # Pellets
        for P in Pellets:
            P.circle(win)
        # Extraneous Pellets
        for wall in walls:
            for P in Pellets:
                if P.x > wall.x and P.x < wall.x + wall.w:
                    if P.y > wall.y and P.y < wall.y + wall.h:
                        Pellets.pop(Pellets.index(P))
                elif P.x > 0 and P.x < 80 or P.x > 100 and P.x < 280 or P.x > 300 and P.x < winx:
                    if P.y > 120 and P.y < 300:
                        Pellets.pop(Pellets.index(P))
        # Overlap ScoreBoard
        win.blit(ScoreBoard, (0, 0))
        win.blit(Liveboard, (0, 440))
        #Eaten Pellets
        for P in Pellets:
            if P.x > icon.x - 10 and P.x < icon.x + icon.w + 10:
                if P.y > icon.y - 10 and P.y < icon.y + icon.h + 10:
                    Score += 10
                    Pellets.pop(Pellets.index(P))
        #controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = 'Left'
            right = True
            down = True
            up = True
            m_open = L
        if keys[pygame.K_RIGHT]:
            direction = 'Right'
            left = True
            up = True
            down = True
            m_open = R
        if keys[pygame.K_UP]:
            direction = 'Up'
            down = True
            left = True
            right = True
            m_open = U
        if keys[pygame.K_DOWN]:
            direction = 'Down'
            up = True
            left = True
            right = True
            m_open = D
        #movement
        if direction == 'Left' and left:
            icon.x -= icon.vel
        if direction == 'Right' and right:
            icon.x += icon.vel
        if direction == 'Up' and up:
            icon.y -= icon.vel
        if direction == 'Down' and down:
            icon.y += icon.vel
        #wall Boundaries
        for wall in walls:
            if icon.x > wall.x and icon.x < wall.x + wall.w:
                if icon.y > wall.y and icon.y < wall.y + wall.h:
                    Bump = True
                    if direction == 'Left':
                        left = False
                        icon.x += 2
                    elif direction == 'Right':
                        right = False
                        icon.x -= 2
                    elif direction == 'Up':
                        up = False
                        icon.y += 2
                    else:
                        down = False
                        icon.y -= 2
            if icon.x + icon.w > wall.x and icon.x + icon.w < wall.x + wall.w:
                if icon.y + icon.h > wall.y and icon.y + icon.h < wall.y + wall.h:
                    Bump = True
                    if direction == 'Left':
                        left = False
                        icon.x += 5
                    elif direction == 'Right':
                        right = False
                        icon.x -= 5
                    elif direction == 'Up':
                        up = False
                        icon.y += 5
                    else:
                        down = False
                        icon.y -= 5
            if icon.x + icon.w > wall.x and icon.x + icon.w < wall.x + wall.w:
                if icon.y > wall.y and icon.y < wall.y + wall.h:
                    Bump = True
                    if direction == 'Left':
                        left = False
                        icon.x += 5
                    elif direction == 'Right':
                        right = False
                        icon.x -= 5
                    elif direction == 'Up':
                        up = False
                        icon.y += 5
                    else:
                        down = False
                        icon.y -= 5
            if icon.x > wall.x and icon.x < wall.x + wall.w:
                if icon.y + icon.h > wall.y and icon.y + icon.h < wall.y + wall.h:
                    Bump = True
                    if direction == 'Left':
                        left = False
                        icon.x += 5
                    elif direction == 'Right':
                        right = False
                        icon.x -= 5
                    elif direction == 'Up':
                        up = False
                        icon.y += 5
                    else:
                        down = False
                        icon.y -= 5
        #teleport
        if icon.x + icon.w > winx:
            icon.x = 5
        if icon.x < 0:
            icon.x = winx - 20
        pygame.display.update()
    if collide:
        Lives -= 1
        collide = False
    if timer <= 30:
        timer += 1
        timedial = True
    else:
        timer = 0
        timedial = False
    if Lives < 0:
        game_run = False
        win.fill((0, 0, 0))
        Font1 = pygame.font.SysFont('Calibri', 30, True)
        text = Font1.render("You're out of lives :(.", True,  (255, 255, 255))
        text_2 = Font1.render("Press Space to retry", True,  (255, 255, 255))
        win.blit(text, (0, 0,))
        win.blit(text_2, (0, 100))
    keys = pygame.key.get_pressed()
    if complete:
        gsf += 0.2
    if keys[pygame.K_SPACE] and Lives < 0:
        game_run = True
        reset = True
    pygame.display.update()
pygame.quit()