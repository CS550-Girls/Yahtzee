import pygame
import time

values = [4,5,5,4,4]

class Button():
  def __init__(self, rect, row):
      self.rect = rect
      self.score = 0
      self.row = row

  def calc(self):
    if self.row <= 6:
      self.score = self.row * values.count(self.row)

    if self.row == 7:
        for i in range(1, 7):
            num = values.count(i)
            if num == 3:
                self.score = sum(values)
                break

    if self.row == 8:
        for i in range(1, 7):
            num = values.count(i)
            if num == 4:
                self.score = sum(values)
                break

    if self.row == 9:
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

    if self.row == 10:
        sorted_values = [0]
        for i in range(0, len(values)):
            value = values[i]
            index = len(sorted_values)-1
            sorted = False

            while not sorted
            if value > sorted_values[index]:
                sorted_values[index + 1] = value

    if self.row == 12:
        for i in range(1, 7):
            num = values.count(i)
            if num == 5:
                self.score = 50
                break

    if self.row == 13:
        self.score = sum(values)

  def print(self):
      pygame.draw.rect(score_screen, (0, 128, 255), self.rect)

  def check_status(self):
      self.calc()

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()

      if (self.rect.x + 475) > mouse[0] > self.rect.x and (self.rect.y + 30) > mouse[1] > self.rect.y:
          if click[0] == 1:

              print(self.score)

              small_font = pygame.font.SysFont('Calibri Light', 28)
              text = small_font.render(str(self.score), True, (0, 0, 0))
              score_screen.blit(text, (350, 100 + 30 * self.row))

              time.sleep(.001)

'''
class Upper_Section_Button(Button):
  def __init__(self, rect, num):
<<<<<<< HEAD
      Button.__init__(self)

  def calc(self):

'''
class Buttons():
    def __init__(self):
        self.buttons = []

        for i in range(0, 6):
            y = 108 + (28*i)
            x = 50
            rect = pygame.Rect(x, y, 474, 27)

            row = 1 + i

            self.buttons.append(Button(rect, row))

        for i in range(6, 14):
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
        for i in range(0, len(self.buttons)):
            Button = self.buttons[i]

            Button.check_status()

def screen_set():
	score_screen.fill([255, 255, 255])

	background_image = pygame.image.load('Resources/Scoresheet.jpg')
	score_screen.blit(background_image, (0, 0))

############## GAME LOGIC
pygame.init()
pygame.font.init()

score_screen = pygame.display.set_mode((574, 673))

pygame.display.set_caption("Yahtzee")
icon = pygame.image.load('Resources/Icon.png')
pygame.display.set_icon(icon)

done = False
scored = False

Buttons = Buttons()

while not done:

    screen_set()

    Buttons.print()

    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            scored = Buttons.check_status()

    pygame.display.flip()
=======
  
  def calc():
  

###############################
import sys
import pygame
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
scoreBoardTitle = [' ','Ones','Twos','Threes','Fours','Fives','Sixes','Sum','Bonus','Three of a kind','Four of a kind','Full House','Small Straight','Large Straight','Chance','YAHTZEE','TOTAL SCORE']


class ScoreCard(object):
    def __init__(self):
        pygame.init()
        self.size = width, height = 480,640
        self.width = 480
        self.height = 640
        self.rowheight = 37
        self.titlewidth = 300
        self.user1width = 90
        self.user2width = 90
        self.totalRows = 17
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Score Card")
        self.myfont = pygame.font.SysFont('Arial', 25)
        self.screen.fill((white))
        pygame.display.update()

    def addRects(self):
        rectX = 0
        rectY = 0
        for i in range(self.totalRows):
            self.rect = pygame.draw.rect(self.screen, (black),(rectX,rectY,self.titlewidth, self.rowheight), 2)
            self.screen.blit(self.myfont.render(scoreBoardTitle[i], True, black), (rectX+10, rectY+1))
            self.rect = pygame.draw.rect(self.screen, (black),(rectX + self.titlewidth ,rectY,self.user1width, self.rowheight), 2)
            self.rect = pygame.draw.rect(self.screen, (black),(rectX + self.titlewidth + self.user1width,rectY,self.user2width, self.rowheight), 2)
            rectY = (rectY + self.rowheight)
            
        pygame.display.update()

    def addText(self,rowNum,UserNum,value):
        # Row Number is number of row for which score needs to changed (Value values for ROw Num is 0 to 16)
        #uSer num is 1 or 2 (For the user you need to changet the score) (Value values for Usernum is 1 and 2)
        
        if (UserNum ==1):
            rectX = self.titlewidth + 10
        elif (UserNum ==2):
            rectX = self.titlewidth + self.user1width + 10
        else:
            return

        rectY = rowNum * self.rowheight
        self.screen.blit(self.myfont.render(value, True, black), (rectX, rectY))
        pygame.display.update()

    def addTextByPixel(self,pixelX,pixleY,value):
        self.screen.blit(self.myfont.render(value, True, black), (pixelX, pixleY))
        pygame.display.update()


if __name__ == '__main__':
    scoreCard = ScoreCard()
    scoreCard.addRects()
    scoreCard.addText(5,2,"10")
    scoreCard.addText(5,1,"20")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                #pygame.quit(); sys.exit();
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                scoreCard.addTextByPixel(Mouse_x,Mouse_y,"20")
                
>>>>>>> 1ab1755f2d68cf2c66bbe98328d51ef6d3867fc7
