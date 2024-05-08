# Void Keylogger

## Cross-Platform Keylogging Tool

Void Keylogger is a sophisticated monitoring tool that can detect the operating system (Windows or Linux) and record every keystroke made on the device. This tool is designed for ethical use, such as parental monitoring or system administration.

### Features

- **OS Detection:** Automatically detects whether it is running on Windows or Linux.
- **Keystroke Logging:** Captures all keystrokes, including special keys like Shift, Backspace, and Enter.
- **Output Customization:** Formats the logged data for readability and easier analysis.
- **Stealth Mode:** Operates invisibly in the background (note: ensure you have proper permissions to use such features).

### Prerequisites

- Python 3.x
- `pynput` library

### Installation

1. Clone the repository or download the `main.py`, `detect.py`, and `file_edit.py` scripts.
2. Ensure that Python 3.x is installed on your system.
3. Install the required Python packages:
   ```bash
   pip install pynput

### To use Void Keylogger, execute the main.py script:
```bash
python main.py
```

## Key Modules and Functions

### `platform` Module
- **File:** [detect.py](detect.py)
- **Function(s) Used:**
  - `platform.system()`: Determines the operating system on which the keylogger is running. Used in the `detect_os()` function to check if the system is Windows or Linux.

### `pynput.keyboard` Module
- **File:** [file_edit.py](file_edit.py)
- **Function(s) Used:**
  - `Listener`: Monitors keyboard events.
  - `on_press`: Callback function that is triggered when a key is pressed. It's linked to the `write_file` function that logs each keystroke.

### `os` Module
- **File:** [main.py](main.py)
- **Function(s) Used:**
  - `os.environ`: Retrieves the path to store the log file based on the operating system.
  - `os.path.join()`: Constructs a full file path intelligently to store the log file, accommodating different OS file path conventions.

### `sys` Module
- **File:** [main.py](main.py)
- **Function(s) Used:**
  - `sys.exit()`: Typically used for interacting with the Python interpreter to terminate the program gracefully if needed (not explicitly mentioned but commonly used).

## Design and Implementation
- **OS Detection**: The `detect_os()` function in `detect.py` utilizes the `platform` system to identify the operating system, which influences where the keylogger will save its log files (Windows: `%appdata%`, Linux: `/root`).
- **Keylogging Logic**: The `file_edit.py` includes the `write_file` function that processes and logs each keystroke. Special keys like 'enter', 'backspace', and 'shift' are formatted specifically for better readability in the logs.
- **Execution and Management**: The `main.py` script sets up the environment based on the detected OS, establishes the log file path, and starts the `Listener` to monitor keystrokes. It ensures the keylogger runs continuously unless manually stopped.
