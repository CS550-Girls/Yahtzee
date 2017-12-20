import pygame
import time
import random

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
		#screen.blit(self.image, self.rect)

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
		self.values = []
		# Loop through dice and generate new values
		for i in range(0, len(self.dice)):
			Die = self.dice[i]
			Die.check_status()

			if Die.save !=  True:
				self.values.append(Die.roll())

			#Die.print()

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
'''
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

	#Dice.print()
'''
class Button():
  def __init__(self, rect, row):
      self.rect = rect # Define position
      self.score = 0 # Set default score
      self.row = row # Set row number on grid
      self.filled = False # Set default 'filled' bool value

  def calc(self):
    global total

    # Calculate score based on given values and row number

    if not self.filled:
        if self.row <= 6: # Add all occurances of a given number
          self.score = self.row * Dice.values.count(self.row)

        elif self.row == 7: # Add sum if a given number occurs three times
            for i in range(1, 7):
                num = Dice.values.count(i)
                if num == 3:
                    self.score = sum(Dice.values)
                    break

        elif self.row == 8: # Add sum if a given number occurs four times
            for i in range(1, 7):
                num = Dice.values.count(i)
                if num == 4:
                    self.score = sum(Dice.values)
                    break

        elif self.row == 9: # Set score to 25 if one number occurs twice and another occurs three times
            taken = -1
            two = False
            three = False

            for i in range(1, 7):
                num = Dice.values.count(i)
                if num == 3:
                    taken = i
                    three = True
                    break

            for i in range(1, 7):
                if i != taken:
                    num = Dice.values.count(i)
                    if num == 2:
                        two = True
                        break

            if two and three == True:
                self.score = 25

        elif self.row == 10: # Set score to 30 if 4 of the digits are in sequence
            for i in range(0, len(Dice.values)):
                for x in range(0, len(Dice.values)-1):
                    for i in range(1, len(Dice.values)):
                        a = Dice.values[i-1]
                        b = Dice.values[i]

                        if a > b:
                            Dice.values[i-1] = b
                            Dice.values[i] = a

            for x in range(3, 4):
                a = Dice.values[i-3]
                b = Dice.values[i-2]
                c = Dice.values[i-1]
                d = Dice.values[i]

                if b == a+1 and c == a+2 and d == a+3:
                    self.score = 30
                    break

        elif self.row == 11: # Set score to 40 if all 5 of the digits are in sequence
            for i in range(0, len(Dice.values)):
                for x in range(0, len(Dice.values)-1):
                    for i in range(1, len(Dice.values)):
                        a = Dice.values[i-1]
                        b = Dice.values[i]

                        if a > b:
                            Dice.values[i-1] = b
                            Dice.values[i] = a

            a = Dice.values[0]
            b = Dice.values[1]
            c = Dice.values[2]
            d = Dice.values[3]
            e = Dice.values[4]

            if b == a+1 and c == a+2 and d == a+3 and e == a+4:
                self.score = 40

        elif self.row == 12: # Set score to 50 if all 5 of the digits are the same
            for i in range(1, 7):
                num = Dice.values.count(i)
                if num == 5:
                    self.score = 50
                    break

        elif self.row == 13: # Calculate sum of values
            self.score = sum(Dice.values)

  def check_status(self):
     # Get mouse position
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()

     if (self.rect.x + 475) > mouse[0] > self.rect.x and (self.rect.y + 30) > mouse[1] > self.rect.y:
         if click[0] == 1:
             self.calc() # Calculate score

             print(self.score)

             subscores.append(self.score)

             if self.row <= 6:
                 upper_subscores.append(self.score)
             elif self.row > 6:
                 lower_subscores.append(self.score)

             self.filled = True # Set status to 'filled'

             time.sleep(.001)

             return True

         else:
             return False

  def print(self):
      # Create invsible button rectangle
      button = pygame.Surface((self.rect.w, self.rect.h))
      button.set_alpha(0)
      button.fill((0, 128, 255))
      screen.blit(button, (self.rect.x, self.rect.y))

      # Print score if button has been clicked
      if self.filled == True:
           small_font = pygame.font.SysFont('Calibri Light', 28)
           text = small_font.render(str(self.score), True, (0, 0, 0))
           screen.blit(text, (270, self.rect.y + 5))


class Buttons():
    def __init__(self):
        self.buttons = [] # Define list to hold buttons

        for i in range(0, 6): # Loop through and create top 6 buttons
            y = 108 + (28*i)
            x = 50
            rect = pygame.Rect(x, y, 474, 27)

            row = 1 + i

            self.buttons.append(Button(rect, row))

        for i in range(6, 13): # Loop through and create bottom 6 buttons
            y = 226 + (28*i)
            x = 50
            rect = pygame.Rect(x, y, 474, 27)

            row = 1 + i

            self.buttons.append(Button(rect, row))

    def print(self):
        for i in range(0, len(self.buttons)):
            Button = self.buttons[i]

            Button.print()

        upper_score = sum(upper_subscores)
        if upper_score >= 65:
            augmented_upper_score = upper_score +35
            text5 = small_font.render('35', True, (0, 0, 0))
            screen.blit(text5, (268, 310))
        else:
            augmented_upper_score = upper_score
        lower_score = sum(lower_subscores)
        total_score = sum(subscores)

        small_font = pygame.font.SysFont('Calibri Light', 28)

        text1 = small_font.render(str(upper_score), True, (0, 0, 0))
        screen.blit(text1, (268, 282))
        text2 = small_font.render(str(upper_score), True, (0, 0, 0))
        screen.blit(text2, (268, 340))
        text3 = small_font.render(str(lower_score), True, (0, 0, 0))
        screen.blit(text3, (268, 598))
        text4 = small_font.render(str(total_score), True, (0, 0, 0))
        screen.blit(text4, (268, 625))

    def check_status(self):
        for i in range(0, len(self.buttons)): # Loop through and check status of buttons
            Button = self.buttons[i]

            scored = Button.check_status()

            if scored:
                break

        return scored

def screen_set():
	screen.fill([255, 255, 255])

	background_image = pygame.image.load('Resources/Scoresheet.jpg')
	screen.blit(background_image, (0, 0))

	Buttons.print()


############## GAME LOGIC
# Initialize pygame and its components
pygame.init()
pygame.font.init()

# Set up window
screen = pygame.display.set_mode((574, 673))
pygame.display.set_caption("Yahtzee")
icon = pygame.image.load('Resources/Icon.png')
pygame.display.set_icon(icon)

# Set default values
done = False
scored = False

subscores = []
upper_subscores = []
lower_subscores = []

# Create instance of Dice
Buttons = Buttons()
Dice = Dice()

while not done:
    screen_set()

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and Dice.rolls < 3:
           Dice.roll()
           print(Dice.values)
        if event.type == pygame.MOUSEBUTTONDOWN:
            scored = Buttons.check_status()

    if scored == True:
        print('scored!')
        Dice.rolls = 0
        scored = False

    pygame.display.flip()
