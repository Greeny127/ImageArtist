import time
import cv2
import pyautogui
from colormap import rgb2hex

class Paint:

    def __init__(self):
        self.imName = 'image.jpg'
        self.image = cv2.imread(self.imName)
        self.size = self.image.shape
        self.x = 414
        self.y = 124
        self.startcord = [self.x, self.y] #Change this for starting coord

    def setColor(self, hex):
        pyautogui.click(355, 522, clicks=2) #Change this for the pallete coord
        pyautogui.write(hex)

    def getPixels(self):
        rows = self.size[0] #getting max pixel amount
        cols = self.size[1] # --^
        pixels = []

        for i in range(rows):
            for j in range(cols):
                r, g, b = int(self.image[i, j, 2]), int(self.image[i, j, 1]), int(self.image[i, j, 0]) #RGB Values

                if r >= 250 and g >= 250 and b >= 250: #Checking if it's white, no need to waste time since background is already white
                    pass

                else:
                    hexVal = rgb2hex(r, g, b) #Hex Value
                    pixeldata = (self.startcord[:], hexVal, i, j) #Packing it for appending into 'pixels'

                    pixels.append(pixeldata)

                self.startcord[0] += 1 #Adds 1 to 'startcord' x value, since the pixel is over
            
            self.startcord[0] = self.x #Resets the X value to 'startcord' x value
            self.startcord[1] += 1 #Adds 1 to 'startcord' y value

        return pixels
        
    def draw(self):
        print("Getting Pixel Data")
        pixelData = self.getPixels() #Gets all the pixel coordinates and RGB values
        done = []
        print("Starting Drawing")

        for pixel in pixelData: #cheacks if all the pixels of a color is done by checking if it's in 'done'
            if pixel in done:
                pass
            
            else: #If not then it will search for the pixel and color all the pixels and then append to 'done'
                self.setColor(pixel[1])
                for nums in pixelData:
                    if pixel[1] == nums[1]:
                        done.append(nums)
                        pyautogui.click(x=nums[0][0], y=nums[0][1])

try:

    brush = Paint() #Creating a Paint() object
    time.sleep(5) #5 seconds to switch to the Paint.net window
    print("Started")
    brush.draw()

    print("\nDone")

except pyautogui.FailSafeException:
    print("\nForcefully stopped drawing")
