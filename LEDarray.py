# This library uses adafruit dotstar library to create more functions
# for the 8x8 dotstar array. It also remaps the LEDs so that they follow
# a spiral numbering scheme.
import time
import board
import adafruit_dotstar as dotstar
import RPi.GPIO as GPIO

number = [36, 28, 27, 35, 43, 44, 45, 37, 29, 21, 20, 19, 18, 26, 34, 42, 50, 51, 52, 53, 54, 46, 38, 30, 22, 14, 13, 12, 11, 10, 9, 17, 25, 33, 41, 49, 57, 58, 59, 60, 61, 62, 63, 55, 47, 39, 31, 23, 15, 7, 6, 5, 4, 3, 2, 1, 0, 8, 16, 24, 32, 40, 48, 56]


class LEDarray:
    """
    Class for adafruit dotstar LED matrix. Assumes either one 8x8 is used, or 2 8x8 connected in series
    """
    def __init__(self, n_arrays=1, brightness=0.2):
        if n_arrays != 1 and n_arrays != 2:
            raise IOError('Can only use 1 or 2 8x8 arrays')
        self.array = dotstar.DotStar(board.SCK, board.MOSI, n_arrays*64, brightness=brightness)
    
    def getDotstarObject(self):
        """
        This function return the underlying Dotstar array object.

        Arguments:
        None

        Returns:
        None
        """
        return self.array

    def oneLED(self, LED_num, color):
        """
        This function maps the LED numbering to a spiral pattern going
        outward from the center. It will turn on LEDs to the given color.
        It is assumed that an Adafruit 8x8 Dotstar matrix is used.

        Arguments:
        LED_num          : LED number in the spiral pattern.
        color            : should be colour you want for the LED as either an int-hex or rgb.

        Returns:
        None
        """
        self.array[number[LED_num]] = color
        return

    def turnOnFillCircle(self, radius, color):
        """
        Fill up a 'circle' of LEDs (it fills up a square lol) of a given
        radius. Radius is not given in a distance metric, but rather as
        how many unique rings are inside the circle. So, for the 8x8 LED
        array, the radius is from 0 to 3 with 3 filling up the entire array.

        Arguments:
        radius           : Radius from 0 to 3
        color            : should be colour you want for the LED as either an int-hex or rgb.

        Returns:
        None
        """
        # number of LEDs 
        LED_in_radius = [4, 16, 36, 64]
        for i in range(LED_in_radius[radius]):
            self.oneLED(i, color)
        return

    def turnAllOff(self):
        """
        Turns all LEDs in the array off.
        
        Arguments:
        None

        Returns:
        None
        """
        self.array.fill(0x000000)
        return

    def turnOnRing(self, radius, color):
        """
        Fill up a ring of LEDs (it fills up a square ring lol) of a given
        radius. Radius is not given in a distance metric, but rather as
        how many unique rings are inside the circle. So, for the 8x8 LED
        array, the radius is from 0 to 3 with 3 turning on the outermost ring.

        Arguments:
        radius           : Radius from 0 to 3
        color            : should be colour you want for the LED as either an int-hex or rgb.

        Returns:
        None
        """
        LED_in_radius = [0, 4, 16, 36, 64]
        for i in range(LED_in_radius[radius], LED_in_radius[radius+1]):
            self.oneLED(i, color)
        return
    
    def fill_half(self, color, side):
        """
        turn on half of the array with given color

        Arguments:
        color       : should be colour you want for the LED as either an int-hex or rgb.
        side        : string, 't','b','r','l' for the top/bottom/right/left respectively

        Returns:
        None
        """
        if side == 'l':
            for i in range(32):
                self.array[i] = color
        
        elif side == 'r':
            for i in range(32):
                self.array[i+32] = color
        
        elif side == 't':
            for i in range(4):
                for j in range(i,57+i,8):
                    self.array[j] = color
        
        elif side == 'b':
            for i in range(4):
                for j in range(i,57+i,8):
                    self.array[j+4] = color        

        else:
            raise IOError("wrong side parameter, choose either 'l','r','t','b'")
        
        return

    def fill(self, color):
        """
        Fill the array with given color

        Arguments:
        color            : should be colour you want for the LED as either an int-hex or rgb.

        Returns:
        None
        """
        self.array.fill(color)

# TODO: def brightfield
# TODO: def darkfield

if __name__ == "__main__":
    time.sleep(3.25)
    dot = LEDarray(n_arrays = 1, brightness = 0.4)
    dot.turnAllOff()
#     for i in range(64):
#         dot.oneLED(i, 0xA000A0)
#         time.sleep(0.10)
#     for i in range(64):
#         dot.oneLED(i, 0x000000)
#         time.sleep(0.10)
#     time.sleep(0.5)
#     dot.turnAllOff()
#     time.sleep(0.25)
#     for i in range(4):
#         dot.turnOnFillCircle(i, 0x93A060)
#         time.sleep(1)
#     dot.turnAllOff()
#     time.sleep(0.25)
    # for i in range(4):
    #     dot.turnOnRing(i,(170,118,136))
    #     time.sleep(1)
#     turnAllOff(dot)
#     time.sleep(0.25)
#     dot.turnOnRing(3, 0x80A093)
    #dot.turnAllOff()
    #dot.fill((60,110,60))78/
    dot.turnOnFillCircle(1,(155,123,136)) 
    #dot[11] = (200,0,0)
    time.sleep(2.25)
    dot.turnAllOff()
    dot.fill_half((155,123,136), "b")
    time.sleep(2.25)
    dot.turnAllOff()
    dot.fill_half((155,123,136), "t")
    time.sleep(2.25)
    dot.turnAllOff()
    dot.fill_half((155,123,136), "l")
    time.sleep(2.25)
    dot.turnAllOff()
    dot.fill_half((155,123,136), "r")
    time.sleep(2.25)
    for i in range(4):
        dot.turnAllOff()
        dot.turnOnRing(i,(155,123,136))
        time.sleep(7)
    dot.turnAllOff()
    for i in range(16):
        dot.getDotstarObject()[i] = (155,123,136)
    time.sleep(8)
    dot.turnAllOff()
    for i in range(48,64):
        dot.getDotstarObject()[i] = (155,123,136)
    time.sleep(8)
    dot.turnAllOff()
    dot.turnOnRing(1, (155,123,136))
    #dot[28] = (200, 100, 220)