# import modules
import pyautogui
import webbrowser
import datetime

# define variables
now = datetime.date.today()
today = '{0:%m%d%y}'.format(now).format(now)
##you have to import this module here again
from datetime import datetime

startTime = datetime.now()
##
jba = pyautogui.locateCenterOnScreen(r'')


# define functions
def web(x):
    ie = webbrowser.get(webbrowser.iexplore)
    ie.open(x)




def press(key, times):
    for i in range(0, times):
        pyautogui.press(key)


def type_(txtstring):
    pyautogui.typewrite(txtstring)


def reset():
    pyautogui.press('ctrl')
    pyautogui.press('esc')


def ledger():
    pyautogui.click(335, 685)


def beg():
    ledger()
    reset()
    ledger()


def changeco(company):
    beg()
    type_(company)
    pyautogui.hotkey('Shift', 'F4')


def changerpt(report):
    beg()
    type_(report)
    press('enter', 1)

    def findshrtrptt():
        y = pyautogui.locateCenterOnScreen(r'')

        while y == None:
            y = pyautogui.locateCenterOnScreen(r'')
            pyautogui.click(89, 307)
            press('*', 1)
            print('')

        if y != None:
            pyautogui.click(89, 307)
            print('')
            pyautogui.click(y)
            pyautogui.moveTo(228, None)
            pyautogui.click()
            # now begin entering data
            press('8', 1)
            press('enter')
            press('4', 1)
            press('2', 1)
            press('enter', 2)
            press('pagedown', 1)
            pyautogui.typewrite('******')
            pyautogui.typewrite('******')
            press('enter', 5)
            pyautogui.hotkey('Shift', 'F2')
            print('')