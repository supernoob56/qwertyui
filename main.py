import pygame
import random
import constants
from models import Snake, Apple

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(constants.FONT_NAME, constants.FONT_SIZE)

window = pygame.display.set_mode(constants.WINDOW_SIZE)
pygame.display.set_caption("Snake")


def draw_score(score):
    score_text = font.render(f"SCORE: {score}", True, constants.WHITE)
    coordinates = (10, 10)

    window.blit(score_text, coordinates)


def render(snake, apple, score):

    window.fill(constants.BLACK)

    snake.draw_snake(window)
    apple.draw_apple(window)
    draw_score(score)

    pygame.display.update()


# šeit tiek izsaukta __init__ metode
snake = Snake(
    x=random.randint(0, constants.WIDTH - Snake.rectangle_size),
    y=random.randint(0, constants.HEIGHT - Snake.rectangle_size),
)

apple = Apple(
    x=random.randint(0, constants.WIDTH - Snake.rectangle_size),
    y=random.randint(0, constants.HEIGHT - Snake.rectangle_size),
)

score = 0

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                snake.x_change = 0
                snake.y_change = -snake.rectangle_size
            elif event.key == pygame.K_a:
                snake.x_change = -snake.rectangle_size
                snake.y_change = 0
            elif event.key == pygame.K_s:
                snake.x_change = 0
                snake.y_change = snake.rectangle_size
            elif event.key == pygame.K_d:
                snake.x_change = snake.rectangle_size
                snake.y_change = 0
            
    snake.move_snake()

    if snake.is_outside_screen(window) or snake.is_crossing_itself():
        pygame.quit()

    head = snake.get_first_rectangle()
    if apple.is_eaten(head):
        snake.length += 1

        apple.rectangle.left = random.randint(0, constants.WIDTH - Snake.rectangle_size)
        apple.rectangle.top = random.randint(0, constants.HEIGHT - Snake.rectangle_size) 

        score += 1

    render(snake, apple, score)
    clock.tick(constants.FPS)