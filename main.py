import pygame, sort, random

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
anzahl_balken = 100

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

class Balken():
    def __init__(self, x, height = screen_height/anzahl_balken * 0.5, color = "white"):
        self.width = screen_width/anzahl_balken - 1
        self.height = (screen_height-10)/anzahl_balken * height
        self.x = x * screen_width/anzahl_balken
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, screen_height - self.height, self.width, self.height))

    def activate(self):
        if self.color == "white":
            self.color = "red"
        else:
            self.color = "white"

lst = list(range(1, anzahl_balken+1))
random.shuffle(lst)
balkenList = [Balken(x, height) for x, height in enumerate(lst, 1)]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # limits FPS to 60
    dt = clock.tick(60) / 1000

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for balken in balkenList:
        balken.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()




pygame.quit()