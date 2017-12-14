import pygame
import random
import time

class Die():
	def __init__(self, rect):
		self.rect = rect
		self.value = 0

	def roll(self):
		self.value = random.randint(1,6)
		image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')
		self.image =  pygame.transform.scale(image, (100, 100))

		return self.value

	def print(self):
		screen.blit(self.image, self.rect)


class Dice():
	def __init__(self):
		self.score = 0
		self.rolls = 0

		self.values = []
		self.dice = []

		for i in range(0, 5):
			x = 50 + (150*i)
			y = 250
			rect = pygame.Rect(x, y, 0, 0)

			self.dice.append(Die(rect))

	def roll(self):
		for i in range(0, len(self.dice)):
			self.values.append(self.dice[i].roll())

	def print(self):
		for i in range(0, len(self.dice)):
			self.dice[i].print()

############## GAME LOGIC
pygame.init()
screen = pygame.display.set_mode((800, 600))
background_image = pygame.image.load('Resources/Background.jpg')
screen.blit(background_image, (0, 0))
pygame.display.set_caption("Yahtzee")
done = False

Dice = Dice()

Dice.roll()
Dice.print()

while not done:
	pressed = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

  	# Stuff

	pygame.display.flip()

