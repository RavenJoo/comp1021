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
enemy_max_x = window_width / 2 - enemy_size * 6
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

    # Player should only be moved only if it is within the window range
    if x - player_speed > -window_width / 2 + window_margin:
        player.goto(x - player_speed, y)


# This function is run when the "Right" key is pressed. The function moves the
# player to the right when the player is within the window area
def playermoveright():

    # Get current player position
    x, y = player.position()

    # Player should only be moved only if it is within the window range
    if x + player_speed < window_width / 2 - window_margin:
        player.goto(x + player_speed, y)


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
    dx = enemy_speed * enemy_direction
    dy = 0

    # Perform several actions if the enemies hit the window border
    x0 = enemies[0].xcor()
    if x0 + dx > enemy_max_x or x0 + dx < enemy_min_x:
        # Switch the moving direction
        enemy_direction = -enemy_direction

        # Bring the enemies closer to the player
        dy = -enemy_size / 2

        # Increase the speed when the direction switches to right again
        if enemy_direction == 1:
            enemy_speed = enemy_speed + enemy_speed_increment

    # Move the enemies according to the dx and dy values determined above
    for enemy in enemies:
        x, y = enemy.position()
        enemy.goto(x + dx, y + dy)

        # Set up alternating enemy image
        if (x//20)%2 == 0:
            enemy.shape("enemy.gif")
        else:
            enemy.shape("enemy2.gif")
        
    # Perfrom several actions if the laser is visible

    if laser.isvisible():
        # Move the laser
        x, y = laser.position()
        laser.goto(x, y + laser_speed)

        # Hide the laser if it goes beyong the window
        if laser.ycor() > window_height / 2:
            laser.hideturtle()

        # Check the laser against every enemy using a for loop
        for enemy in enemies:
            # If the laser hits a visible enemy, hide both of them
            if enemy.isvisible() and laser.distance(enemy) < laser_hit_enemy_distance:
                enemy.hideturtle()
                laser.hideturtle()
                # Stop if some enemy is hit
                break

    # If one of the enemies is very close to the player, the game will be over
    for enemy in enemies:
        if enemy.ycor()-player.ycor() < enemy_hit_player_distance and enemy.isvisible():
            # Show a message
            gameover("You lose!")

            # Return and do not run updatescreen() again
            return

    # Set up a variable as a counter
    count = 0

    # For each enemy
    for enemy in enemies:
        # Increase the counter if the enemy is visible
        if enemy.isvisible():
            count = count + 1

    # If the counter is 0, that means you have killed all enemies
    if count == 0:
        # Perform several gameover actions
        gameover("You win!")

    # Update the screen
    turtle.update()

    # Schedule the next screen update
    turtle.ontimer(updatescreen, update_interval)

"""
    Shoot the laser
"""

# This function is run when the player presses the spacebar. It shoots a laser
# by putting the laser in the player's current position. Only one laser can
# be shot at any one time.
def shoot():

    # Shoot the laser only if it is not visible
    if not laser.isvisible():
        # Make the laser to become visible
        laser.showturtle()
        
        # Move the laser to the position of the player
        laser.goto(player.pos())

"""
    Game start
"""
# This function contains things that have to be done when the game starts.
def gamestart(x, y):
    start_button.clear()
    start_button.hideturtle()

    labels.clear()
    enemy_number_text.clear()
    left_arrow.hideturtle()
    right_arrow.hideturtle()
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

    # Map player movement handlers to key press events

    turtle.onkeypress(playermoveleft, "Left")
    turtle.onkeypress(playermoveright, "Right")
    turtle.listen()

    ### Enemy turtles ###

    # Add the enemy picture
    turtle.addshape("enemy.gif")
    turtle.addshape("enemy2.gif")

    for i in range(enemy_number):
        # Create the turtle for the enemy
        enemy = turtle.Turtle()
        enemy.shape("enemy.gif")
        enemy.up()

        # Move to a proper position counting from the top left corner
        enemy.goto(enemy_init_x + enemy_size * (i % 6), enemy_init_y - enemy_size * (i // 6))

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

    turtle.onkeypress(shoot, "space")

    turtle.update()

    # Start the game by running updatescreen()
    turtle.ontimer(updatescreen, update_interval)


"""
    Game over
"""

# This function shows the game over message.
def gameover(message):

    # Part 5.3 - Improving the gameover() function
    goturtle = turtle.Turtle()
    goturtle.hideturtle()
    goturtle.pencolor("yellow")
    goturtle.write(message, align="center", font=("System", 30, "bold"))
    turtle.update()

"""
    Set up main Turtle parameters
"""

# Set up the turtle window
turtle.setup(window_width, window_height)
turtle.bgcolor("Black")
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Spinner control initialization
labels = turtle.Turtle()
labels.hideturtle()
labels.pencolor("White")
labels.up()
# Write the text
labels.goto(-100, 0) # Next to the spinner control
labels.write("Number of Enemies:", font=("System", 12, "bold"))
# Value display
enemy_number_text = turtle.Turtle()
enemy_number_text.hideturtle()
enemy_number_text.pencolor("White")
enemy_number_text.up()
enemy_number_text.goto(80, 0)
enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
# Left arrow
left_arrow = turtle.Turtle()
left_arrow.up()
left_arrow.shape("arrow")
left_arrow.color("White")
left_arrow.shapesize(0.5, 1)
left_arrow.left(180)
left_arrow.goto(60, 8)
def decrease_enemy_number(x, y):
    # Declare enemy_number as global
    global enemy_number
    if enemy_number > 1:
        enemy_number = enemy_number - 1
        enemy_number_text.clear()
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
left_arrow.onclick(decrease_enemy_number)
left_arrow.showturtle()
# Right arrow
right_arrow = turtle.Turtle()
right_arrow.up()
right_arrow.shape("arrow")
right_arrow.color("White")
right_arrow.shapesize(0.5, 1)
right_arrow.goto(100, 8)
def increase_enemy_number(x, y):
    # Declare enemy_number as global
    global enemy_number
    if enemy_number < 48:
        enemy_number = enemy_number + 1
        enemy_number_text.clear()
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
right_arrow.onclick(increase_enemy_number)

# Start button initialization
start_button = turtle.Turtle()
start_button.up()
start_button.goto(-40, -40)
# Set up button graphics
start_button.color("White", "DarkGray")
start_button.begin_fill()
for _ in range(2):
    start_button.forward(80)
    start_button.left(90)
    start_button.forward(25)
    start_button.left(90)
start_button.end_fill()
start_button.color("White")
start_button.goto(0, -35)
start_button.write("Start", font=("System", 12, "bold"), align = "center")
# Make the turtle clickable with the same size as the graphics
start_button.goto(0, -28)
start_button.shape("square")
start_button.shapesize(1.25, 4)
start_button.color("")
start_button.onclick(gamestart)

turtle.update()

# Switch focus to turtle graphics window
turtle.done()
