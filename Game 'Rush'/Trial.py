import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers.
 
# Initialize the pygame modules to get everything started.
pygame.init()
 
# declaring a variable and creating the screen width
screen_width = 800
# declaring a variable and creating the screen height
screen_height = 600
# delcaring a variable and setting the screens width and height
screen = pygame.display.set_mode((screen_width ,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# delcaring a variable and uploading the background to the game window
background = pygame.image.load('stars.jpg').convert()
# setting a caption for the game window
pygame.display.set_caption("Rush")
# delcaring a variable and setting the icon for the game window
icon = pygame.image.load('thunder.png')
# displaying the icon for the game window
pygame.display.set_icon(icon)

#  declaring a variable and uploading the player image
player = pygame.image.load("spaceship.png")
# declaring a variable and uploading the enemy image
enemy1 = pygame.image.load("enemy.png")
# declaring a variable and uploading the enemy image
enemy2 = pygame.image.load("enemy.png")
# declaring a variable and uploading the enemy image
enemy3 = pygame.image.load("enemy.png")
# declaring a variable and uploading the enemy image
enemy4 = pygame.image.load('enemy.png')
# declaring a variable and uploading the prize image
prize  = pygame.image.load("thunder.png")

# declaring a variable and setting the players height
image_height = player.get_height()
# declaring a variable and setting the players width
image_width = player.get_width()
# declaring a variable and setting the enemys height
enemy1_height = enemy1.get_height()
# declaring a variable and setting the enemys width
enemy1_width = enemy1.get_width()
# declaring a variable and setting the enemys height
enemy2_height = enemy2.get_height()
# declaring a variable and setting the enemys width
enemy2_width = enemy2.get_width()
# declaring a variable and setting the enemys height
enemy3_height = enemy3.get_height()
# declaring a variable and setting the enemys width
enemy3_width = enemy3.get_width()
# declaring a variable and setting the enemys height
enemy4_height = enemy4.get_height()
# declaring a variable and setting the enemys width
enemy4_width = enemy4.get_width()
# declaring a variable and setting the prizes height
prize_height = prize.get_height()
# declaring a variable and setting the prizes width
prize_width = prize.get_width()

# print statement and converting and integer using the str() function
print("This is the height of the player image: " +str(image_height))
# print statement and converting and integer using the str() function
print("This is the width of the player image: " +str(image_width))

# declaring a variable and storing the players X position
playerXPosition = 100
#  declaring a variable and storing the players Y position
playerYPosition = 50

# declaring a variable and storing the enemys X position
enemy1XPosition = screen_width
# declaring a variable and storing the enmys Y position
enemy1YPosition = random.randint(0, screen_height - enemy1_height)
# declaring a variable and storing the enemys X position
enemy2XPosition = screen_width
# declaring a variable and storing the enmys Y position
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
# declaring a variable and storing the enemys X position
enemy3XPosition = screen_width
# declaring a variable and storing the enmys Y position
enemy3YPosition = random.randint(0, screen_height - enemy3_height)
# declaring a variable and storing the enemys X position
enemy4Xposition = screen_width
# declaring a variable and storing the enmys Y position
enemy4Yposition = random.randint(0, screen_height - enemy4_height)
# declaring a variable and storing the prizes X position
prizeXPosition = screen_width
# declaring a variable and storing the prizes Y position
prizeYPosition = random.randint(0, screen_height - prize_height)


# delcaring a boolean value
key_up= False
# delcaring a boolean value
key_down = False
# delcaring a boolean value
key_left= False
# delcaring a boolean value
key_right = False
 

# while loop
while 1:

    # clearing the screen
    screen.fill(0)
    # printing the background onto the screen
    screen.blit(background, (0, 0))
    # printing the player image onto the screen
    screen.blit(player, (playerXPosition, playerYPosition))
    # printing the enemy image on the screen
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    # printing the enemy image on the screen
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    # printing the enemy image on the screen
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    # printing the enemy image on the screen
    screen.blit(enemy4, (enemy4Xposition, enemy4Yposition))
    # printing the prize image on the screen
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    # updating the screen using the .flip() function
    pygame.display.flip()

    # creating a for loop
    for event in pygame.event.get():
     

        # if statement
        if event.type == pygame.QUIT:
            # using the .quit() function to exit the game
            pygame.quit()
            exit(0)

        # if statement
        if event.type == pygame.KEYDOWN:

            # if statement
            if event.key == pygame.K_UP:
                # storing a boolean value
                key_up = True
            # if statement
            if event.key == pygame.K_DOWN:
                # storing a boolean value
                key_down = True
            # if statement
            if event.key == pygame.K_LEFT:
                # storing a boolean value
                key_left = True
            # if statement
            if event.key == pygame.K_RIGHT:
                # storing a boolean value
                key_right = True
         
        # if statement
        if event.type == pygame.KEYUP:

            # if statement
            if event.key == pygame.K_UP:
                # declaring a boolean value
                key_up = False
            # if statement
            if event.key == pygame.K_DOWN:
                # declaring a boolean value
                key_down = False
            # if statement
            if event.key == pygame.K_LEFT:
                # declaring a boolean value
                key_left = False
            # if statement
            if event.key == pygame.K_RIGHT:
                # declaring a boolean value
                key_right = False

    # if statement and storing a boolean value
    if key_up == True:
        # if statement and using arithmetic operations
        if playerYPosition > 0 :
            # calculation using the arithmetic operation of subtraction
            playerYPosition -= 0.5
    # if statement and storing a boolean value
    if key_down == True:
        # if statement and using arithmetic operations
        if playerYPosition < screen_height - image_height:
            # calculation using the arithmetic operation of addition
            playerYPosition += 0.5
    # if statement and storing a boolean value
    if key_left == True:
        # if statement and using arithmetic operations
        if playerXPosition > 0:
            # calculation using the arithmetic operation of subtraction
            playerXPosition -= 0.5
    # if statement and storing a boolean value
    if key_right == True:
        # if statement and using arithmetic operations
        if playerXPosition < screen_width - image_width:
            # calculation using the arithmetic operation of addition
            playerXPosition += 0.5

    # declaring a variable and creating a bounding box for the player
    playerBox = pygame.Rect(player.get_rect())

    # updating the players Y box position
    playerBox.top = playerYPosition
    # updating the players X box position
    playerBox.left = playerXPosition

    # declaring a variable and creating the bounding box for the enemy
    enemy1Box = pygame.Rect(enemy1.get_rect())
    # updating the enemys Y box position
    enemy1Box.top = enemy1YPosition
    # updating the enemys X box position
    enemy1Box.left = enemy1XPosition
    # declaring a variable and creating the bounding box for the enemy
    enemy2Box = pygame.Rect(enemy2.get_rect())
    # updating the enemys Y box position
    enemy2Box.top = enemy2YPosition
    # updating the enemys X box position
    enemy2Box.left = enemy2XPosition
    # declaring a variable and creating the bounding box for the enemy
    enemy3Box = pygame.Rect(enemy3.get_rect())
    # updating the enemys Y box position
    enemy3Box.top = enemy3YPosition
    # updating the enemys X box position
    enemy3Box.left = enemy3XPosition
    # declaring a variable and creating the bounding box for the enemy
    enemy4Box = pygame.Rect(enemy4.get_rect())
    # updating the enemys Y box position
    enemy4Box.top = enemy4Yposition
    # updating the enemys X box position
    enemy4Box.left = enemy4Xposition

    # declaring a variabel and creating the bounding box for the prize
    prizeBox = pygame.Rect(prize.get_rect())
    # updating the prizes Y box position
    prizeBox.top = prizeYPosition
    # updating the prizes X box position
    prizeBox.left = prizeXPosition

    # if statement
    if playerBox.colliderect(prizeBox):

        # print statement
        print("You win!")
        # using the .quit() function to exit the game
        pygame.quit()
        exit(0)
    # if statement
    if playerBox.colliderect(enemy1Box):
        # print statement
        print("You lose!")
        # using the .quit() function to exit the game
        pygame.quit()
        exit(0)

    # if statement
    if playerBox.colliderect(enemy2Box):
        # print statement
        print("You lose!")
        # using the .quit() function to exit the game
        pygame.quit()
        exit(0)

    # if statement
    if playerBox.colliderect(enemy3Box):
        # print statement
        print("You lose!")
        # using the .quit() function to exit the game
        pygame.quit()
        exit(0)

    # if statement
    if playerBox.colliderect(enemy4Box):
        # print statement
        print("You lose!")
        # using the .quit() function to exit the game
        pygame.quit()
        exit(0)

    # if statement
    if playerBox.colliderect(prizeBox):
        # print statement
        print("You Win!")
        # using the .quit() function the exit the game
        pygame.quit()
        exit(0)
         

    # using the arithmetic operation of subtraction to make the enemy image move
    enemy1XPosition -= 0.4
    # using the arithmetic operation of subtraction to make the enemy image move
    enemy2XPosition -= 0.3
    # using the arithmetic operation of subtraction to make the enemy image move
    enemy3XPosition -= 0.2
    # using the arithmetic operation of subtraction to make the enemy image move
    enemy4Xposition -= 0.5
    # using the arithmetic operation of subtraction to make the prize image move
    prizeXPosition -= 0.2

