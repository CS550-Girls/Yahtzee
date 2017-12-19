import pygame
import time
import random

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
          self.score = self.row * values.count(self.row)

        elif self.row == 7: # Add sum if a given number occurs three times
            for i in range(1, 7):
                num = values.count(i)
                if num == 3:
                    self.score = sum(values)
                    break

        elif self.row == 8: # Add sum if a given number occurs four times
            for i in range(1, 7):
                num = values.count(i)
                if num == 4:
                    self.score = sum(values)
                    break

        elif self.row == 9: # Set score to 25 if one number occurs twice and another occurs three times
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

        elif self.row == 10: # Set score to 30 if 4 of the digits are in sequence
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

        elif self.row == 11: # Set score to 40 if all 5 of the digits are in sequence
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

        elif self.row == 12: # Set score to 50 if all 5 of the digits are the same
            for i in range(1, 7):
                num = values.count(i)
                if num == 5:
                    self.score = 50
                    break

        elif self.row == 13: # Calculate sum of values
            self.score = sum(values)

  def check_status(self):
     # Get mouse position
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()

     if (self.rect.x + 475) > mouse[0] > self.rect.x and (self.rect.y + 30) > mouse[1] > self.rect.y:
         if click[0] == 1:
             self.calc() # Calculate score

             print(self.score)

             self.filled = True # Set status to 'filled'

             time.sleep(.001)

  def print(self):
      # Create invsible button rectangle
      button = pygame.Surface((self.rect.w, self.rect.h))
      button.set_alpha(0)
      button.fill((0, 128, 255))
      score_screen.blit(button, (self.rect.x, self.rect.y))

      # Print score if button has been clicked
      if self.filled == True:
           small_font = pygame.font.SysFont('Calibri Light', 28)
           text = small_font.render(str(self.score), True, (0, 0, 0))
           score_screen.blit(text, (270, self.rect.y + 5))


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

    def check_status(self):
        for i in range(0, len(self.buttons)): # Loop through and check status of buttons
            Button = self.buttons[i]

            Button.check_status()

def screen_set():
	score_screen.fill([255, 255, 255])

	background_image = pygame.image.load('Resources/Scoresheet.jpg')
	score_screen.blit(background_image, (0, 0))

	Buttons.print()

def reset():
    global values

    for i in range(0, len(values)): # Reset roll-mimicing values
        values[i] = random.randint(1,6)

    print(values)


############## GAME LOGIC
# Initialize pygame and its components
pygame.init()
pygame.font.init()

# Set up window
score_screen = pygame.display.set_mode((574, 673))
pygame.display.set_caption("Yahtzee")
icon = pygame.image.load('Resources/Icon.png')
pygame.display.set_icon(icon)

# Set default values
reset()
done = False
scored = False
values = [0,0,0,0,0]

# Create instance of Dice
Buttons = Buttons()

while not done:
    screen_set()

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        	reset()
        if event.type == pygame.MOUSEBUTTONDOWN:
            scored = Buttons.check_status()

    pygame.display.flip()
