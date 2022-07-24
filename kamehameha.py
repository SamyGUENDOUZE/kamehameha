from colorama import Fore
import time
from playsound import playsound
import threading

kamehameha_list = ['KA...', 'ME...', 'HA...', 'ME...', 'AHHHHHH!!']

def kamehameha_text():

    for k in kamehameha_list:
        
        time.sleep(1.68)
        
        print(Fore.LIGHTBLUE_EX + k, end="\r")
    print('')
   
    for b in range(10):
        boom = '='
        time.sleep(0.45)
        print(Fore.LIGHTCYAN_EX + b*boom, end="\r")
        if b == 9 : 
            print(b*boom +'))))))')
        
def kamehameha_sound():
            playsound('kamehameha_sound.mp3')

th1 = threading.Thread(target=kamehameha_text)
th2 = threading.Thread(target=kamehameha_sound)


th1.start()
th2.start()

th1.join()
th2.join()
