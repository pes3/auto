import pyautogui as p

p.click()

def down():
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    p.click()

x = range(0,120,2)
for i in x:
    down()

