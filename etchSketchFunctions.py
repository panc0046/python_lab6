from gfxhat import lcd
from gfxhat import backlight
import click
from etchSketchLibrary import *

#task 1

# Display text
backlight.set_all(0,255,0)
backlight.show()
displayText("etch a sketch",lcd,20,5)

x = input("Enter value of x")
y = input("Enter value of y")

while True:
    keyEvent = click.getchar()
    if x >= 127:
        x = 0  
    elif x <= 0:
        x = 127
    elif y >= 63 :
        y = 0
    elif y <= 0:
        y = 63
    if keyEvent == "q":
        clearScreen(lcd)
        backlight.set_all(0,0,0)
        backlight.show()
        exit()
    elif keyEvent == "s":
        clearScreen(lcd)
    #up arrow event
    elif keyEvent == '\x1b[A':
        y = y-1
        lcd.set_pixel(x,y,1)
        lcd.show()
    #down arrow event
    elif keyEvent == '\x1b[B':
        y = y+1
        lcd.set_pixel(x,y,1)
        lcd.show()
    #right arrow event
    elif keyEvent == '\x1b[C':
        x = x+1
        lcd.set_pixel(x,y,1)
        lcd.show()
    #left arrow event
    elif keyEvent == '\x1b[D':
        x = x-1
        lcd.set_pixel(x,y,1)
        lcd.show()