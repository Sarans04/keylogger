from pynput.mouse import Controller
# from pynput.keyboard import Controller

def Controlmouse():
    mouse=Controller()
    mouse.position=(200,100)

def Controlkeyboard():
    keyboard=Controller()
    keyboard.type("Hii")

Controlmouse()
# Controlkeyboard()