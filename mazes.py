import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)

# initial position of ellipse
ell_x = 203.25
ell_y = 230
ell_width = 208.25
ell_height = 235

# maze
# edge
draw.rectangle(((21.25, 0), (218.75, 6.25)), fill='#ffffff') # 1
draw.rectangle(((212.5, 0), (218.75, 240)), fill='#ffffff') # 2
draw.rectangle(((6.25, 218.75), (197.5, 225)), fill='#ffffff') # 3
draw.rectangle(((0, 0), (6.25, 225)), fill='#ffffff') # 4

# align
draw.rectangle(((6.25, 42.5), (21.25, 48.75)), fill='#ffffff')
draw.rectangle(((6.25, 127.5), (21.25, 133.75)), fill='#ffffff')

draw.rectangle(((21.25, 21.25), (48.75, 27.5)), fill='#ffffff')
draw.rectangle(((21.25, 63.75), (48.75, 70)), fill='#ffffff')
draw.rectangle(((21.25, 106.25), (48.75, 112.5)), fill='#ffffff')
draw.rectangle(((21.25, 148.75), (48.75, 155)), fill='#ffffff')

draw.rectangle(((42.5, 85), (70, 91.5)), fill='#ffffff')
draw.rectangle(((42.5, 148.75), (70, 155.25)), fill='#ffffff')
draw.rectangle(((42.5, 170), (70, 176.5)), fill='#ffffff')

draw.rectangle(((63.75, 21.25), (91.25, 27.5)), fill='#ffffff')
draw.rectangle(((63.75, 42.5), (91.25, 48.75)), fill='#ffffff')
draw.rectangle(((63.75, 63.75), (91.25, 70)), fill='#ffffff')
draw.rectangle(((63.75, 106.25), (91.25, 112.5)), fill='#ffffff')
draw.rectangle(((63.75, 148.75), (91.25, 155)), fill='#ffffff')
draw.rectangle(((63.75, 191.25), (91.25, 197.5)), fill='#ffffff')

draw.rectangle(((85, 21.25), (112.5, 27.5)), fill='#ffffff')
draw.rectangle(((85, 63.75), (112.5, 70)), fill='#ffffff')
draw.rectangle(((85, 85), (112.5, 91.25)), fill='#ffffff')
draw.rectangle(((85, 127.5), (112.5, 133.75)), fill='#ffffff')

draw.rectangle(((106.25, 42.5), (133.75, 48.75)), fill='#ffffff')
draw.rectangle(((106.25, 85), (133.75, 91.25)), fill='#ffffff')

draw.rectangle(((127.5, 21.25), (155, 27.5)), fill='#ffffff')
draw.rectangle(((127.5, 106.25), (155, 112.5)), fill='#ffffff')
draw.rectangle(((127.5, 148.75), (155, 155)), fill='#ffffff')
draw.rectangle(((127.5, 191.25), (155, 197.5)), fill='#ffffff')

draw.rectangle(((148.75, 85), (176.25, 91.25)), fill='#ffffff')
draw.rectangle(((148.75, 148.75), (176.25, 155)), fill='#ffffff')
draw.rectangle(((148.75, 170), (176.25, 176.25)), fill='#ffffff')

draw.rectangle(((170, 21.25), (197.5, 27.5)), fill='#ffffff')
draw.rectangle(((170, 106.25), (197.5, 112.5)), fill='#ffffff')
draw.rectangle(((170, 148.75), (197.5, 155)), fill='#ffffff')
draw.rectangle(((170, 191.25), (197.5, 197.5)), fill='#ffffff')

draw.rectangle(((191.25, 85), (218.75, 91.25)), fill='#ffffff')
draw.rectangle(((191.25, 170), (218.75, 176.25)), fill='#ffffff')

# vertical
draw.rectangle(((21.25, 6.25), (27.5, 21.25)), fill='#ffffff')
draw.rectangle(((21.25, 70), (27.5, 106.25)), fill='#ffffff')
draw.rectangle(((21.25, 155), (27.5, 197.47)), fill='#ffffff')

draw.rectangle(((42.5, 27.5), (48.75, 63.75)), fill='#ffffff')
draw.rectangle(((42.5, 91.25), (48.75, 155)), fill='#ffffff')
draw.rectangle(((42.5, 176.25), (48.75, 218.75)), fill='#ffffff')

draw.rectangle(((63.75, 70), (70, 85)), fill='#ffffff')
draw.rectangle(((63.75, 127.5), (70, 148.75)), fill='#ffffff')

draw.rectangle(((85, 48.75), (91.25, 63.75)), fill='#ffffff')
draw.rectangle(((85, 91.25), (91.25, 133.75)), fill='#ffffff')
draw.rectangle(((85, 155), (91.25, 197.47)), fill='#ffffff')

draw.rectangle(((106.25, 27.5), (112.5, 42.5)), fill='#ffffff')
draw.rectangle(((106.25, 112.5), (112.5, 218.75)), fill='#ffffff')

