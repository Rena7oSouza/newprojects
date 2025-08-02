import pyautogui
import time
import pyperclip
import keyboard

def pyautoguipress(command, waittime=1, times=1):
    """
    Press a specific key multiple times with a delay.

    Parameters:
        command (str): The key to press.
        waittime (float): Time to wait between presses (in seconds).
        times (int): Number of times to press the key.
    """
    for _ in range(times):
        pyautogui.press(command)
        time.sleep(waittime)


def pyautoguiwrite(text, waittime=1, interval=0.05):
    """
    Write text using pyautogui with optional typing speed and wait.

    Parameters:
        text (str): The text to type.
        waittime (float): Time to wait after writing.
        interval (float): Delay between key presses.
    """
    pyautogui.write(text, interval=interval)
    time.sleep(waittime)


def presstab(waittime=1, times=1):
    """
    Simulate TAB key presses using the keyboard module.

    Parameters:
        waittime (float): Time to wait between presses.
        times (int): Number of times to press TAB.
    """
    for _ in range(times):
        keyboard.send("tab")
        time.sleep(waittime)


def pyautoguihotkey(keya, keyb, waittime=1):
    """
    Press a combination of two keys simultaneously.

    Parameters:
        keya (str): First key (e.g., 'ctrl').
        keyb (str): Second key (e.g., 's').
        waittime (float): Time to wait after the hotkey is pressed.
    """
    pyautogui.hotkey(keya, keyb)
    time.sleep(waittime)


def copypaste(info, waittime=1):
    """
    Copy text to clipboard and paste it using Ctrl+V.

    Parameters:
        info (str): Text to be copied and pasted.
        waittime (float): Time to wait after pasting.
    """
    pyperclip.copy(info)

    # Hold down Ctrl key
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)

    # Press V to paste
    pyautoguipress("v", 0.1)

    # Release Ctrl key
    pyautogui.keyUp('ctrl')
    time.sleep(waittime)


def select_and_copy_screen():
    """
    Select all content on screen (Ctrl+A) and copy it to clipboard (Ctrl+C).

    Returns:
        str: Text content copied from the screen.
    """
    # Hold down Ctrl key
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)

    # Press A to select all
    pyautoguipress("a", 0.1)

    # Press C to copy
    pyautoguipress("c", 0.1)

    # Release Ctrl key
    pyautogui.keyUp('ctrl')
    time.sleep(0.5)

    # Return copied text from clipboard
    copied_text = pyperclip.paste()
    return copied_text
