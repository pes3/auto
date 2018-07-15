# Code written on 5.29 and is when JBA is already logged in and opens to maximized screen
import pyautogui
from datetime import datetime
from autotools import *




print('**********')
pyautogui.PAUSE = 1
# automate findingfind desktop application
pyautogui.locateCenterOnScreen(r'***********')
print('found')
pyautogui.PAUSE = 3
#automate manual cliking thru a desktop application
pyautogui.doubleClick(255, 138)
pyautogui.click(1053, 135)
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.PAUSE = 2
pyautogui.typewrite('2')
pyautogui.press('enter')
pyautogui.typewrite('40')
pyautogui.keyDown('shift')
pyautogui.press('f4')
pyautogui.keyUp('shift')
pyautogui.typewrite('********')
pyautogui.press('enter')
pyautogui.typewrite('********')
pyautogui.click(502, 274)
pyautogui.typewrite('***********')
pyautogui.hotkey(' ')
pyautogui.hotkey(' ')
pyautogui.typewrite(today)
pyautogui.hotkey(' ')
pyautogui.hotkey(' ')
pyautogui.click(440, 600)
pyautogui.typewrite('*******')
pyautogui.press('enter')
pyautogui.press('f8')
print('***')
#next round

pyautogui.press('esc')
pyautogui.press('ctrl')
pyautogui.PAUSE = .5
pyautogui.press('ctrl')
pyautogui.typewrite('********')
pyautogui.press('enter')
pyautogui.typewrite('353000')
pyautogui.click(438, 365)
pyautogui.typewrite('********')
pyautogui.click(790, 361)
pyautogui.typewrite('*******')
pyautogui.click(438, 422)
pyautogui.typewrite('*******')
pyautogui.press('enter')
pyautogui.press('f8')
print('***')
#next round
print('****')
pyautogui.PAUSE = .5
pyautogui.click(332, 683)
pyautogui.press('esc')
pyautogui.press('ctrl')
pyautogui.typewrite('******')
pyautogui.press('enter')
pyautogui.typewrite('******')
pyautogui.click(660, 654)
pyautogui.typewrite('2')
pyautogui.press('enter')
pyautogui.typewrite('********')
pyautogui.press('enter')
pyautogui.typewrite('N')
pyautogui.press('enter')
pyautogui.press('f8')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.typewrite('1')
pyautogui.typewrite('1')
pyautogui.press('pgdn')
pyautogui.press('down')
pyautogui.typewrite('1')
pyautogui.press('f8')
print('now 26/IN3')
# worked 5.29

# added 26/in3 5.31
pyautogui.press('ctrl')
pyautogui.press('enter')
pyautogui.click(335, 685)
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.typewrite('26/IN3')
pyautogui.press('enter')
pyautogui.typewrite('353000')
pyautogui.click(566, 422)
pyautogui.typewrite('DG')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.typewrite('Y')
pyautogui.press('enter')
pyautogui.typewrite('Y')
pyautogui.PAUSE = 1
pyautogui.hotkey('F8')
print('************')
# Next Company
pyautogui.press('ctrl')
pyautogui.click(335, 685)
pyautogui.PAUSE = .2
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.press('ctrl')
pyautogui.typewrite('*******')  # input company 32
pyautogui.press('ctrl')
pyautogui.hotkey('Shift', 'F4')
pyautogui.typewrite('******')
pyautogui.press('enter')
pyautogui.typewrite('*******')
pyautogui.click(566, 422)
pyautogui.typewrite('DG')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.typewrite('Y')
pyautogui.press('enter')
pyautogui.typewrite('Y')
pyautogui.PAUSE = 1
pyautogui.hotkey('F8')
# Next Company
print('*******')
pyautogui.press('ctrl')
pyautogui.click(335, 685)
pyautogui.PAUSE = .2
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.press('ctrl')
pyautogui.typewrite('46')  # input company 46
pyautogui.press('ctrl')
pyautogui.hotkey('Shift', 'F4')
pyautogui.typewrite('*******')
pyautogui.press('enter')
pyautogui.typewrite('*******')
pyautogui.click(566, 422)
pyautogui.typewrite('DG')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.typewrite('Y')
pyautogui.press('enter')
pyautogui.typewrite('Y')
pyautogui.PAUSE = 1
pyautogui.hotkey('F8')
print('********')
# clean slate back to CO 40
pyautogui.press('ctrl')
pyautogui.click(335, 685)
pyautogui.PAUSE = .2
pyautogui.press('enter')
pyautogui.press('esc')
pyautogui.press('ctrl')
pyautogui.typewrite('40')
pyautogui.press('ctrl')
pyautogui.hotkey('Shift', 'F4')
print('View below time taken to run code')
print(datetime.now() - startTime)
print('****')


print('******')
pyautogui.hotkey('Shift', 'F2')
findshrtrptt()
findshrtrptt()
findshrtrptt()
pyautogui.press('enter')

print(datetime.now() - startTime)

# everything worked great 6.12.18
# trying without fully testing 80% of saving file to word on 6.13


def find(x):


pyautogui.PAUSE = 6
pyautogui.click(1407, 3)
find(r'************')
pyautogui.click(185, 38)
pyautogui.typewrite('********')
pyautogui.PAUSE = 5
pyautogui.press('enter')
find(r'********')
pyautogui.typewrite('********')
pyautogui.press('tab')
pyautogui.typewrite('******')
pyautogui.press('enter')
find(r'************')
pyautogui.click(633, 407)
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 's')
pyautogui.PAUSE = 3
tab('tab')
pyautogui.press('enter')
pyautogui.typewrite(r'*********')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
find(r'C:\***')
print('done')