draw.rectangle(((127.5, 6.25), (133.75, 21.25)), fill='#ffffff')
draw.rectangle(((127.5, 48.75), (133.75, 106.25)), fill='#ffffff')
draw.rectangle(((127.5, 127.5), (133.75, 148.75)), fill='#ffffff')
draw.rectangle(((127.5, 170), (133.75, 191.25)), fill='#ffffff')

draw.rectangle(((148.75, 27.5), (155, 85)), fill='#ffffff')
draw.rectangle(((148.75, 112.5), (155, 148.75)), fill='#ffffff')
draw.rectangle(((148.75, 197.5), (155, 218.75)), fill='#ffffff')

draw.rectangle(((170, 27.5), (176.25, 133.75)), fill='#ffffff')
draw.rectangle(((170, 155), (176.25, 197.47)), fill='#ffffff')

draw.rectangle(((191.25, 42.5), (197.5, 85)), fill='#ffffff')
draw.rectangle(((191.25, 127.5), (197.5, 148.75)), fill='#ffffff')


while True:
    # game clear
    if ell_x >= 6.25 and ell_x <= 21.25 and ell_y < 5 :
        draw.rectangle((0, 0, width, height), outline=0, fill='#000000')
        draw.text((35, 110), "Game Clear", font=fnt, fill='#0000ff')
    
    # game over
    if (ell_x >= 21.25 and ell_x <= 218.75 and ell_y >= 0 and ell_y <= 6.25) or \
        (ell_x >= 212.5 and ell_x <= 218.75 and ell_y >= 0 and ell_y <= 240) or \
        (ell_x >= 6.25 and ell_x <= 197.5 and ell_y >= 218.75 and ell_y <= 225) or \
        (ell_x >= 0 and ell_x <= 6.25 and ell_y >= 0 and ell_y <= 225) or \
        \
        \
        (ell_x >= 6.25 and ell_x <= 21.25 and ell_y >= 42.5 and ell_y <= 48.75) or \
        (ell_x >= 6.25 and ell_x <= 21.25 and ell_y >= 127.5 and ell_y <= 133.75) or \
        \
        (ell_x >= 21.25 and ell_x <= 48.75 and ell_y >= 21.25 and ell_y <= 27.5) or \
        (ell_x >= 21.25 and ell_x <= 48.75 and ell_y >= 63.75 and ell_y <= 70) or \
        (ell_x >= 21.25 and ell_x <= 48.75 and ell_y >= 106.25 and ell_y <= 112.5) or \
        (ell_x >= 21.25 and ell_x <= 48.75 and ell_y >= 148.75 and ell_y <= 155) or \
        \
        (ell_x >= 42.5 and ell_x <= 70 and ell_y >= 85 and ell_y <= 91.5) or \
        (ell_x >= 42.5 and ell_x <= 70 and ell_y >= 148.75 and ell_y <= 155.25) or \
        (ell_x >= 42.5 and ell_x <= 70 and ell_y >= 170 and ell_y <= 176.5) or \
        \
        (ell_x >= 63.75 and ell_x <= 91.25 and ell_y >= 21.25 and ell_y <= 27.5) or \
        (ell_x >= 63.75 and ell_x <= 91.25 and ell_y >= 42.5 and ell_y <= 48.75) or \
        (ell_x >= 63.75 and ell_x <= 91.25 and ell_y >= 63.75 and ell_y <= 70) or \
        (ell_x >= 63.75 and ell_x <= 91.25 and ell_y >= 106.25 and ell_y <= 112.5) or \
        (ell_x >= 63.75 and ell_x <= 91.25 and ell_y >= 148.75 and ell_y <= 155) or \
        (ell_x >= 63.75 and ell_x <= 91.25 and ell_y >= 191.25 and ell_y <= 197.5) or \
        \
        (ell_x >= 85 and ell_x <= 112.5 and ell_y >= 21.25 and ell_y <= 27.5) or \
        (ell_x >= 85 and ell_x <= 112.5 and ell_y >= 63.75 and ell_y <= 70) or \
        (ell_x >= 85 and ell_x <= 112.5 and ell_y >= 85 and ell_y <= 91.25) or \
        (ell_x >= 85 and ell_x <= 112.5 and ell_y >= 127.5 and ell_y <= 133.75) or \
        \
        (ell_x >= 106.25 and ell_x <= 133.75 and ell_y >= 42.5 and ell_y <= 48.75) or \
        (ell_x >= 106.25 and ell_x <= 133.75 and ell_y >= 85 and ell_y <= 91.25) or \
        \
        (ell_x >= 127.5 and ell_x <= 155 and ell_y >= 21.25 and ell_y <= 27.5) or \
        (ell_x >= 127.5 and ell_x <= 155 and ell_y >= 106.25 and ell_y <= 112.5) or \
        (ell_x >= 127.5 and ell_x <= 155 and ell_y >= 148.75 and ell_y <= 155) or \
        (ell_x >= 127.5 and ell_x <= 155 and ell_y >= 191.25 and ell_y <= 197.5) or \
        \
        (ell_x >= 148.75 and ell_x <= 176.25 and ell_y >= 85 and ell_y <= 91.25) or \
        (ell_x >= 148.75 and ell_x <= 176.25 and ell_y >= 148.75 and ell_y <= 155) or \
        (ell_x >= 148.75 and ell_x <= 176.25 and ell_y >= 170 and ell_y <= 176.25) or \
        \
        (ell_x >= 170 and ell_x <= 197.5 and ell_y >= 21.25 and ell_y <= 27.5) or \
        (ell_x >= 170 and ell_x <= 197.5 and ell_y >= 106.25 and ell_y <= 112.5) or \
        (ell_x >= 170 and ell_x <= 197.5 and ell_y >= 148.75 and ell_y <= 155) or \
        (ell_x >= 170 and ell_x <= 197.5 and ell_y >= 191.25 and ell_y <= 197.5) or \
        \
        (ell_x >= 191.25 and ell_x <= 218.75 and ell_y >= 85 and ell_y <= 91.25) or \
        (ell_x >= 191.25 and ell_x <= 218.75 and ell_y >= 170 and ell_y <= 176.25) or \
        \
        \
        (ell_x >= 21.25 and ell_x <= 27.5 and ell_y >= 6.25 and ell_y <= 21.25) or \
        (ell_x >= 21.25 and ell_x <= 27.5 and ell_y >= 70 and ell_y <= 106.25) or \
        (ell_x >= 21.25 and ell_x <= 27.5 and ell_y >= 155 and ell_y <= 197.47) or \
        \
        (ell_x >= 42.5 and ell_x <= 48.75 and ell_y >= 27.5 and ell_y <= 63.75) or \
        (ell_x >= 42.5 and ell_x <= 48.75 and ell_y >= 91.25 and ell_y <= 155) or \
        (ell_x >= 42.5 and ell_x <= 48.75 and ell_y >= 176.25 and ell_y <= 218.75) or \
        \
        (ell_x >= 63.75 and ell_x <= 70 and ell_y >= 70 and ell_y <= 85) or \
        (ell_x >= 63.75 and ell_x <= 70 and ell_y >= 127.5 and ell_y <= 148.75) or \
        \
        (ell_x >= 85 and ell_x <= 91.25 and ell_y >= 48.75 and ell_y <= 63.75) or \
        (ell_x >= 85 and ell_x <= 91.25 and ell_y >= 91.25 and ell_y <= 133.75) or \
        (ell_x >= 85 and ell_x <= 91.25 and ell_y >= 155 and ell_y <= 197.47) or \
        \
        (ell_x >= 106.25 and ell_x <= 112.5 and ell_y >= 27.5 and ell_y <= 42.5) or \
        (ell_x >= 106.25 and ell_x <= 112.5 and ell_y >= 112.5 and ell_y <= 218.75) or \
        \
        (ell_x >= 127.5 and ell_x <= 133.75 and ell_y >= 6.25 and ell_y <= 21.25) or \
        (ell_x >= 127.5 and ell_x <= 133.75 and ell_y >= 48.75 and ell_y <= 106.25) or \
        (ell_x >= 127.5 and ell_x <= 133.75 and ell_y >= 127.5 and ell_y <= 148.75) or \
        (ell_x >= 127.5 and ell_x <= 133.75 and ell_y >= 170 and ell_y <= 191.25) or \
        \
        (ell_x >= 148.75 and ell_x <= 155 and ell_y >= 27.5 and ell_y <= 85) or \
        (ell_x >= 148.75 and ell_x <= 155 and ell_y >= 112.5 and ell_y <= 148.75) or \
        (ell_x >= 148.75 and ell_x <= 155 and ell_y >= 197.5 and ell_y <= 218.75) or \
        \
        (ell_x >= 170 and ell_x <= 176.25 and ell_y >= 27.5 and ell_y <= 133.75) or \
        (ell_x >= 170 and ell_x <= 176.25 and ell_y >= 155 and ell_y <= 197.47) or \
        \
        (ell_x >= 191.25 and ell_x <= 197.5 and ell_y >= 42.5 and ell_y <= 85) or \
        (ell_x >= 191.25 and ell_x <= 197.5 and ell_y >= 127.5 and ell_y <= 148.75):
        
        draw.rectangle((0, 0, width, height), outline=0, fill='#000000')
        draw.text((35, 110), "Game Over", font=fnt, fill='#ff0000')
    
    # draw-ellipse
    draw.ellipse((ell_x, ell_y, ell_width, ell_height), fill='#00ff00')
    
    # move-ellipse
    if not button_U.value:  # up pressed
        draw.ellipse((ell_x, ell_y, ell_width, ell_height), fill='#000000')
        ell_y -= 5
        ell_height -= 5

    if not button_D.value:  # down pressed
        draw.ellipse((ell_x, ell_y, ell_width, ell_height), fill='#000000')
        ell_y += 5
        ell_height += 5

    if not button_L.value:  # left pressed
        draw.ellipse((ell_x, ell_y, ell_width, ell_height), fill='#000000')
        ell_x -= 5
        ell_width -= 5

    if not button_R.value:  # right pressed
        draw.ellipse((ell_x, ell_y, ell_width, ell_height), fill='#000000')
        ell_x += 5
        ell_width += 5
    
    # Display the Image
    disp.image(image)

    time.sleep(0.01)