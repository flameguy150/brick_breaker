import pygame
from pygame import mixer
import random
import math

screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('brick breaker')  
background_colour = (0, 0, 0)
screen.fill(background_colour)

clock = pygame.time.Clock()

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

bricks_remove = []

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
		self.bricks = []
		self.grid = 0
		
		

	def physics_move(self):
		# if pygame.Rect.collideobjects(self.circlec, self.grid.bricks):
		# 	# self.ball_XChange *= -1
		# 	self.ball_YChange *= -1
		# 	print("bounce")
		# 	print("")
		global bricks_remove
		for brick in self.bricks:
			if self.circlec.colliderect(brick.outline): #if ball collides with a level brick
				# corner collisions
				corner_collided, corner = self.corner_collision(brick) 
				if corner_collided == True:
					self.ball_YChange *= -1
					self.ball_XChange *= -1
					brick.change_brick() #change brick to black
					bricks_remove.append(brick)
					break
					
					
                # side collisions
				side = self.collision_detection(brick) #for level bricks
				if side == "left" or side == "right":
					self.ball_XChange *= -1
					brick.change_brick() #change brick to black
					print(brick.number)
					bricks_remove.append(brick) #delete brick from list
					break
				elif side == "top" or side == "bottom":
					self.ball_YChange *= -1
					brick.change_brick() #change brick to black
					print(brick.number)
					bricks_remove.append(brick) #delete brick from list
					break
					
		if self.circlec.colliderect(self.brick.outline): #if it collides with paddle
			
            # corner collisions
			corner_collided, corner = self.corner_collision(brick) 
			if corner_collided:
				self.ball_YChange *= -1
				self.ball_XChange *= -1
				
            # side collisions
			side = self.collision_detection(self.brick)
			if side == "top" or side == "bottom":
				self.ball_YChange *= -1
			elif side == "left" or side == "right":
				self.ball_XChange *= -1
				
		elif self.x >= 499 or self.x <= 1: 
			self.ball_XChange *= -1
		elif self.y >= 700 or self.y <= 0: 
			self.ball_YChange *= -1
			
        #delete bricks
		for brick in bricks_remove:
			if brick in self.bricks:
				self.bricks.remove(brick)

		self.prevx = self.x
		self.prevy = self.y
		self.x += self.ball_XChange
		self.y += self.ball_YChange
		self.generate_ball() #redrawing ball
		
	def generate_ball(self):
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
		
        #check corners as well
		elif min_dist == top and min_dist == right:
			return "topright"
		elif min_dist == top and min_dist == left:
			return "topleft"
		elif min_dist == bottom and min_dist == right:
			return "bottomright"
		elif min_dist == bottom and min_dist == left:
			return "bottomleft"
		
	def corner_collision(self, brick_): #euclidian distance formula = math.sqrt((x2-x1)^2 + (y2-y1)^2)
		ballx, bally = (self.x, self.y)
		radius = self.radius #you can access these w pygame objects

		brick = brick_.outline
		topright = (brick.top, brick.right)
		topleft = (brick.top, brick.left)
		bottomright = (brick.bottom, brick.right)
		bottomleft = (brick.bottom, brick.left)
		corners = [topright, topleft, bottomright, bottomleft]
		# for corner in corners:
		# 	pygame.draw.circle(screen, (0, 255, 0), corner, 3)  # Green dots for corners
		#euclidian distance = distance from center of circle and each corner, if distance <= radius, it is colliding
		#meaning it should return true and the specific point is is colliding with
		#otherwise, returns false
		for cornerx,cornery in corners:
			x2 = cornerx
			y2 = cornery
			x1 = ballx
			y1 = bally
			# print(x2, y2)
			distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
			if distance <= radius:
				return True, (x2, y2)
		return False, None #returns nothing
	
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
		self.number = 0
	
		
		self.starter = 0
		
		
		
	def generate_paddle(self):
		if self.starter != 0: #only goes through after creating for the first time
			#instead of deleting, what if i just create a whole black canvas to cover?
			self.change_paddle() #change rect to black
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
		
	def change_paddle(self): #this can be used to change cells to black to cover
		color = (0,0,0) #black
		left = self.previleft
		top = self.top
		width = self.width
		height = self.height
		new_brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		new_outline = pygame.draw.rect(screen, color, pygame.Rect(left-1, top-1, width+2, height+2))
		# print("redrawing")
		
	def change_brick(self): #this can be used to change cells to black to cover
		color = (0,0,0) #black
		left = self.left
		top = self.top
		width = self.width
		height = self.height
		new_brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))
		new_outline = pygame.draw.rect(screen, color, pygame.Rect(left-1, top-1, width+2, height+2))
		
	# def controls(self, event):
	# 	global running, move_left_, move_right_
		
	# 	# pygame.key.K_RIGHT.set_repeat()
		
	# 		# elif event.key == pygame.K_LEFT:
	# 		# 	self.move_left()
	# 		# elif event.key == pygame.K_RIGHT:
	# 		# 	self.move_right()
            
		
	def move_left(self):
		if self.left <= 0:
			pass
		else:
			self.previleft = self.left
			self.left -= 1.7
			# print("left")
			self.generate_paddle()
		
	def move_right(self):
		if self.left >= 400:
			pass
		else:
			self.previleft = self.left
			self.left += 1.7
			# print("right")
			self.generate_paddle()
			

	"""level bricks"""
	

	def create_brick(self, color, left, top, width, height):
		color = color
		left = left
		top = top
		width = width
		height = height
		brick_outline = pygame.draw.rect(screen, (0,0,0), pygame.Rect(left-1, top-1, width+2, height+2))
		brick = pygame.draw.rect(screen, color, pygame.Rect(left, top, width, height))

		
		# corner points
		
		self.topleft = (left, top) 
		self.topright = ((left + width), top)
		self.bottomleft = (left, (top + height)) 
		self.bottomright = ((left + width), (top + height)) 
		
        #store outline to access hitbox 
		self.outline = brick_outline
		self.rect = brick #we put it as brick outline so that ball does not draw over brick
		
		
		

