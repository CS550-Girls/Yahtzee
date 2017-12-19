import pygame
import random
import time

class Die():
	def __init__(self, rect):
		self.rect = rect # Define position
		self.value = 1 # Set initial value
		self.save = False # Set default save value (False = 'don't save')

		# Load and print image corresponding to value
		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))

	def check_status(self):
		# Get mouse status
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		image = self.image # Set default image

		if (self.rect.x + 100) > mouse[0] > self.rect.x and (self.rect.y + 100) > mouse[1] > self.rect.y:
			if click[0] == 1:
				self.save = not self.save # Switch status

				print('clicked!') # For testing

				# Switch image to match save status
				if self.save == False:
					image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
				elif self.save == True:
					image = pygame.image.load('Resources/Die_' + str(self.value) + '_grey.png')

		# Load and print image
		self.image =  pygame.transform.scale(image, (100, 100))
		screen.blit(self.image, self.rect)
		time.sleep(.001)


	def print(self):
		screen.blit(self.image, self.rect) # Print image

	def roll(self):
		self.value = random.randint(1,6) # Generate random value

		# Load and print new image corresponding to value
		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))
		screen.blit(self.image, self.rect)

		# Return value
		return self.value

	def reset(self):
		self.save = False # Un-save all dice
		self.value = 1 # Reset to default value

		# Load and print new image corresponding to value
		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))
		screen.blit(self.image, self.rect)

class Dice():
	def __init__(self):
		self.score = 0 # Set starting score
		self.rolls = 0 # Reset number of rolls

		self.values = [] # Create list for dice values in a given roll
		self.dice = [] # Create list for dice in 'hand'

		# Create dice
		for i in range(0, 5):
			x = 50 + (150*i)
			y = 300
			rect = pygame.Rect(x, y, 0, 0)

			self.dice.append(Die(rect))

	def print(self):
		for i in range(0, len(self.dice)):
			Die = self.dice[i]
			Die.print()

	def roll(self):
		# Loop through dice and generate new values
		for i in range(0, len(self.dice)):
			Die = self.dice[i]
			Die.check_status()

			if Die.save !=  True:
				self.values.append(Die.roll())

			Die.print()

		# Add one to roll count
		self.rolls += 1

	def check_status(self):
		# Loop through dice and check if they're being clicked
		for i in range(0, len(self.dice)):
			Die = self.dice[i]
			Die.check_status()

	def reset(self):
		# Loop through dice and reset each
		for i in range(0, len(self.dice)):
			Die = self.dice[i]
			Die.reset()

		# Reset roll count
		self.rolls = 0

def screen_set():
	# Print background visuals
	screen.fill([255, 255, 255])

	background_image = pygame.transform.scale(pygame.image.load('Resources/Background.png'), (800, 600))
	screen.blit(background_image, (0, 0))

	# Print instructional text if rolling is still active
	if Dice.rolls < 3:
		big_font = pygame.font.SysFont('Calibri Light', 35)
		text = big_font.render('press the spacebar to roll', True, (255, 255, 255))
		screen.blit(text, (250, 520))

		small_font = pygame.font.SysFont('Calibri Light', 28)
		text = small_font.render(str(3-Dice.rolls)+ ' rolls left', True, (255, 255, 255))
		screen.blit(text, (350, 550))

	Dice.print()

############## GAME LOGIC
# Initialize pygame and its components
pygame.init()
pygame.font.init()

# Set up window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Yahtzee")
icon = pygame.image.load('Resources/Icon.png')
pygame.display.set_icon(icon)

# Create instance of Dice
Dice = Dice()

# Set default 'done' bool value
done = False

while not done:
	screen_set()

	pressed = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and Dice.rolls < 3:
			Dice.roll()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
			Dice.reset()
		if event.type == pygame.MOUSEBUTTONDOWN:
			Dice.check_status()

	pygame.display.flip()
