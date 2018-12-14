import pyautogui as p
import pyperclip
# zoon at 75%
def start():
   
    p.click(675, 634)
    p.typewrite('appliances')
    p.press('enter')
    p.click(700, 666)
    p.PAUSE = 4
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    p.click(980, 665)
    p.click(866, 517)
    p.rightClick(885, 673)
    p.PAUSE = 4
    p.press('up')
    p.press('up')
    p.press('up')
    p.press('up')
    p.press('up')
    p.press('enter')
    #now we have opened explorer and about to save file
    #pinterets zoom at 100
    p.hotkey('ctrl','c')
    p.press('enter')
    p.click(298, 13)
    p.click(317, 202)
    p.click(327,304)
    p.click(395,398)
    p.hotkey('ctrl','v')
    p.press('enter')
    #this works to place in image
    p.click(107, 18)
    p.click(670, 521)
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    p.press('down')
    #p.click(724, 563) tried to click for short link now trying image
    x,y = p.locateCenterOnScreen(r'C:\Users\Patrick\amazonaffiliates\shortlink.PNG')
    p.click(x, y)
    p.click(496, 595)
    p.hotkey('ctrl','c')
    p.click(280,13)
    p.click(665, 651)
    p.hotkey('ctrl','v')
    p.click(1361,652)
    p.click()
    p.click()
    p.click()
    p.click()
    p.click()
    p.click()
    p.click(719,524)
    p.click(1352, 241)
    p.click()
    p.click()
    p.click()
    p.click(733, 426)
    p.click(1012, 245)


