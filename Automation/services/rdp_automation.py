import pyautogui
import subprocess
import time
import pyperclip

class RDPAutomation:

    def __init__(self, dns, rdp_user, rdp_pass):
        self.dns = dns
        self.rdp_user = rdp_user
        self.rdp_pass = rdp_pass

    def connect_rdp(self):
        print("Iniciando conexão RDP...")
        subprocess.Popen(f"mstsc /v:{self.dns}")
        time.sleep(5)

        # Paste User
        #pyperclip.copy(self.rdp_user)
        #pyautogui.hotkey("ctrl", "v")
        #pyautogui.press("tab")

        # Paste PassWord
        pyperclip.copy(self.rdp_pass)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        print("Credenciais inseridas...")

        # Wait login
        time.sleep(10)

    
    def run(self):
        self.connect_rdp()
        print("Java program iniciado via RDP.")
