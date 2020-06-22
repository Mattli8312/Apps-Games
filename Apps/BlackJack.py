import pygame
import random
pygame.init()
clock = pygame.time.Clock()
class Font():
    def __init__(self, size, bold, text, color):
        self.name = 'banchschrift'
        self.size = size
        self.bold = bold
        self.t = text
        self.c = color
    def create(self, surf, x,y ):
        self.font = pygame.font.SysFont(self.name, self.size, self.bold)
        self.text = self.font.render(self.t, False, self.c)
        surf.blit(self.text, (x,y))
class cards():
    def __init__(self, x, y, val, suit, color, worth):
        self.x = x
        self.y = y
        self.c = color
        self.v = val
        self.n = worth
        self.f1 = Font(20, True, str(val), self.c)
        self.f2 = pygame.transform.scale(pygame.image.load(suit), (15, 15))
    def face_up(self, win):
        white = (255, 255, 255)
        pygame.draw.rect(win, white, (self.x, self.y, 40, 80))
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, 40, 80), 3)
        self.f1.create(win, self.x + 5, self.y)
        win.blit(self.f2, (self.x + 5,self.y + 20))
    def face_down(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, 40, 80))
        pygame.draw.rect(win,(255,255,255), (self.x, self.y, 40, 80), 3)
