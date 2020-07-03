import pygame
pygame.init()
two = pygame.transform.scale(pygame.image.load("images/2.png"), (80,80))
four = pygame.transform.scale(pygame.image.load("images/4.png"), (80,80))
eight = pygame.transform.scale(pygame.image.load("images/8.png"), (80,80))
sixteen = pygame.transform.scale(pygame.image.load("images/16.png"), (80,80))
three2 = pygame.transform.scale(pygame.image.load("images/32.png"), (80,80))
six4 = pygame.transform.scale(pygame.image.load("images/64.png"), (80,80))
one28 = pygame.transform.scale(pygame.image.load("images/128.png"), (80,80))
two56 = pygame.transform.scale(pygame.image.load("images/256.png"), (80,80))
five12 = pygame.transform.scale(pygame.image.load("images/512.png"), (80,80))
one024 = pygame.transform.scale(pygame.image.load("images/1024.png"), (80,80))
two048 = pygame.transform.scale(pygame.image.load("images/2048.png"), (80,80))
four096 = pygame.transform.scale(pygame.image.load("images/4096.png"), (80,80))
eight192 = pygame.transform.scale(pygame.image.load("images/8192.png"), (80,80))
dict = {2:two,4:four,8:eight,16:sixteen,32:three2,64:six4,
        128:one28,256:two56,512:five12,1024:one024,2048:two048,
        4096:four096,8192:eight192}