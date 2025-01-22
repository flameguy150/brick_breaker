import pygame


"""


make ball object 
    - figure out physics and moving mechanics

make a brick object (the rectangles)
    -have them dissapear when colliding with ball

player controls
    -should be controlled by keyboard




"""
pygame.display.init()

background_colour = (0, 0, 0) 
rectangle_color = (255,0,0)
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((500, 700)) 
  
# Set the caption of the screen 
pygame.display.set_caption('brick breaker') 

# Fill the background colour to the screen 
screen.fill(background_colour)

move_left_ = False
move_right_ = False

clock = pygame.time.Clock()


def my_deep_copy(array):
    deep_array = []
    for point in array:
        deep_array.append(point)
    return deep_array

""" CLASSES  CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES"""

class Ball:
    pass

class Brick:
	def __init__(self, left, top, width, height):
		# self.x = 225 # half of window width, we can worry abt resizing later
		self.previleft = 0 #need this to store previous left and change previous brick to black
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		self.rect = 0
		
		self.starter = 0
		
		
		
	def create_brick(self):
		if self.starter != 0: #only goes through after creating for the first time
			#instead of deleting, what if i just create a whole black canvas to cover?
			self.change_brick() #change rect to black
			self.starter = 0 #delete is a tkinter thing
		color = (255, 255, 255)
		left = self.left
		top = self.top
		width = self.width
		height = self.height
		brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		self.rect = brick
		self.starter = self #need this to delete later after redrawing
		
	def change_brick(self): #this can be used to change cells to black to cover
		color = (0,0,0) #black
		left = self.previleft
		top = self.top
		width = self.width
		height = self.height
		new_brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		# print("redrawing")
		
	def controls(self, event):
		global running, move_left_, move_right_
		
		# pygame.key.K_RIGHT.set_repeat()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE: #ESCAPE = QUIT BUTTON
				running = False
			# elif event.key == pygame.K_LEFT:
			# 	self.move_left()
			# elif event.key == pygame.K_RIGHT:
			# 	self.move_right()
			
				

			
				
			# brick.move #brick object will be redrawn
		
	def move_left(self):
		self.previleft = self.left
		self.left -= 1
		print("left")
		self.create_brick()
		
	def move_right(self):
		self.previleft = self.left
		self.left += 1
		print("right")
		self.create_brick()
	
		

class Grid:
	def __init__(self, brick):
		self.width = 500 #window width
		self.height = 700 #window height
		self.brick = brick










""" CLASSES  CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES"""







brick = Brick(225, 600, 50, 10)
brick.create_brick()


# grid = Grid(brick)

pygame.display.flip() 
  
# Variable to keep our game loop running 
running = True


while running:
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