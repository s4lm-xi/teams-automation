import pyautogui as gui
import time

def main(day, order):
    six = 70
    seven = six + 80
    eight = seven + 80
    nine = eight + 80
    ten = nine + 80
    eleven = ten + 80
    twelve = eleven + 100
    thirteen = twelve + 80
    fourteen = thirteen + 80
    i = 0
    
    for classes in order:
        
        if i >= 1:
            index = order.index(classes)
            sub = index - 1
            total = index - sub
            if total == -2:
                print('3333')
                time.sleep(3)
            elif total == -3:
                print('666666')
                time.sleep(6)
            elif total == -4:
                print('999999')
                time.sleep(9)
            
            
        time.sleep(5)
        x, y = gui.locateCenterOnScreen(day+'.png')
        gui.click(x,y)

        gui.move(300,500)

        gui.scroll(20)
        gui.scroll(-9)

        if classes == 6:
            gui.move(x, y+six)
            gui.click(x, y+six, button='right')
            time.sleep(1)
        elif classes == 7:
            gui.move(x, y+six)
            gui.click(x, y+seven, button='right')
            time.sleep(1)
        elif classes == 8:
            gui.move(x, y+six)
            gui.click(x, y+eight, button='right')
            time.sleep(1)
        elif classes == 9:
            gui.move(x, y+six)
            gui.click(x, y+nine, button='right')
            time.sleep(1)
        elif classes == 10:
            gui.move(x, y+six)
            gui.click(x, y+ten, button='right')
            time.sleep(1)
        elif classes == 11:
            gui.move(x, y+six)
            gui.click(x, y+eleven, button='right')
            time.sleep(1)
        elif classes == 12:
            gui.move(x, y+six)
            gui.click(x, y+twelve, button='right')
            time.sleep(1)
        elif classes == 13:
            gui.move(x, y+six)
            gui.click(x, y+thirteen, button='right')
            time.sleep(1)
        elif classes == 14:
            gui.move(x, y+six)
            gui.click(x, y+fourteen, button='right')
            time.sleep(1)

        x, y = gui.locateCenterOnScreen('view.png')
        gui.click(x,y)
        time.sleep(5)
        x, y = gui.locateCenterOnScreen('join.png')
        gui.click(x, y)
        
        i+=1
        #50 minute sleep in the session
        time.sleep(10)

        #leaving the seesion
        x, y = gui.locateCenterOnScreen('leave.png')
        gui.click(x, y)

        x, y = gui.locateCenterOnScreen('calender.png')
        gui.click(x, y)
        
        
        
day = input('====Enter the day====\n')
order = input('====Enter the order====\n')
main(day, order)