class buttons():
    def __init__(self, x, y, w, h, txt, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = Font(30, True, txt, (0,0,0))
        self.c = color
        self.c1 = color
    def drawbutton(self, win):
        pygame.draw.rect(win, self.c,(self.x, self.y, self.w, self.h))
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.w, self.h), 3)
        self.t.create(win, self.x + 5, self.y + 5)
    def touching(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.w:
            if pos[1] > self.y and pos[1] < self.y + self.h:
                self.c = (255,255,255)
                return True
            else:
                self.c = self.c1
                return False
        else:
            self.c = self.c1
            return False
def reset():
    global deck, hand_cash, counter
    hand_cash = 5000
    counter = 51
    while len(deck) > 0:
        deck.pop(0)
def build_deck():
    global deck
    deck = []
    while len(deck) > 0:
        deck.pop(0)
    values = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
    suits = ('BlackJack/Hearts.jpg', 'BlackJack/Diamonds.jpg', 'BlackJack/Spades.jpg', 'BlackJack/Clubs.jpg')
    color = (255,0,0)
    for i in range(len(suits)):
        if i > 1: color = (0,0,0)
        for j in range(len(values)):
            deck.append(cards(20, 20,values[j],suits[i],color,j+1))
def HIT(win, hand, x, y, p):
    global deck, counter, p_hand_val, p_dis, b_hand_val
    num = random.randint(0, counter)
    hand.append(deck[num])
    deck[num].y = y
    if(deck[num].v == 'J') or (deck[num].v == 'Q') or (deck[num].v == 'K'):
        if p:
            deck[num].x = x + p_dis
            p_hand_val += 10
        else:
            deck[num].x = x + b_dis
            b_hand_val += 10
    elif deck[num].v == 'A':
        if p:
            if p_hand_val < 11:
                p_hand_val += 11
            else:
                p_hand_val += 1
            deck[num].x = x + p_dis
        else:
            if b_hand_val < 11:
                b_hand_val += 11
            else:
                b_hand_val += 1
            deck[num].x = x + b_dis
    else:
        if p:
            deck[num].x = x + p_dis
            p_hand_val += deck[num].n
        else:
            deck[num].x = x + b_dis
            b_hand_val += deck[num].n
    deck.pop(num)
    counter -= 1
def start(win):
    global player_hand, bot_hand, p_dis, b_dis
    p_dis = 0
    b_dis = 0
    while len(player_hand) > 0:
        player_hand.pop(0)
    while len(bot_hand) > 0:
        bot_hand.pop(0)
    for i in range(2):
        HIT(win, player_hand, width//2 - 40, height-100, True)
        HIT(win, bot_hand, width//2-40, 50, False)
        p_dis += 20
        b_dis += 20
def mainPage(surf, b1, b2, b3, b4):
    surf.blit(b1, (0, 0))
    surf.blit(b2, (width // 2 - 100, 40))
    b3.drawbutton(surf)
    b4.drawbutton(surf)
def rulePage(surf, b1, b2):
    surf.blit(b1, (0, 0))
    b2.drawbutton(surf)
    white = (255,255,255)
    words = ["Rules", "Objective", "1. Get to 21 without going over",
             "2. Try to beat the dealer", "Card Values", "1. A = 1 or 11",
             "2. Face cards = 10", "3. Other cards equal card value",
             "Moveset", "1.Hit: Draw card from the deck", "2.Stand: End turn",
             "3.Double-Down: raise bet by, at most, initial bet"]
    sizes = [40, 30, 20, 20, 30, 20, 20, 20, 30, 20, 20, 20]
    y = 10
    for i in range(len(words)):
        Text = Font(sizes[i], True, words[i], white)
        Text.create(surf, 10, y)
        y += sizes[i]
def modePage(surf, b0, b1,b2,b3):
    surf.blit(b0, (0,0))
    b1.drawbutton(surf)
    b2.drawbutton(surf)
    b3.drawbutton(surf)
def gamePage(surf, b1, deck, player_hand, bot_hand, hitter, standing, DD, QUIT, list):
    global hit, set, bet, hand_cash, bet_value, stand, p_dis, b_dis, compare
    global p_hand_val, b_hand_val, BetRatio, DoubleDown
    surf.blit(b1, (0, 0))
    Currency = buttons(0, height // 1.5, 150, 30, "Cash: " + str(hand_cash), (255,0,0))
    Betting = buttons(0, height//1.3, 150, 30, "Bet: " + str(bet_value), (0, 128, 255))
    Currency.drawbutton(surf)
    Betting.drawbutton(surf)
    txt = "Make a bet"
    Winner = Font(50, True, txt, (255,255,255))
    sign_timer = 120
    for d in deck:
        d.face_down(surf)
    if not(bet):
        hitter.drawbutton(surf)
        standing.drawbutton(surf)
        DD.drawbutton(surf)
        QUIT.drawbutton(surf)
        if set:
            start(surf)
            set = False
        if hit:
            HIT(surf, player_hand, width//2-40, height-100, True)
            p_dis += 20
            hit = False
        elif DoubleDown:
            HIT(surf, player_hand, width//2-40, height-100, True)
            stand = True
            bet_value *= 2
            DoubleDown = False
        elif stand:
            if b_hand_val <= 12:
                HIT(surf, bot_hand, width//2 - 40, 50, False)
                b_dis += 20
                pygame.time.delay(500)
            else:
                pygame.time.delay(500)
                compare = True
                stand = False
        elif compare:
            if p_hand_val == 21 and b_hand_val != 21:
                hand_cash += bet_value * BetRatio
                print("BlackJack!")
            elif b_hand_val == 21 or b_hand_val < 21 and b_hand_val > p_hand_val or p_hand_val > 21 and b_hand_val < 21:
                hand_cash -= bet_value
                print("Dealer won")
            elif p_hand_val < 21 and p_hand_val > b_hand_val or b_hand_val > 21 and p_hand_val < 21:
                hand_cash += bet_value
                print("You Won!")
            else:
                print("Tie")
            pygame.time.delay(3000)
            print(len(deck))
            compare = False
            bet = True
        for i in range(len(bot_hand)):
            if i == 0:
                if not(compare):
                    bot_hand[i].face_down(surf)
                else:
                    bot_hand[i].face_up(surf)
            else:
                bot_hand[i].face_up(surf)
        for p in player_hand:
            p.face_up(surf)
    else:
        p_hand_val = 0
        b_hand_val = 0
        Winner.create(surf, width // 2, height // 2)
        for l in list:
            l.drawbutton(surf)
def interface():
    global width, height, counter, deck, player_hand, p_hand_val, hit, set, pos
    global bet, hand_cash, bet_value, stand, b_hand_val, bot_hand, p_dis, b_dis, compare
    global BetRatio, DoubleDown
    width = 500
    height = 400
    win = pygame.display.set_mode((width, height))
    mainbackground = pygame.transform.scale(pygame.image.load('BlackJack/Background.jpg'), (width, height))
    gamebackground = pygame.transform.scale(pygame.image.load('BlackJack/PlayingBoard.jpg'), (width, height))
    rulebackground = pygame.transform.scale(pygame.image.load('BlackJack/RuleBoard.jpg'), (width, height))
    pygame.display.set_caption("BlackJack")
    player_hand = []
    bot_hand = []
    run = True
    main = True
    play = False
    rule = False
    mode = False
    hit = False
    stand = False
    DoubleDown = False
    compare = False
    set = True
    bet = True
    counter = 51
    build_deck()
    p_hand_val = 0
    b_hand_val = 0
    hand_cash = 5000
    bet_value = 0
    BetRatio = 0
    Title = pygame.transform.scale(pygame.image.load('BlackJack/Title.png'), (200, 150))
    StartButton = buttons(width//2 - 50, height//2, 100, 60, "PLAY", (0,255,0))
    RuleButton = buttons(width//2 - 50, height//2 + 80, 100, 60, "Rules", (0, 255, 0))
    BackButton = buttons(width - 100, 0, 100, 60, "Back", (0, 255, 0))
    EasyButton = buttons(width // 2 - 100, height // 10, 200, 100, "Easy (3:2)", (0, 255, 255))
    MeadButton = buttons(width // 2 - 100, height // 10 + 120, 200, 100, "Medium (5:4)", (255, 128, 0))
    HardButton = buttons(width // 2 - 100, height // 10 + 240, 200, 100, "Hard (6:5)", (255, 0, 0))
    HitButton = buttons(width-100, height//2, 80, 40, "Hit", (0,255,0))
    StandButton = buttons(width-100, height//2 + 50, 80, 40, "Stand", (255,0,0))
    DDownButton = buttons(width-100, height//2 + 100, 80, 40, "Ddown", (0,128,255))
    QUIT = buttons(width - 100, 0, 100, 40, "QUIT", (255, 0, 0))
    Hundred = buttons(20, height - 60, 100, 40, "100", (255, 0, 255))
    Tundred = buttons(130, height-60, 100, 40, "200", (128, 255, 13))
    Thundred = buttons(240, height-60, 100, 40, "300", (255, 128, 0))
    Frundred = buttons(350, height-60, 100, 40, "400", (0, 255, 255))
    Betbuttons = (Hundred, Tundred, Thundred, Frundred)
    while run:
        clock.tick(30)
        keys = pygame.key.get_pressed()
        if main:
            mainPage(win, mainbackground, Title, StartButton, RuleButton)
        elif play:
            gamePage(win, gamebackground, deck, player_hand, bot_hand, HitButton, StandButton, DDownButton, QUIT, Betbuttons)
        elif rule:
            rulePage(win, rulebackground, BackButton)
        elif mode:
            modePage(win, mainbackground, EasyButton, MeadButton, HardButton)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            pos = pygame.mouse.get_pos()
            pressed = pygame.MOUSEBUTTONDOWN
            if main:
                if StartButton.touching(pos) and event.type == pressed:
                    main = False
                    mode = True
                elif RuleButton.touching(pos) and event.type == pressed:
                    main = False
                    rule = True
            elif rule:
                if BackButton.touching(pos) and event.type == pressed:
                    rule = False
                    main = True
            elif mode:
                if EasyButton.touching(pos) and event.type == pressed:
                    play = True
                    mode = False
                    BetRatio = 1.5
                elif MeadButton.touching(pos) and event.type == pressed:
                    play = True
                    mode = False
                    BetRatio = 1.25
                elif HardButton.touching(pos) and event.type == pressed:
                    play = True
                    mode = False
                    BetRatio = 1.2
            elif bet:
                vals = (100, 200, 300, 400)
                for i in range(len(Betbuttons)):
                    if Betbuttons[i].touching(pos) and event.type == pressed:
                        bet_value = vals[i]
                        bet = False
                        set = True
            elif play:
                if HitButton.touching(pos) and event.type == pressed:
                    hit = True
                elif StandButton.touching(pos) and event.type == pressed:
                    stand = True
                elif DDownButton.touching(pos) and event.type == pressed:
                    DoubleDown = True
                elif QUIT.touching(pos) and event.type == pressed:
                    play = False
                    reset()
                    build_deck()
                    main = True
                    bet = True
        pygame.display.update()
    pygame.quit()
interface()