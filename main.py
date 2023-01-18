import keyboard
from time import sleep
go_out = True
while(go_out):
    print("Press a key:")
    key_pressed = keyboard.read_hotkey(False)
    print(key_pressed)
    sleep(0.5)
    if(key_pressed == 'ctrl+shift+backspace'):
        print("Exited the application")
        sleep(0.5)
        go_out = False
