# snake_Game
In main.py, all the Python source files are imported and used together like a single unified module. This file handles the core game logic, including conditions such as collisions with walls, the snake’s tail, or food.

In snake.py, the snake's body is created along with functions to control its movement (up, down, left, right) and increase its length when food is eaten.

In food.py, a food object is generated that appears at random locations within the screen boundaries.

In scoreboard.py, the scoreboard is implemented to update the score whenever the snake eats food. It also tracks and displays the high score.

In data.txt, the high score is saved so that it persists even after restarting the game. This file is read and updated through functions in scoreboard.py.
