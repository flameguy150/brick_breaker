import pygame
from breaker_util import Ball, Brick, Grid
from pygame import mixer
import os
"""


make ball object 
    - figure out physics and moving mechanics

make a brick object (the rectangles)
    -have them dissapear when colliding with ball

player controls
    -should be controlled by keyboard


multiple balls mode?

go through 3 levels


need to implement physics and collision for side of bricks

corner detection is not working so heres what im gonna do:
store corner points for each brick and use that



"""


song = os.path.join("sounds", "2nujabes_type_beat.mp3")

mixer.init() 
mixer.music.load(song) 
mixer.music.set_volume(0.7) 
mixer.music.play(-1, 0.0) 

 

  
# Define the dimensions of 
# screen object(width,height) 

  
# Set the caption of the screen 
pygame.display.set_caption('brick breaker') 




clock = pygame.time.Clock()







""" CLASSES  CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES"""


def mainloop():
	paddle = Brick(200, 600, 100, 10) #paddle
	paddle.generate_paddle()
	ball = Ball()
	ball.generate_ball()
	grid = Grid(paddle, ball)
	grid.generate_grid() 

	
pygame.init()

paddle = Brick(200, 600, 100, 10) #paddle
paddle.generate_paddle()

ball = Ball()
ball.generate_ball()

grid = Grid(paddle, ball)

grid.generate_grid() 
running = True

while running:
	clock.tick(120)
	ball.physics_move()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
				running = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		paddle.move_left()	
	elif keys[pygame.K_RIGHT]:
		paddle.move_right()
		
	pygame.display.flip()
	
pygame.quit()
quit()




# grid = Grid(brick)


  
# Variable to keep our game loop running 



# while running:
# 	clock.tick(120)
# 	# for ball in balls:
# 	ball.physics_move()
# 	for event in pygame.event.get():
# 		# grid.ball.physics_move() #interesting mechanic
# 		if event.type == pygame.QUIT:
# 			running = False
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
# 				running = False
	
		
# 	keys = pygame.key.get_pressed()
# 	if keys[pygame.K_LEFT]:
# 		paddle.move_left()	
# 	elif keys[pygame.K_RIGHT]:
# 		paddle.move_right()
		
# 	pygame.display.flip()

"""
		elif pygame.key.get_pressed()[pygame.K_LEFT]:
			self.previleft = self.left
			self.left -= 1
				# print("left!")
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.previleft = self.left
			self.left += 1
		keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        example.move_left()
    if keys[pygame.K_RIGHT]:
        example.move_right()
		
		
		
		
"""