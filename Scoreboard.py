import pygame

class Button():
  def __init__(self, rect):
  
  def print():
  
class Upper_Section_Button():
  def __init__(self, rect, num):
  
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
                
