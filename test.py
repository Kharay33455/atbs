import pyautogui
import time
#make pause command variable 
pyautogui.PAUSE = 1
#allow failsafe
pyautogui.FAILSAFE = True
#screen size to get
width, heigth = pyautogui.size()
print(f'Width is {width}\nHeight is {heigth}')
#moveTo(x,y,duration) move to 
#moveRel(x,y,duration) move in relation to
#pyautofui.position() get mouse pposition
#pyautogui.moveTo(500, 500, 1)
#pyautogui.rightClick()
#pyautogui.leftClick()
#pyautogui.doubleClick()
#pyautogui.dragTo() pyautogui.mouseUp() and mouseDown()
#pyautogui.dragRel()
#pyautogui.scroll(int) scroll by int numbers
""" screenshotting and analyzing screenshots """
#im = pyautogui.screenshot() takes a screenshot and store it in im variable. width and height of screenshot is screen width -1 and screen height -1
#im.getpixel((x,y)) get color at pixel x and y of image im where im is a picture taken by screen shot and x is less than width, y is also less than height
#print(pyautogui.pixelMatchesColor(x,y,(a,b,c))) match color of screen at x, y to rgb(a,b,c)
"""Locate things on screen"""
##a,b,c,d = pyautogui.locateOnScreen('picture.format') locate the picture and store its co-ordinates in a,b,c,d. where a is left, b is top, c is width and height is d.
#x,y = pyautogui.center((a,b,c,d)) locate the center of said image and store iit in x,y
#list(pyautogui.locateAllOnScreen('picture.format')) locate all in case it's more than one
"""controlling the keyboard"""

#pyautogui.typewrite(string) write a string. remember to click first
#pyautogui.keyDown() and pyautogui.keyUp() used to hold down keys and release them.
#to do things with hotkeys(holding down multiple keys).. use pyautogui.hotkey('key1','key2',...)
