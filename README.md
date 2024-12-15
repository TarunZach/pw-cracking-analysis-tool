# Cyber Security Password Analyzer

A simple password analysis tool built with Python's Tkinter for GUI-based interaction. The application demonstrates different actions like simulating brute force attacks, dictionary attacks, and generating rainbow tables.

## Project Structure

```
Cyber Security Password Analyzer/
|
|-- Main.py   # Main application script
|-- README.md              # Documentation
```

## Code Structure

The `Main.py` script includes the following key components:

### 1. **PasswordAnalysisTool Class**

- **Purpose**: Manages the main GUI application logic.
- **Methods**:
  - `__init__(self, root)`: Initializes the application window and UI.
  - `create_ui(self)`: Creates the user interface components.
  - `perform_brute_force_action(self)`: Simulates a brute force attack action.
  - `perform_dictionary_attack_action(self)`: Executes a dictionary attack action.
  - `perform_rainbow_table_action(self)`: Simulates rainbow table generation.

### 2. **Main Execution**

- The script initializes the `PasswordAnalysisTool` class and starts the Tkinter event loop.

## How to Run

1. **Install Python**: Ensure Python 3.x is installed on your system.

2. **Run the Script**:
   ```bash
   python Main.py
   ```

3. **Interact with the GUI**:
   - Use the buttons to perform actions and observe outputs in the text box.

## Example Output

After clicking on the "Brute Force" button, the following text is displayed in the text box:
```
Simulating Brute Force Attack...

