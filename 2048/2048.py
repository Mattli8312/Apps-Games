import pygame
pygame.init()
from TwentyFourtyEightGame import TilesTFE
import random
class Fonts():
  def __init__(self, x, y, size, txt, color):
    self.x = x
    self.y = y
    self.t = txt
    self.c = color
    self.f = pygame.font.SysFont("Calibri", size, True)
  def write(self, surf):
    text = self.f.render(self.t, False, self.c)
    surf.blit(text, (self.x, self.y))
class tiles():
  def __init__(self, x, y, val):
    self.x = x
    self.y = y
    self.v = val
  def draw(self, surf):
    self.image = TilesTFE.dict[self.v]
    surf.blit(self.image, (self.x, self.y))
def update(dir):
  global grid, score
  delta = [0,0,0,0]
  if dir == "d":
    for i in range(3, -1, -1):
      for j in range(3, -1, -1):
        if grid[i][j] != 0:
          if delta[i] > 0 and grid[i][j] == grid[i][4-delta[i]]:
            grid[i][4-delta[i]] += grid[i][j]
            score += grid[i][4-delta[i]]
            grid[i][j] = 0
          else:
            if 3-delta[i] != j:
              grid[i][3-delta[i]] = grid[i][j]
              grid[i][j] = 0
            delta[i] += 1
  elif dir == "a":
    for i in range(0, 4, 1):
      for j in range(0, 4, 1):
        if grid[i][j] != 0:
          if delta[i] > 0 and grid[i][j] == grid[i][delta[i] - 1]:
            grid[i][delta[i] - 1] += grid[i][j]
            score += grid[i][delta[i] - 1]
            grid[i][j] = 0
          else:
            if delta[i] != j:
              grid[i][delta[i]] = grid[i][j]
              grid[i][j] = 0
            delta[i] += 1
  elif dir == "w":
    for i in range(0, 4, 1):
      for j in range(0, 4, 1):
        if grid[j][i] != 0:
          if delta[i] > 0 and grid[j][i] == grid[delta[i] - 1][i]:
            grid[delta[i] - 1][i] += grid[j][i]
            score += grid[delta[i] - 1][i]
            grid[j][i] = 0
          else:
            grid[delta[i]][i] = grid[j][i]
            if delta[i] != j:
              grid[j][i] = 0
            delta[i] += 1
  elif dir == "s":
    for i in range(3, -1, -1):
      for j in range(3, -1, -1):
        if grid[j][i] != 0:
          if delta[i] > 0 and grid[j][i] == grid[4 - delta[i]][i]:
            grid[4 - delta[i]][i] += grid[j][i]
            score += grid[4-delta[i]][i]
            grid[j][i] = 0
          else:
            grid[3 - delta[i]][i] = grid[j][i]
            if 3 - delta[i] != j:
              grid[j][i] = 0
            delta[i] += 1
def adder():
  global grid, Lost
  cc = []
  for i in range(4):
    for j in range(4):
      cc.append([i,j])
  select = False
  while not(select):
    num = random.randint(0, len(cc) - 1)
    if grid[cc[num][0]][cc[num][1]] == 0:
      grid[cc[num][0]][cc[num][1]] = 2
      select = True
    else:
      cc.pop(num)
      if len(cc) <= 0:
        select = True
        Lost = True
def drawgrid(surf):
  global grid
  blocks = []
  for i in range(4):
    for j in range(4):
      if grid[i][j] != 0:
        blocks.append(tiles(i * 90 + 25, j * 90 + 225, grid[i][j]))
  x = 20
  y = 220
  pygame.draw.rect(surf, (170,160,150), (20,220, 360,360))
  for i in range(5):
    pygame.draw.line(surf, (160,150,140), (x, 220), (x, 580), 10)
    pygame.draw.line(surf, (160,150,140), (20, y), (380, y), 10)
    x += 90
    y += 90
  for b in blocks:
    b.draw(surf)
def lostground(surf):
  global tax, tay
  G_O = Fonts(80,300, 50, "Game Over", (0,0,0))
  G_O.write(surf)
  T_A = Fonts(175, 360, 15, "Try again", (255,255,255))
  pygame.draw.rect(surf, (50,50,50), (167, 350, tax, tay))
  T_A.write(surf)
def background(surf):
  global score, scr_w, scr_x, scr_c, ngx, ngy
  if score >= scr_c:
    scr_x -= 5
    scr_w += 5
    scr_c *= 100
  title = Fonts(25,25,75,"2048",(110,100,100))
  sub_script = Fonts(25,175,15, "Join the numbers and get to the 2048 tile!", (50,50,50))
  Score_script = Fonts(scr_x + scr_w//4, 35, 15, "Score", (255,255,255))
  Score = Fonts(scr_x + 0.9*scr_w//2, 60, 15, str(score), (255,255,255))
  NewGame = Fonts(305, 170, 15, "New Game", (255,255,255))
  pygame.draw.rect(surf, (110,100,100), (scr_x, 30, scr_w, 50))
  pygame.draw.rect(surf, (50,50,50), (300, 170, ngx, ngy))
  title.write(surf)
  sub_script.write(surf)
  Score_script.write(surf)
  Score.write(surf)
  NewGame.write(surf)
def interface():
  global grid, score, scr_w, scr_x, scr_c, Lost, ngx, ngy, tax, tay
  score = 0
  scr_w = 70
  scr_x = 300
  scr_c = 100
  ngx , ngy = 80, 20
  tax, tay = 70, 50
  grid = [[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  win = pygame.display.set_mode((400, 600))
  Lost = False
  run = True
  while run:
      win.fill((250,245,240))
      drawgrid(win)
      background(win)
      for event in pygame.event.get():
          pos = pygame.mouse.get_pos()
          if event.type == pygame.QUIT:
              run = False
          if pos[0] >= 300 and pos[0] <= 380 and pos[1] >= 170 and pos[1] <= 190:
              ngx, ngy = 100, 30
              if event.type == pygame.MOUSEBUTTONDOWN:
                score = 0
                grid = [[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
          else:
            ngx, ngy = 80, 20
          if pos[0] >= 167 and pos[0] <= 237 and pos[1] >= 350 and pos[1] <= 400:
            tax , tay = 80, 60
            if event.type == pygame.MOUSEBUTTONDOWN:
              Lost = False
              score = 0
              grid = [[2,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
          else:
            tax, tay = 70, 50
      if not(Lost):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
          update("w")
          adder()
          pygame.time.delay(250)
        elif keys[pygame.K_RIGHT]:
          update("s")
          adder()
          pygame.time.delay(250)
        elif keys[pygame.K_UP]:
          update("a")
          adder()
          pygame.time.delay(250)
        elif keys[pygame.K_DOWN]:
          update("d")
          adder()
          pygame.time.delay(250)
      else:
        lostground(win)
      pygame.display.update()
  pygame.quit()
interface()