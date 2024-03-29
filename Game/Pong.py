import pygame
import random
import sys
import os

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.pad1 = pygame.Rect(20, 150, 20, 100)
        self.pad2 = pygame.Rect(560, 150, 20, 100)
        self.ball = pygame.Rect(290, 190, 20, 20)
        self.ball_speed_x = 5
        self.ball_speed_y = 5
        self.score1 = 0
        self.score2 = 0
        self.game_loop()
    
    def move_pad1_up(self):
        self.pad1.y -= 50

    def move_pad1_down(self):
        self.pad1.y += 50

    def move_pad2_up(self):
        self.pad2.y -= 50

    def move_pad2_down(self):
        self.pad2.y += 50

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_pad2_up()
                    elif event.key == pygame.K_DOWN:
                        self.move_pad2_down()
                    elif event.key == pygame.K_w:
                        self.move_pad1_up()
                    elif event.key == pygame.K_s:
                        self.move_pad1_down()

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 255, 0), self.pad1) # Edit the color of the pad1 (255,255,255) is white color
            pygame.draw.rect(self.screen, (255, 0, 255), self.pad2) # Edit the color of the pad2 (255,0,255) is purple color
            pygame.draw.ellipse(self.screen, (0, 255, 0), self.ball) # Edit the color of the ball (255,255,255) is white color
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            if self.ball.left <= 0:
                self.score2 += 1
            elif self.ball.right >= self.screen_width:
                self.score1 += 1

            if self.ball.top <= 0 or self.ball.bottom >= self.screen_height:
                self.ball_speed_y *= -1
            if self.ball.left <= 0 or self.ball.right >= self.screen_width:
                self.ball_speed_x *= -1

            if self.ball.colliderect(self.pad1) and self.ball_speed_x < 0:
                self.ball_speed_x *= -1
                self.ball.left = self.pad1.right
            if self.ball.colliderect(self.pad2) and self.ball_speed_x > 0:
                self.ball_speed_x *= -1
                self.ball.right = self.pad2.left

            self.display_scores()
            pygame.display.flip()
            self.clock.tick(60)

    def restart_game(self):
        self.ball.x = 290
        self.ball.y = 190
        self.ball_speed_x = random.choice([-5, 5])
        self.ball_speed_y = random.choice([-5, 5])
    
    def display_scores(self):
        font = pygame.font.Font(None, 36)
        score_text1 = font.render("Player 1: " + str(self.score1), True, (255, 255, 255))
        score_text2 = font.render("Player 2: " + str(self.score2), True, (255, 255, 255))
        self.screen.blit(score_text1, (10, 10))
        self.screen.blit(score_text2, (self.screen_width - 150, 10))
if __name__ == "__main__":
    game = PongGame()
