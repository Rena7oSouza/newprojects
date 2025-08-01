import pyautogui
import time
import pyperclip
import keyboard

def pyautoguipress(command, waittime=1, times=1):
    for _ in range(times):
        pyautogui.press(command)
        time.sleep(waittime)


def pyautoguiwrite(text, waittime=1, interval=0.05):
    pyautogui.write(text, interval=interval)
    time.sleep(waittime)

def presstab(waittime=1, times=1):
    for _ in range(times):
        keyboard.send("tab")
        time.sleep(waittime)
    
def pyautoguihotkey(keya, keyb, waittime=1):
        pyautogui.hotkey(keya, keyb)
        time.sleep(waittime)

def copypaste(info, waittime=1):
    pyperclip.copy(info)
    # Hold ctrl
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)
    # Press V
    pyautoguipress("v", 0.1)
    # Release Ctrl
    pyautogui.keyUp('ctrl')
    time.sleep(waittime)

def select_and_copy_screen():
    # Hold ctrl
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)
    # Press A
    pyautoguipress("a", 0.1)
    # Press C
    pyautoguipress("c", 0.1)
    # Release Ctrl
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)
 
    copied_text = pyperclip.paste()
    return copied_text
    