from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()

def displayObject(x,y,selectObject):
    lcd.clear()
    backlight.set_all(0,255,0)
    backlight.show()
    i = 0
    counter = 0
    while i < len(selectObject):
        j = 0
        temp_x = x
        temp_y = y + counter
        while j < len(selectObject[i]):
            lcd.set_pixel(temp_x,temp_y,selectObject[i][j])
            j = j+1
            temp_x = temp_x+1
        i = i+1
        counter = counter+1
        temp_y=temp_y+1
        lcd.show()
