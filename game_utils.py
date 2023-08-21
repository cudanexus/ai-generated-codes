def check_collision(snake, food):
    return (snake.x < food.x + food.size and
            snake.x + snake.size > food.x and
            snake.y < food.y + food.size and
            snake.y + snake.size > food.y)
