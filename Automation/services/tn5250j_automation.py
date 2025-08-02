from models.tn5250j_handler import extract_members, add_or_edit, verify_success
from services.pyautogui_utils import pyautoguipress, pyautoguiwrite, pyautoguihotkey, select_and_copy_screen, presstab, copypaste

class TN5250JAutomation:


    def __init__(self, user, password):
        self.user = user
        self.password = password


    def open_java_program(self, path):
        pyautoguihotkey("win", "r")

        pyautoguipress("backspace")

        copypaste(path)
        
        pyautoguipress("enter", 10)



    def login(self):
        # Typing username and password
        pyautoguiwrite(self.user)

        presstab()

        pyautoguiwrite(self.password, 2)

        pyautoguipress("enter", 2)


    def proceed_to_register_screen(self):
        # Navigating through menu to access member list
        pyautoguiwrite("strpdm")

        pyautoguipress("enter")

        pyautoguipress("3")

        pyautoguipress("enter", 2)

        pyautoguiwrite("qcppsrc")

        pyautoguipress("enter", 1)


    def scroll_and_collect_members(self):
        screens = []
        down_count = 0

        while True:
            copied = select_and_copy_screen()
            screens.append(copied)

            if "Bottom" in copied and "More" not in copied:
                break

            pyautoguipress("pagedown", 1)
            down_count += 1

        for _ in range(down_count):
            pyautoguipress("pageup", 1)

        return screens


    def add_member(self, excel, member):
        # Press F6 to Start register
        pyautoguipress("f6", 1)
        # Type Product
        product = member.get("Produto", "").replace(" ", "")
        pyautoguiwrite(product, 0.5)

        presstab(0.5)

        #Type TXT
        pyautoguiwrite("TXT", 0.5)

        # Del function wasn't working, replace by " "
        pyautoguiwrite(" " * 2, 0.2, 0.02)

        pyautoguipress("backspace", 0.05, 2)

        presstab(0.5)

        price = f"valor {member.get('Valor', '0')}"
        if len(price) < 50:
            price += " " * (50 - len(price))
        pyautoguiwrite(price, 1, 0.1)

        # Press Enter
        pyautoguipress("enter")

        #Type Description
        description = member.get("Descrição", "")[:70]
        if len(description) < 70:
            description += " " * (70 - len(description))
            
        pyautoguiwrite(description, 0.5, 0.05)
        #Press Enter
        pyautoguipress("enter")

        #Press F3 
        pyautoguipress("f3")

        #Press Enter
        pyautoguipress("enter",0.5)

        verify_success(excel, select_and_copy_screen(), product, "Add")
    

    def edit_member(self, excel, member,idx, totalidx):
        presstab(0.5, idx*3)

        pyautoguipress("2", 0.5)

        pyautoguipress("enter", 0.5)
        
        presstab(0.5, 3)

        description = member.get("Descrição", "")[:70]
        if len(description) < 70:
            description += " " * (70 - len(description))

        pyautoguiwrite(description, 0.5, 0.05)

        pyautoguipress("enter", 0.5)

        pyautoguipress("F3", 0.5)

        presstab(0.5, 4)

        price = f"valor {member.get('Valor', '0')}"
        if len(price) < 50:
            price += " " * (50 - len(price))

        pyautoguiwrite(price, 0.5, 0.1)

        pyautoguipress("enter", 0.5)

        verify_success(excel, select_and_copy_screen(),member.get("Produto", ""), "Edit")
        self.tostartfield(idx,totalidx)


    def tostartfield(self, currentidx, totalidx):

        totaltabs = (totalidx - currentidx) * 3 + 4
        presstab(0.1, totaltabs)

    def run(self, path, excel):
        self.open_java_program(path)
        self.login()
        self.proceed_to_register_screen()
        screen_text = select_and_copy_screen()
        extracted_members = extract_members(screen_text)
        add_or_edit(excel, excel.get_table_data(), extracted_members, self.add_member, self.edit_member)
