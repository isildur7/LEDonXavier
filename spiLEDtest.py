import time
import random
import board
import adafruit_dotstar as dotstar
 
# On-board DotStar for boards including Gemma, Trinket, and ItsyBitsy
# dots = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
 
# Using a DotStar Digital LED Strip with 30 LEDs connected to hardware SPI
dots = dotstar.DotStar(board.SCK, board.MOSI, 64*2, brightness=0.01)
 
# Using a DotStar Digital LED Strip with 30 LEDs connected to digital pins
# dots = dotstar.DotStar(board.D6, board.D5, 30, brightness=0.2)
 
 
# HELPERS
# a random color 0 -> 192
def random_color():
    return random.randrange(0, 7) * 32
 
 
# MAIN LOOP
n_dots = len(dots)
print(n_dots)
c = (random_color(), random_color(), random_color())
print(c)
# for i in range(25):
#     # Fill each dot with a random color
#     for dot in range(n_dots):
#         dots[dot] = (random_color(), random_color(), random_color())
#     #dots.fill(c)
#     time.sleep(0.25)
for dot in range(n_dots):
        dots[dot] = (random_color(), random_color(), random_color())
    #dots.fill(c)
        time.sleep(1)
dots.fill((0,0,0))
time.sleep(0.25)
dots[63] = c
dots[121] = c
time.sleep(2)
dots.fill(0)