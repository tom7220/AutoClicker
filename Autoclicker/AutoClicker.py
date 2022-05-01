import keyboard
import pyautogui
import sys
while(True):
            pyautogui.click()
            if keyboard.is_pressed('q'):
                quit();
            print("Fail safe Trigged")