class Grid:
	def __init__(self, my_brick, ball):
		# ball = Ball()
		self.width = 500 #window width
		self.height = 700 #window height
		self.my_brick = my_brick
		self.wall_l = 0
		self.wall_r = 0
		self.ball = ball
		self.ball.brick = self.my_brick #for collidepoint w ball
		self.ball.grid = self
		self.increments = 0
		

		self.bricks = []#to store all bricks and access them to change later
	
		
	def generate_grid(self):#generate sht ton of bricks and ball
		#level creation, 3 levels
		#maybe level editor?
		#create red bricks for now then generate different colors
		#500 x 700
		for y in range(5):
			for x in range(5):
				x_ = (x*50) + 125
				y_ = y * 25
				color = (255, 0, 0)
				brick_ = Brick(x_, y_, 48, 25)
				left = brick_.left
				top = brick_.top
				width = brick_.width
				height = brick_.height
				brick_.create_brick(color, left, top, width, height)
				brick_.number = self.increments
				self.bricks.append(brick_)
				self.ball.bricks.append(brick_)
				self.increments += 1
			
			
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





# mixer.init() 
# # mixer.music.load("RLbeat2.mp3") 
# # mixer.music.set_volume(0.7) 
# # mixer.music.play(-1, 0.0) 



# paddle = Brick(200, 600, 100, 10) #paddle
# paddle.generate_paddle()

# ball = Ball()
# ball.generate_ball()

# grid = Grid(paddle, ball)
# # grid.my_brick.create_brick()
# grid.generate_walls()
# grid.generate_grid() 
# # grid.ball.draw_ball()



# # grid = Grid(brick)


  
# # Variable to keep our game loop running 
# running = True


# while running:
# 	clock.tick(120)
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
