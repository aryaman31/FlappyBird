import sys, pygame, random
pygame.init()
pygame.mixer.init()

# Variables
trackfps = 0
fallv = 1
pressed = False
score = 0
gameSpeed = 1

# Defs
def imp(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

# Iniitialise
size = w,h = 450,600
fps = 60
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flying box")
clock = pygame.time.Clock()

# Colors
black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,193,7

# Classes
class pipesTop(pygame.sprite.Sprite):
    def __init__(self,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,height))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = w
        
    def update(self):
        global running, score
        self.rect.x -= 3 * gameSpeed
        if self.rect.right < 0:
            allSprites.remove(self)

        for p in players:
            if p.rect.top < self.rect.bottom:
                if p.rect.right > self.rect.left:
                    if p.rect.left < self.rect.right:
                        running = False
            if p.rect.left == self.rect.right:
                score += 1

class pipesBot(pygame.sprite.Sprite):
    def __init__(self,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,h-(height+150)))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.bottom = h
        self.rect.left = w

    def update(self):
        global running
        self.rect.x -= 3 * gameSpeed
        if self.rect.right < 0:
            allSprites.remove(self)
        
        for p in players:
            if p.rect.bottom > self.rect.top:
                if p.rect.right > self.rect.left:
                    if p.rect.left < self.rect.right:
                        running = False

class birds(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = w/2,h/2

    def update(self):
        global fallv, pressed, running
        fallv -= 1
        keys = pygame.key.get_pressed()
        if not(keys[pygame.K_SPACE]):
            pressed = False
        if keys[pygame.K_SPACE] and not(pressed):
            pressed = True
            fallv = 12
        self.rect.y -= fallv

        if self.rect.top > h:
            running = False
        

# Sprite Stuff
allSprites = pygame.sprite.Group()
players = pygame.sprite.Group()

bird = birds()
allSprites.add(bird)
players.add(bird)

# Game Loop
running = True
start = False
while running:
    # Processing
    trackfps += 1
    clock.tick(fps)
    running = imp(running)
    # Update
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True
    if trackfps % 60 == 0 and start:
        height = random.randint(200,h-200)
        pipe = pipesTop(height)
        allSprites.add(pipe)

        pipe = pipesBot(height)
        allSprites.add(pipe)
    if start:
        allSprites.update() 
    
    # Draw
    screen.fill(black)
    allSprites.draw(screen) 
    pygame.display.flip()

print(score)
pygame.quit()


