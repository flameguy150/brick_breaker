import pygame
import random

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('brick breaker')  
background_colour = (0, 0, 0)
screen.fill(background_colour)


def my_deep_copy(array):
    deep_array = []
    for point in array:
        deep_array.append(point)
    return deep_array

def my_range(start, end, increment):
    current_value = start
    values = []
    while current_value < end:
        values.append(current_value)
        current_value += increment
    
    return values

""" CLASSES  CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES CLASSES"""
class Ball:
	def __init__(self):
		self.center = (250, 350)
		self.radius = 5
		self.circle = 0
		self.circlec = 0 #canvas circle
		self.x = random.randint(250,300)
		self.y = random.randint(350, 400)
		self.curcenter = (self.x, self.y)
		self.prevx = 0
		self.prevy = 0
		self.ball_XChange = random.choice((-1,1)) #can set to random with randint(1,-1) or smthing like that
		self.ball_YChange = -1
		self.brick = 0 #should be a rect for colliding
		self.grid = 0
		
		

	def physics_move(self):
		# if pygame.Rect.collideobjects(self.circlec, self.grid.bricks):
		# 	# self.ball_XChange *= -1
		# 	self.ball_YChange *= -1
		# 	print("bounce")
		# 	print("")
		for lvlbrick in self.grid.bricks:
			if self.circlec.colliderect(lvlbrick.outline):
				side = self.collision_detection(self.brick)
				if side == "top" or side == "bottom":
					self.ball_XChange *= -1
				elif side == "left" or side == "right":
					self.ball_YChange *= -1
					
		if self.circlec.colliderect(self.brick.outline): #if it collides with paddle
			side = self.collision_detection(self.brick)
			if side == "top" or side == "bottom":
				self.ball_YChange *= -1
			elif side == "left" or side == "right":
				self.ball_XChange *= -1
				
		elif self.x >= 499 or self.x <= 1: 
			self.ball_XChange *= -1
		elif self.y >= 700 or self.y <= 0: 
			self.ball_YChange *= -1
		# else:
		# 	self.lvl_bounce()
		self.prevx = self.x
		self.prevy = self.y
		self.x += self.ball_XChange
		self.y += self.ball_YChange
		self.draw_ball() #redrawing ball
		
	def draw_ball(self):
		if self.circle != 0: #this is for moving the ball
			self.change_ball()#change it to black
			self.circle = 0
			#now it continues w the rest of function to create new ball in the new coords
		center = (self.x, self.y)
		radius = self.radius
		drawn_ball = pygame.draw.circle(screen, (255,255,255), center, radius)
		self.circlec = drawn_ball
		self.circle = self
		
	def change_ball(self):
		color = (0,0,0)
		center = (self.prevx, self.prevy)
		radius = self.radius
		new_ball = pygame.draw.circle(screen, color, center, radius)
		
	def collision_detection(self, brick_): #distance from ball and
		brick = brick_.outline
		top = abs(self.circlec.bottom - brick.top) #top side of brick
		bottom = abs(self.circlec.top - brick.bottom) #bottom side of brick
		left = abs(self.circlec.right - brick.left) #left side of brick
		right = abs(self.circlec.left - brick.right) #right side of brick

		min_dist = min(top, bottom, left, right)
		

		if min_dist == top:
			return "top"
		elif min_dist == bottom:
			return "bottom"
		elif min_dist == left:
			return "left"
		elif min_dist == right:
			return "right"

	
	
	# def create_ball(self): #reason i put this in the grid class is so i can have a ball object to collide w rects
	# 	center = self.center
	# 	radius = self.radius
	# 	drawn_ball = pygame.draw.circle(screen, (255,255,255), center, radius)
		
		
	
    
	
class Brick:
	def __init__(self, left, top, width, height):
		# self.x = 225 # half of window width, we can worry abt resizing later
		self.previleft = 0 #need this to store previous left and change previous brick to black
		self.left = left
		self.top = top
		self.width = width
		self.height = height
		self.rect = 0
		self.outline = 0
	
		
		self.starter = 0
		
		
		
	def create_stbrick(self):
		if self.starter != 0: #only goes through after creating for the first time
			#instead of deleting, what if i just create a whole black canvas to cover?
			self.change_brick() #change rect to black
			self.starter = 0 #delete is a tkinter thing
			#then it continues after this if statement and makes another rect
		color = (255, 255, 255)
		left = self.left
		top = self.top
		width = self.width
		height = self.height
		brick_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-1, top-1, width+2, height+2))
		brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		self.outline = brick_outline
		self.rect = brick #we put it as brick outline so that ball does not draw over brick
		self.starter = self #need this to delete paddle later after redrawing
		
	def change_brick(self): #this can be used to change cells to black to cover
		color = (0,0,0) #black
		left = self.previleft
		top = self.top
		width = self.width
		height = self.height
		new_brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		new_outline = pygame.draw.rect(screen, color, pygame.Rect(left-1, top-1, width+2, height+2))
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
            
		
	def move_left(self):
		if self.left <= 0:
			pass
		else:
			self.previleft = self.left
			self.left -= 1.7
			# print("left")
			self.create_stbrick()
		
	def move_right(self):
		if self.left >= 400:
			pass
		else:
			self.previleft = self.left
			self.left += 1.7
			# print("right")
			self.create_stbrick()
			

	"""level bricks"""
	

	def create_brick(self, left, top, width, height):
		color = (255, 255, 255)
		left = left
		top = top
		width = width
		height = height
		brick_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-1, top-1, width+2, height+2))
		brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		self.outline = brick_outline
		self.rect = brick #we put it as brick outline so that ball does not draw over brick
		

class Grid:
	def __init__(self, my_brick):
		ball = Ball()
		self.width = 500 #window width
		self.height = 700 #window height
		self.my_brick = my_brick
		self.wall_l = 0
		self.wall_r = 0
		self.ball = ball
		self.ball.brick = self.my_brick #for collidepoint w ball
		self.ball.grid = self
		

		self.bricks = []#to store all bricks and access them to change later
	
		
	def generate_grid(self):#generate sht ton of bricks and ball
		#level creation, 3 levels
		#maybe level editor?
		#create red bricks for now then generate different colors
		#500 x 700
		for x in range(10):
			x_ = x*50
			brick_ = Brick(x_, 0, 49, 25)
			left = brick_.left
			top = brick_.top
			width = brick_.width
			height = brick_.height
			brick_.create_brick(left, top, width, height)
			self.bricks.append(brick_)
			
			
		# brick = Brick(0, 0, 50, 25)
		# left = brick.left
		# top = brick.top
		# width = brick.width
		# height = brick.height
		# brick.create_brick(left, top, width, height)
	
	def generate_walls(self):
		wall_l = pygame.draw.line(screen, (0,0,0), (1,0), (1, 700))
		wall_r = pygame.draw.line(screen, (0,0,0), (499,0), (499, 700))
		self.wall_l = wall_l
		self.wall_r = wall_r
		
    
		
	
	

	# def boundaries(self):
	# 	if self.brick.collidepoint(self.wall_r): #have it so if ball collides with a wall object?
	# 		self.brick.left = 400
	# 	elif self.brick.collidepoint(self.wall_r):
	# 		self.brick.left = 0
