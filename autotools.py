## functions for my program
def findshrtrptt():
    y = pyautogui.locateCenterOnScreen(r'*****')

    while y == None:
        y = pyautogui.locateCenterOnScreen(r'*****')
        pyautogui.click(89, 307)
        pyautogui.press('pagedown')
        print('pagedown')

    if y != None:
        pyautogui.click(89, 307)
        print('going the else route')
        pyautogui.click(y)
        pyautogui.moveTo(228, None)
        pyautogui.click()
        # now begin entering data
        pyautogui.typewrite('8')
        pyautogui.press('enter')
        pyautogui.typewrite('4')
        pyautogui.typewrite('2')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('pagedown')
        pyautogui.typewrite('******')
        pyautogui.typewrite('*******')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.hotkey('Shift', 'F2')
        print('*********')

import pyautogui


def find(x):
    import pyautogui
    y = pyautogui.locateCenterOnScreen(x)
    pyautogui.doubleClick(y)


def tab(x):
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)
    pyautogui.press(x)


#variables
now = datetime.date.today()  # create the date for today
today = '{0:%m%d%y}'.format(now).format(now)
startTime = datetime.now()
jba = pyautogui.locateCenterOnScreen(r'******') 
