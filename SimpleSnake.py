import random
import curses


# Create the screen and initialize some variables
screen = curses.initscr()
curses.curs_set(0)
screenheight, screenwidth = screen.getmaxyx()
options = curses.newwin(screenheight, screenwidth, 0, 0)
options.keypad(1)
options.timeout(100)

# Create initial x and y coordinates
y_coordinate = screenheight/2
x_coordinate = screenwidth/4
# Create the initial snake position
snake = [
    [y_coordinate, x_coordinate],
    [y_coordinate, x_coordinate-1],
    [y_coordinate, x_coordinate-2]
]

goal = [screenheight/2, screenwidth/2]
options.addch(int(goal[0]), int(goal[1]), curses.ACS_DIAMOND)

control = curses.KEY_RIGHT

while True:
    next_command = options.getch()
    control = control if next_command == -1 else next_command

    # Check to see if game over
    if snake[0][0] in [0, screenheight] or snake[0][1] in [0, screenwidth] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    refresh_head = [snake[0][0], snake[0][1]]

    # Check user input and move the snake
    if control == curses.KEY_DOWN:
        refresh_head[0] += 1
    if control == curses.KEY_UP:
        refresh_head[0] -= 1
    if control == curses.KEY_RIGHT:
        refresh_head[1] += 1
    if control == curses.KEY_LEFT:
        refresh_head[1] -= 1

    snake.insert(0, refresh_head)

    # Check if snake has eaten the goal
    if snake[0] == goal:
        goal = None
        while goal is None:
            # Create new goal
            newGoal = [
                random.randint(1, screenheight-1),
                random.randint(1, screenwidth-1)
            ]
            goal = newGoal if newGoal not in snake else None
        options.addch(goal[0], goal[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        options.addch(int(tail[0]), int(tail[1]), ' ')

    options.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)