import pygame
from game_objects import Snake, Food, BigFood
from game_utils import check_collision

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    big_food = None
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != pygame.K_DOWN:
                    snake.direction = pygame.K_UP
                elif event.key == pygame.K_DOWN and snake.direction != pygame.K_UP:
                    snake.direction = pygame.K_DOWN
                elif event.key == pygame.K_LEFT and snake.direction != pygame.K_RIGHT:
                    snake.direction = pygame.K_LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != pygame.K_LEFT:
                    snake.direction = pygame.K_RIGHT

        snake.update()
        if check_collision(snake, food):
            snake.grow = True  # Set grow flag
            score += 1
            food = Food()
            if score % 5 == 0:
                big_food = BigFood()

        if big_food and pygame.time.get_ticks() - big_food.timer > 10000:
            big_food = None

        if big_food and check_collision(snake, big_food):
            snake.grow = True  # Set grow flag
            score += 5
            big_food = None

        def draw_score(screen, score):
            font = pygame.font.Font(None, 36)
            text = font.render("Score: " + str(score), 1, (255, 255, 255))
            screen.blit(text, (0, 0))

        screen.fill((0, 0, 0))
        draw_score(screen, score)
        snake.draw(screen)
        food.draw(screen)
        if big_food:
            big_food.draw(screen)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
