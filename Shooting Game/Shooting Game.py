"""
    Turtle Graphics - Shooting Game
"""

import turtle

"""
    Constants and variables
"""

# General parameters
window_height = 600
window_width = 600
window_margin = 50
update_interval = 25    # The screen update interval in ms, which is the
                        # interval of running the updatescreen function

# Player's parameters
player_size = 50        # The size of the player image plus margin
player_init_x = 0
player_init_y = -window_height / 2 + window_margin
player_speed = 10       # The speed the player moves left or right

# Enemy's parameters
enemy_number = 2        # The number of enemies in the game

enemy_size = 50         # The size of the enemy image plus margin
enemy_init_x = -window_width / 2 + window_margin
enemy_init_y = window_height / 2 - window_margin
enemy_min_x = enemy_init_x
enemy_max_x = window_width / 2 - enemy_size * enemy_number
    # The maximum x coordinate of the first enemy, which will be used
    # to restrict the x coordinates of all other enemies
enemy_hit_player_distance = 30
    # The player will lose the game if the vertical
    # distance between the enemy and the player is smaller
    # than this value

# Enemy movement parameters
enemy_speed = 2
enemy_speed_increment = 1
    # The increase in speed every time the enemies move
    # across the window and back
enemy_direction = 1
    # The current direction the enemies are moving:
    #     1 means from left to right and
    #     -1 means from right to left

# The list of enemies
enemies = []

# Laser parameter
laser_width = 2
laser_height = 15
laser_speed = 20
laser_hit_enemy_distance = 20
    # The laser will destory an enemy if the distance
    # between the laser and the enemy is smaller than
    # this value

"""
    Handle the player movement
"""

# This function is run when the "Left" key is pressed. The function moves the
# player to the left when the player is within the window area
def playermoveleft():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range

    player.goto(x - player_speed, y)

    turtle.update() # delete this line after finishing updatescreen()

# This function is run when the "Right" key is pressed. The function moves the
# player to the right when the player is within the window area
def playermoveright():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range

    player.goto(x + player_speed, y)

    turtle.update() # delete this line after finishing updatescreen()

"""
    Handle the screen update and enemy movement
"""

# This function is run in a fixed interval. It updates the position of all
# elements on the screen, including the player and the enemies. It also checks
# for the end of game conditions.
def updatescreen():
    # Use the global variables here because we will change them inside this
    # function
    global enemy_direction, enemy_speed

    # Move the enemies depending on the moving direction

    # The enemies can only move within an area, which is determined by the
    # position of enemy at the top left corner, enemy_min_x and enemy_max_x

    # x and y displacements for all enemies
    dx = enemy_speed
    dy = 0

    # Part 3.3
    # Perform several actions if the enemies hit the window border

        # Switch the moving direction

        # Bring the enemies closer to the player

        # Increase the speed when the direction switches to right again

    # Move the enemies according to the dx and dy values determined above
    for enemy in enemies:
        x, y = enemy.position()
        enemy.goto(x + dx, y + dy)

    # Part 4.3 - Moving the laser
    # Perfrom several actions if the laser is visible

    if laser.isvisible():
        # Move the laser

        # Hide the laser if it goes beyong the window

        # Check the laser against every enemy using a for loop
        for enemy in enemies:
            # If the laser hits a visible enemy, hide both of them

                # Stop if some enemy is hit
                break

    # Part 5.1 - Gameover when one of the enemies is close to the player

    # If one of the enemies is very close to the player, the game will be over
    for enemy in enemies:
        if enemy.ycor()-player.ycor() < enemy_hit_player_distance:
            # Show a message
            gameover("You lose!")

            # Return and do not run updatescreen() again
            return

    # Part 5.2 - Gameover when you have killed all enemies

    # Set up a variable as a counter

    # For each enemy

        # Increase the counter if the enemy is visible

    # If the counter is 0, that means you have killed all enemies

        # Perform several gameover actions

    # Part 3.1 - Controlling animation using the timer event

    #
    # Add code here
    #

"""
    Shoot the laser
"""

# This function is run when the player presses the spacebar. It shoots a laser
# by putting the laser in the player's current position. Only one laser can
# be shot at any one time.
def shoot():

    print("Pyoo!") # delete this line after completing the function

    # Part 4.2 - the shooting function
    # Shoot the laser only if it is not visible

    #
    # Add code here
    #

"""
    Game start
"""
# This function contains things that have to be done when the game starts.
def gamestart():
    # Use the global variables here because we will change them inside this
    # function
    global player, laser

    ### Player turtle ###

    # Add the spaceship picture
    turtle.addshape("spaceship.gif")

    # Create the player turtle and move it to the initial position
    player = turtle.Turtle()
    player.shape("spaceship.gif")
    player.up()
    player.goto(player_init_x, player_init_y)

    # Part 2.1
    # Map player movement handlers to key press events

    #
    # Add code here
    #

    ### Enemy turtles ###

    # Add the enemy picture
    turtle.addshape("enemy.gif")

    for i in range(enemy_number):
        # Create the turtle for the enemy
        enemy = turtle.Turtle()
        enemy.shape("enemy.gif")
        enemy.up()

        # Move to a proper position counting from the top left corner
        enemy.goto(enemy_init_x + enemy_size * i, enemy_init_y)

        # Add the enemy to the end of the enemies list
        enemies.append(enemy)

    ### Laser turtle ###

    # Create the laser turtle using the square turtle shape
    laser = turtle.Turtle()
    laser.shape("square")
    laser.color("White")

    # Change the size of the turtle and change the orientation of the turtle
    laser.shapesize(laser_width / 20, laser_height / 20)
    laser.left(90)
    laser.up()

    # Hide the laser turtle
    laser.hideturtle()

    # Part 4.2 - Mapping the shooting function to key press event

    #
    # Add code here
    #

    turtle.update()

    # Part 3.1 - Controlling animation using the timer event

    #
    # Add code here
    #


"""
    Game over
"""

# This function shows the game over message.
def gameover(message):

    # Part 5.3 - Improving the gameover() function

    print(message) # delete this line after completing the function

"""
    Set up main Turtle parameters
"""

# Set up the turtle window
turtle.setup(window_width, window_height)
turtle.bgcolor("Black")
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Start the game
gamestart()

# Switch focus to turtle graphics window
turtle.done()