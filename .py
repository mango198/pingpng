import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the paddle class
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.speed = 7

    def draw(self):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < HEIGHT - self.height:
            self.y += self.speed

# Define the ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 10
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def draw(self):
        pygame.draw.circle(WIN, WHITE, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Ball collision with walls
        if self.y <= 0 or self.y >= HEIGHT:
            self.speed_y *= -1

# Create paddles and ball
player_paddle = Paddle(50, HEIGHT // 2 - 50)
computer_paddle = Paddle(WIDTH - 60, HEIGHT // 2 - 50)
ball = Ball()

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_paddle.move_up()
        if keys[pygame.K_DOWN]:
            player_paddle.move_down()

        # AI for computer paddle
        if ball.y < computer_paddle.y:
            computer_paddle.move_up()
        elif ball.y > computer_paddle.y + computer_paddle.height:
            computer_paddle.move_down()

        # Move the ball
        ball.move()

        # Check for collision with paddles
        if (ball.x - ball.radius <= player_paddle.x + player_paddle.width and
            player_paddle.y <= ball.y <= player_paddle.y + player_paddle.height):
            ball.speed_x *= -1

        if (ball.x + ball.radius >= computer_paddle.x and
            computer_paddle.y <= ball.y <= computer_paddle.y + computer_paddle.height):
            ball.speed_x *= -1

        # Clear the screen
        WIN.fill(BLACK)

        # Draw paddles and ball
        player_paddle.draw()
        computer_paddle.draw()
        ball.draw()

        # Update the display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
