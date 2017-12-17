import pygame
import random
import time

class Die():
	def __init__(self, rect):
		self.rect = rect
		self.value = 1
		self.save = False

		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))

	def check_status(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		image = self.image

		if (self.rect.x + 100) > mouse[0] > self.rect.x and (self.rect.y + 100) > mouse[1] > self.rect.y:
			if click[0] == 1:
				self.save = not self.save

				print('clicked!')

				if self.save == False:
					image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
				elif self.save == True:
					image = pygame.image.load('Resources/Die_' + str(self.value) + '_grey.png')

				self.image =  pygame.transform.scale(image, (100, 100))
				screen.blit(self.image, self.rect)
				time.sleep(.001)


	def print(self):
		screen.blit(self.image, self.rect)

	def roll(self):
		self.value = random.randint(1,6)
		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))

		self.print()

		return self.value

	def reset(self):
		self.save = False
		self.value = 1
		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))
		screen.blit(self.image, self.rect)

class Dice():
	def __init__(self):
		self.score = 0
		self.rolls = 0

		self.values = []
		self.dice = []

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
		for i in range(0, len(self.dice)):
			Die = self.dice[i]

			Die.check_status()

			if Die.save !=  True:
				self.values.append(Die.roll())

			Die.print()
		self.rolls += 1

	def check_status(self):
		for i in range(0, len(self.dice)):
			Die = self.dice[i]

			Die.check_status()

	def reset(self):
		for i in range(0, len(self.dice)):
			Die = self.dice[i]

			Die.reset()

			screen.fill([255, 255, 255])

			background_image = pygame.transform.scale(pygame.image.load('Resources/Background.png'), (800, 600))
			screen.blit(background_image, (0, 0))

			big_font = pygame.font.SysFont('Calibri Light', 35)
			text = big_font.render('press the spacebar to roll', True, (255, 255, 255))
			screen.blit(text, (250, 520))

			small_font = pygame.font.SysFont('Calibri Light', 28)
			text = small_font.render(str(3-Dice.rolls)+ ' rolls left', True, (255, 255, 255))
			screen.blit(text, (350, 550))

			self.rolls = 0

def screen_set():
	screen.fill([255, 255, 255])

	background_image = pygame.transform.scale(pygame.image.load('Resources/Background.png'), (800, 600))
	screen.blit(background_image, (0, 0))

	if Dice.rolls < 3:
		big_font = pygame.font.SysFont('Calibri Light', 35)
		text = big_font.render('press the spacebar to roll', True, (255, 255, 255))
		screen.blit(text, (250, 520))

		small_font = pygame.font.SysFont('Calibri Light', 28)
		text = small_font.render(str(3-Dice.rolls)+ ' rolls left', True, (255, 255, 255))
		screen.blit(text, (350, 550))

	Dice.print()

############## GAME LOGIC
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Yahtzee")
icon = pygame.image.load('Resources/Icon.png')
pygame.display.set_icon(icon)

Dice = Dice()

done = False

while not done:
	screen_set()

	pressed = pygame.key.get_pressed()

	if Dice.rolls < 3:
		scored = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				Dice.roll()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				Dice.reset()
			if event.type == pygame.MOUSEBUTTONDOWN:
				Dice.check_status()

	elif Dice.rolls >= 3:
		while not scored:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
					Dice.reset()
				if event.type == pygame.MOUSEBUTTONDOWN:
					scored = Button.check_status()

		Dice.reset()

	pygame.display.flip()
