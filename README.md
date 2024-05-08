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

Void Keylogger utilizes several Python modules to achieve its functionality. Here is a breakdown of these modules and the specific functions used:

### `platform` Module
- **Usage:** Determines the operating system on which the keylogger is running.
- **Functions:**
  - `platform.system()`: Used in `detect.py` to identify the OS (Windows or Linux).

### `pynput.keyboard` Module
- **Usage:** Monitors and records every keystroke.
- **Functions:**
  - `Listener`: A class that listens for keyboard events.
  - `Key`: Enumerates special keys (like space, enter, etc.).
  - `KeyCode`: Handles the representation of ordinary alphanumeric keys.
  - `listener.join()`: Ensures that the listener thread continues execution until stopped.
  
### `os` and `sys` Modules
- **Usage:** Used for system-related operations, including file handling and script execution management.
- **Functions:**
  - `os.path.join()`: Constructs paths by joining names into a complete path.
  - `sys.exit()`: Exits the script when needed, especially in error handling.

### `json` Module
- **Usage:** Formats and stores the keystroke data in JSON format for later retrieval and analysis.
- **Functions:**
  - `json.dump()`: Serializes the keystroke data into a JSON formatted stream.
  - `json.load()`: Deserializes JSON data into Python objects.

### `datetime` Module
- **Usage:** Records the timestamp for each keystroke event.
- **Functions:**
  - `datetime.now()`: Returns the current local date and time.

### `logging` Module
- **Usage:** Provides a way to configure logging.
- **Functions:**
  - `logging.basicConfig()`: Configures the logging to handle the output of keystroke logs.
  - `logging.info()`, `logging.warning()`: Used to log informational and warning messages.

Each of these modules is crucial for the efficient and effective operation of the Void Keylogger, providing a range of functionalities from system detection to data logging and error handling.
