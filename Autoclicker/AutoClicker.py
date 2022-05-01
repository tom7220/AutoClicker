import keyboard
import pyautogui
# if the button q is pressed it will prompt asking you if you want to quit.
# the button q is the fail safe for this project you can also move the cursor to the corners as another failsafe option.
while(True):
            pyautogui.click()
            if keyboard.is_pressed('q'):
                quit();
