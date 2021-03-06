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
				time.sleep(.001)
				self.save = not self.save

				if self.save == False:
					image = pygame.image.load('Resources/Die_' + str(self.value) + '.png')

				elif self.save == True:
					image = pygame.image.load('Resources/Die_' + str(self.value) + '_grey.png')

					self.image =  pygame.transform.scale(image, (100, 100))
					screen.blit(self.image, self.rect)

				return True

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
		status = False

		for i in range(0, len(self.dice)):
			Die = self.dice[i]

			if Die.check_status() == True:
				status = True
				break

		return status

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

	def toggle_status(self, num):
	    Die = self.dice[num - 1]

	    Die.save = not Die.save
	    print(Die.save)

	    if Die.save == False:
	        image = pygame.image.load('Resources/Die_' + str(Die.value) + '.png')

	    elif Die.save == True:
	        image = pygame.image.load('Resources/Die_' + str(Die.value) + '_grey.png')

	    Die.image =  pygame.transform.scale(image, (100, 100))
	    screen.blit(Die.image, Die.rect)

class Button():
  def __init__(self, rect, row):
      self.rect = rect
      self.score = 0
      self.row = row
      self.filled = False

  def calc(self):
    global total
    global Dice

    values = Dice.values

    if not self.filled:
        if self.row <= 6:
          self.score = self.row * values.count(self.row)

        elif self.row == 7:
            for i in range(1, 7):
                num = values.count(i)
                if num == 3:
                    self.score = sum(values)
                    break

        elif self.row == 8:
            for i in range(1, 7):
                num = values.count(i)
                if num == 4:
                    self.score = sum(values)
                    break

        elif self.row == 9:
            taken = -1
            two = False
            three = False

            for i in range(1, 7):
                num = values.count(i)
                if num == 3:
                    taken = i
                    three = True
                    break

            for i in range(1, 7):
                if i != taken:
                    num = values.count(i)
                    if num == 2:
                        two = True
                        break

            if two and three == True:
                self.score = 25

        elif self.row == 10:
            for i in range(0, len(values)):
                for x in range(0, len(values)-1):
                    for i in range(1, len(values)):
                        a = values[i-1]
                        b = values[i]

                        if a > b:
                            values[i-1] = b
                            values[i] = a

            for x in range(3, 4):
                a = values[i-3]
                b = values[i-2]
                c = values[i-1]
                d = values[i]

                if b == a+1 and c == a+2 and d == a+3:
                    self.score = 30
                    break

        elif self.row == 11:
            for i in range(0, len(values)):
                for x in range(0, len(values)-1):
                    for i in range(1, len(values)):
                        a = values[i-1]
                        b = values[i]

                        if a > b:
                            values[i-1] = b
                            values[i] = a

            a = values[0]
            b = values[1]
            c = values[2]
            d = values[3]
            e = values[4]

            if b == a+1 and c == a+2 and d == a+3 and e == a+4:
                self.score = 40

        elif self.row == 12:
            for i in range(1, 7):
                num = values.count(i)
                if num == 5:
                    self.score = 50
                    break

        elif self.row == 13:
            self.score = sum(values)

  def check_status(self):
     self.calc()

     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()

     if (self.rect.x + 475) > mouse[0] > self.rect.x and (self.rect.y + 30) > mouse[1] > self.rect.y:
         if click[0] == 1:
             time.sleep(.001)

             print(self.score)

             self.filled = True

  def print(self):
      button = pygame.Surface((self.rect.w, self.rect.h))
      button.set_alpha(50)
      button.fill((0, 128, 255))
      screen.blit(button, (self.rect.x, self.rect.y))

      if self.filled == True:
           small_font = pygame.font.SysFont('Calibri Light', 28)
           text = small_font.render(str(self.score), True, (0, 0, 0))
           screen.blit(text, (270, self.rect.y + 5))


