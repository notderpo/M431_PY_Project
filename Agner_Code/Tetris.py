import random
import curses

# Set up the screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)  # Set the timeout for getch to 100 milliseconds

# Initialize the game variables
score = 0
key = curses.KEY_RIGHT
h, w = sh, sw
win = curses.newwin(h, w, 0, 0)
win.keypad(1)
win.timeout(100)

# Initial position of the snake
snake = [[1, 5], [1, 4], [1, 3]]
food = [sh // 2, sw // 2]

# Game logic
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calculate the new head of the snake based on the current key
    new_head = [snake[0][0], snake[0][1]]

    # Check if the snake has hit the wall or itself
    if (
        new_head[0] in [0, h]
        or new_head[1] in [0, w]
        or new_head in snake[1:]
    ):
        curses.endwin()
        quit()

    # Move the snake
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Check if the snake has eaten the food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, h - 1),
                random.randint(1, w - 1),
            ]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], "*")
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], " ")

    snake.insert(0, new_head)
    win.addch(snake[0][0], snake[0][1], "#")
