import pygame
from breaker_util import Ball, Brick, Grid
from pygame import mixer
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



"""

pygame.display.init()


mixer.init() 
# mixer.music.load("RLbeat2.mp3") 
# mixer.music.set_volume(0.7) 
# mixer.music.play(-1, 0.0) 

 
rectangle_color = (255,0,0)
  
# Define the dimensions of 
# screen object(width,height) 

  
# Set the caption of the screen 
pygame.display.set_caption('brick breaker') 




move_left_ = False
move_right_ = False

clock = pygame.time.Clock()







""" CLASSES  CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES"""







brick = Brick(200, 600, 100, 10)
brick.create_stbrick()

grid = Grid(brick)
# grid.my_brick.create_brick()
grid.generate_walls()
grid.generate_grid() 
grid.ball.draw_ball()



# grid = Grid(brick)

pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True


while running:
	clock.tick(120)
	grid.ball.physics_move()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		pygame.display.flip()
	brick.controls(event)
		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		brick.move_left()	
	elif keys[pygame.K_RIGHT]:
		brick.move_right()
		
	pygame.display.flip()

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