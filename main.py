from time import sleep
import keyboard


while(True):
    print("Press a key:")
    key_pressed = keyboard.read_key(False)
    print(key_pressed)
    sleep(0.5)
