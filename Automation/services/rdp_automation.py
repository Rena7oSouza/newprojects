import subprocess
from services.pyautogui_utils import copypaste, pyautoguipress, presstab
import time


class RDPAutomation:
    """
    A class to automate Remote Desktop Protocol (RDP) connections.

    Attributes:
        dns (str): The destination address for the RDP connection.
        rdp_user (str): The username for the RDP session.
        rdp_pass (str): The password for the RDP session.
    """

    def __init__(self, dns, rdp_user, rdp_pass):
        """
        Initialize the RDPAutomation class with connection credentials.

        Parameters:
            dns (str): The remote host (IP or domain).
            rdp_user (str): RDP username (currently unused).
            rdp_pass (str): RDP password.
        """
        self.dns = dns
        self.rdp_user = rdp_user
        self.rdp_pass = rdp_pass

    def connect_rdp(self):
        """
        Open a Remote Desktop session and input the password using automation.

        This method launches the RDP client and automatically pastes the password.
        Username input is currently commented out and not used.
        """
        # Launch RDP connection window
        subprocess.Popen(f"mstsc /v:{self.dns}")
        time.sleep(5)  # Wait for the RDP window to fully load

        # Paste Username (commented out - not in use)
        # copypaste(self.rdp_user)
        # presstab()

        # Paste Password
        copypaste(self.rdp_pass)

        # Press Enter to confirm login
        pyautoguipress("enter", 10)

    def run(self):
        """
        Start the RDP connection process.
        """
        self.connect_rdp()
