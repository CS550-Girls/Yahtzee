# Yahtzee

## Overview
This program runs a simple single-player Yatzhee game using the Pygame library. 

## API
  ### Die  
  **Init** *(rect)*
  * self.rect 
  * self.value 
  * self.image 
  #### Roll
  * generate random integer up to 6 and set self.value
  * couple second delay (for real roll effect)
  * send image of blurred dice to screen (for real roll effect)
  * set self.image to dice image that matches the roll value
  * return self.value  
  #### Print
  * send self.image to screen

  ### Dice
  **Init** 
  * self.rolls
  * self.values
  * create 5 instances of Die  
  #### Roll
  * list of selected dice
  * roll listed dice
  * each dice returns value, adds to value list
  * add one to self.rolls  
  #### Print
  * send images to screen  

  ### Button
  **Init** *(rect)*
  * self.rect
  * self.score  
  #### Print
  * send (transparent) button to screen
  * if self.score isn't zero, print score  

  ### Upper Section Button
  **Init** *[subclass of Button] (self, rect, num)*
  * self.rect
  * self.num: dice roll value that counts towards score (i.e. count only 1s)
  * self.score  
  #### Calc
  * Based on vlaues of current roll, calculate score
  * Set self.score  
  #### Print
  * send (transparent) button to screen
  * if self.score isn't zero, print score  
