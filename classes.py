import pygame
import random

class MyClock:
    def __init__(self, fps):
        self.CLOCK = pygame.time.Clock()
        self.FPS = fps

    def tick(self):
        self.CLOCK.tick(self.FPS)

class Player(pygame.sprite.Sprite):
    def __init__(self, rectWidth, rectHeight, screenWidth, screenHeight, color=[0, 0, 0]):
        super().__init__()
        self.image = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, rectWidth, rectHeight), border_radius=10)
        self.rect = self.image.get_rect( center = (screenWidth / 2, screenHeight - 50) )

        self.SCREEN_WIDTH = screenWidth
        self.SPEED = 5
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.left -= self.SPEED

            if self.rect.left < 0:
                self.rect.left = 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.right += self.SPEED

            if self.rect.right > self.SCREEN_WIDTH:
                self.rect.right = self.SCREEN_WIDTH

class Block(pygame.sprite.Sprite):
    def __init__(self, rectWidth, rectHeight, screenWidth, screenHeight, color=[211, 211, 211]):
        super().__init__()

        x = score = random.randrange(rectWidth, screenWidth - rectWidth)

        self.image = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, rectWidth, rectHeight), border_radius=4)
        self.rect = self.image.get_rect( bottomleft = (x, 0) )

        score = random.randrange(5, 50, 5)

        font = pygame.font.Font('./fonts/Pixeltype.ttf', 40)
        text = font.render(str(score), False, 'black')
        textRect = text.get_rect( center = (rectWidth / 2, rectHeight / 2))

        self.image.blit(text, textRect)

        self.SCREEN_HEIGHT = screenHeight
        self.SPEED = 5

    def update(self):
        self.rect.bottom += self.SPEED

        if self.rect.top > self.SCREEN_HEIGHT:
            self.rect.bottom = 0

class Score:
    def __init__(self, default=50):
        self.makeScore(default)

        self.GAME_OVER = False
    
    def makeScore(self, score):
        font = pygame.font.Font('./fonts/Pixeltype.ttf', 40)
        self.text = font.render('Score: ' + str(score), False, 'black')
        self.textRect = self.text.get_rect( topleft = (20, 20))

    def draw(self, screen):
        screen.blit(self.text, self.textRect)