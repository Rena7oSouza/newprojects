import pyautogui
import time
import pyperclip
from models.tn5250j_handler import extract_members, add_or_edit, verify_success
import keyboard

class TN5250JAutomation:

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def open_java_program(self):
        print("Opening tn5250j program...")
        pyautogui.press('t')
        time.sleep(2)
        pyautogui.press("enter")
        time.sleep(10)

    def login(self):
        # Typing username and password
        pyautogui.write(self.user, interval=0.05)
        time.sleep(1)
        keyboard.send("tab")
        time.sleep(1)
        print(self.password)
        pyautogui.write(self.password, interval=0.05)
        time.sleep(2)
        pyautogui.press("enter")
        print("Login credentials entered...")
        time.sleep(2)

    def proceed_to_register_screen(self):
        # Navigating through menu to access member list
        pyautogui.write("strpdm", interval=0.05)
        time.sleep(1)
        pyautogui.press("enter")
        pyautogui.write("3")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.write("qcppsrc", interval=0.05)
        time.sleep(1)
        pyautogui.press("enter")

    def select_and_copy_screen(self):
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        # Press A
        pyautogui.press('a')
        time.sleep(0.1)
        # Press A
        pyautogui.press('c')
        time.sleep(0.1)
        # Release Ctrl
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)
 
        copied_text = pyperclip.paste()
        return copied_text
    
    def scroll_and_collect_members(self):
        screens = []
        down_count = 0

        while True:
            copied = self.select_and_copy_screen()
            screens.append(copied)

            if "Bottom" in copied and "More" not in copied:
                break

            pyautogui.press("pagedown")
            time.sleep(1)
            down_count += 1

        for _ in range(down_count):
            pyautogui.press("pageup")
            time.sleep(0.5)

        return screens

    def del_helper(self, letters):
        for _ in range(letters):
            pyautogui.press("backspace")
            time.sleep(0.05)

    def add_member(self, excel, member):
        time.sleep(0.5)
        # Press F6 to Start register
        pyautogui.press("f6")
        time.sleep(1)
        # Type Product
        produto = member.get("Produto", "")
        pyautogui.press("capslock") 
        pyautogui.write(produto.replace(" ", ""), interval=0.05)
        time.sleep(0.5)
        pyautogui.press("capslock")
        keyboard.send("tab")
        time.sleep(0.5)

        #Type TXT
        pyautogui.press("capslock")  
        pyautogui.write("TXT", interval=0.05)
        time.sleep(0.5)
        pyautogui.press("capslock")
        # Del function wasn't working
        pyautogui.write(" " * 2, interval=0.02)  
        time.sleep(0.2)
        self.del_helper(2)
        time.sleep(0.5)
        keyboard.send("tab")
        time.sleep(0.5)

        valor = f"{float(member.get('Valor', 0)):0.2f}"
        valor = f"valor {valor}" 
        pyautogui.write(valor, interval=0.1)
        time.sleep(1)

        # Press Enter
        pyautogui.press("enter")
        time.sleep(1)

        #Type Description
        descricao = member.get("Descrição", "")[:70]
        pyautogui.write(descricao, interval=0.05)
        time.sleep(0.5)

        #Press Enter
        pyautogui.press("enter")
        time.sleep(1)

        #Press F3 
        pyautogui.press("f3")
        time.sleep(0.5)

        #Press Enter
        pyautogui.press("enter")
        time.sleep(0.5)

        verify_success(excel, self.select_and_copy_screen(), produto)
    


    def edit_member(self, member,idx):
        pass

    def run(self, excel):
        self.open_java_program()
        self.login()
        self.proceed_to_register_screen()
        screen_text = self.select_and_copy_screen()
        extracted_members = extract_members(screen_text)
        add_or_edit(excel, excel.get_table_data(), extracted_members, self.add_member, self.edit_member)