class Buttons():
    def __init__(self):
        self.buttons = []

        for i in range(0, 6):
            y = 108 + (28*i)
            x = 850
            rect = pygame.Rect(x, y, 474, 27)

            row = 1 + i

            self.buttons.append(Button(rect, row))

        for i in range(6, 13):
            y = 226 + (28*i)
            x = 850
            rect = pygame.Rect(x, y, 474, 27)

            row = 1 + i

            self.buttons.append(Button(rect, row))

    def print(self):
        for i in range(0, len(self.buttons)):
            Button = self.buttons[i]

            Button.print()

    def check_status(self):
        for i in range(0, len(self.buttons)):
            Button = self.buttons[i]

            Button.check_status()

def screen_set():
    screen = pygame.display.set_mode((1375, 675))
    screen.fill([255, 255, 255])

    background_image = pygame.transform.scale(pygame.image.load('Resources/Background.png'), (800, 700))
    screen.blit(background_image, (0, 0))

    scorecard_background_image = pygame.transform.scale(pygame.image.load('Resources/Scoresheet.png'), (574, 673))
    screen.blit(scorecard_background_image, (800, 0))

    if Dice.rolls < 3:
        big_font = pygame.font.SysFont('Calibri Light', 35)
        text = big_font.render('press the spacebar to roll', True, (255, 255, 255))
        screen.blit(text, (250, 520))

        small_font = pygame.font.SysFont('Calibri Light', 28)
        text = small_font.render(str(3-Dice.rolls)+ ' rolls left', True, (255, 255, 255))
        screen.blit(text, (350, 550))

        if tutorial == True and Dice.rolls >= 1:
            smallest_font = pygame.font.SysFont('Calibri Light', 20)
            text1 = smallest_font.render("Click on the dice you want to save", True, (255, 255, 255))
            screen.blit(text1, (300, 420))
            time.sleep(1)
            text2 = smallest_font.render("When you're happy with your roll, click on a row on the scoreboard to the right to save your score", True, (255, 255, 255))
            screen.blit(text2, (100, 600))

    Dice.print()
    Buttons.print()


############## GAME LOGIC
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 600))
screen = pygame.display.set_mode((574, 673))

pygame.display.set_caption("Yahtzee")
icon = pygame.image.load('Resources/Icon.png')
pygame.display.set_icon(icon)

done = False
scored = False
rolled = False
tutorial = True
subscores = []

Buttons = Buttons()

Dice = Dice()

while not done:
	screen_set()

	pressed = pygame.key.get_pressed()

	while not rolled:
		screen_set()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and Dice.rolls <= 3:
				Dice.roll()
				rolled = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					Dice.reset()
				elif event.key == pygame.K_1:
					Dice.toggle_status(1)
				elif event.key == pygame.K_2:
					Dice.toggle_status(2)
				elif event.key == pygame.K_3:
					Dice.toggle_status(3)
				elif event.key == pygame.K_4:
					Dice.toggle_status(4)
				elif event.key == pygame.K_5:
					Dice.toggle_status(5)
				elif event.key == pygame.K_6:
					Dice.toggle_status(6)

			'''
			if event.type == pygame.MOUSEBUTTONDOWN:
				Dice.check_status()
			'''
		pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and Dice.rolls <= 3:
			Dice.roll()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				Dice.reset()
			elif event.key == pygame.K_1:
				Dice.toggle_status(1)
			elif event.key == pygame.K_2:
				Dice.toggle_status(2)
			elif event.key == pygame.K_3:
				Dice.toggle_status(3)
			elif event.key == pygame.K_4:
				Dice.toggle_status(4)
			elif event.key == pygame.K_5:
				Dice.toggle_status(5)
			elif event.key == pygame.K_6:
				Dice.toggle_status(6)

		if event.type == pygame.MOUSEBUTTONDOWN:
			scored = Buttons.check_status()

	if scored == True:
		Dice.reset()
		scored = False
		rolled = False
		tutorial = False
		print(sum(subscores))

	pygame.display.flip()
