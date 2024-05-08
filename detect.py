import platform

def detect_os():
    os_name = platform.system()
    if os_name == 'Windows':
        return 1
    elif os_name == 'Linux':
        return 2
    else:
        return 0