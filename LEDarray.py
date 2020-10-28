# This library uses adafruit dotstar library to create more functions
# for the 8x8 dotstar array. It also remaps the LEDs so that they follow
# a spiral numbering scheme.
import time
import board
import adafruit_dotstar as dotstar

number = [36, 28, 27, 35, 43, 44, 45, 37, 29, 21, 20, 19, 18, 26, 34, 42, 50, 51, 52, 53, 54, 46, 38, 30, 22, 14, 13, 12, 11, 10, 9, 17, 25, 33, 41, 49, 57, 58, 59, 60, 61, 62, 63, 55, 47, 39, 31, 23, 15, 7, 6, 5, 4, 3, 2, 1, 0, 8, 16, 24, 32, 40, 48, 56]

def oneLED(LED_array_object, LED_num, color):
    """
    This function maps the LED numbering to a spiral pattern going
    outward from the center. It will turn on LEDs to the given color.
    It is assumed that an Adafruit 8x8 Dotstar matrix is used.

    Arguments:
    LED_array_object : Proper Dotstar Object for the array.
    LED_num          : LED number in the spiral pattern.
    color            : should be colour you want for the LED as either an int-hex or rgb.

    Returns:
    None
    """
    LED_array_object[number[LED_num]] = color
    return

def turnOnFillCircle(LED_array_object, radius, color):
    """
    Fill up a 'circle' of LEDs (it fills up a square lol) of a given
    radius. Radius is not given in a distance metric, but rather as
    how many unique rings are inside the circle. So, for the 8x8 LED
    array, the radius is from 0 to 3 with 3 filling up the entire array.

    Arguments:
    LED_array_object : Proper Dotstar Object for the array.
    radius           : Radius from 0 to 3
    color            : should be colour you want for the LED as either an int-hex or rgb.

    Returns:
    None
    """
    # number of LEDs 
    LED_in_radius = [4, 16, 36, 64]
    for i in range(LED_in_radius[radius]):
        oneLED(LED_array_object, i, color)
    return

def turnAllOff(LED_array_object):
    """
    Turns all LEDs in the array off.
    
    Arguments:
    LED_array_object : Proper Dotstar Object for the array.

    Returns:
    None
    """
    LED_array_object.fill(0x000000)
    return

def turnOnRing(LED_array_object, radius, color):
    """
    Fill up a ring of LEDs (it fills up a square ring lol) of a given
    radius. Radius is not given in a distance metric, but rather as
    how many unique rings are inside the circle. So, for the 8x8 LED
    array, the radius is from 0 to 3 with 3 turning on the outermost ring.

    Arguments:
    LED_array_object : Proper Dotstar Object for the array.
    radius           : Radius from 0 to 3
    color            : should be colour you want for the LED as either an int-hex or rgb.

    Returns:
    None
    """
    LED_in_radius = [0, 4, 16, 36, 64]
    for i in range(LED_in_radius[radius], LED_in_radius[radius+1]):
        oneLED(LED_array_object, i, color)
    return

# TODO: def brightfield
# TODO: def darkfield

if __name__ == "__main__":
    dot = dotstar.DotStar(board.SCK, board.MOSI, 64, brightness=0.01)
    turnAllOff(dot)
    time.sleep(1)
    for i in range(64):
        oneLED(dot, i, 0xA000A0)
        time.sleep(0.10)
    for i in range(64):
        oneLED(dot, i, 0x000000)
        time.sleep(0.10)
    time.sleep(0.5)
    turnAllOff(dot)
    time.sleep(0.25)
    for i in range(4):
        turnOnFillCircle(dot, i, 0x93A060)
        time.sleep(1)
    turnAllOff(dot)
    time.sleep(0.25)
    for i in range(4):
        turnOnRing(dot,3-i, 0x60A093)
        time.sleep(1)
    turnAllOff(dot)
    time.sleep(0.25)