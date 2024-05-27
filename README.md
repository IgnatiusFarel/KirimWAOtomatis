---

# WhatsApp Message Automation

This project allows you to automate sending WhatsApp messages using Python libraries.

## Requirements

Make sure you have installed the necessary libraries. You can install them using the following commands in the terminal (CMD or VSCode):

### Step 1: Install `pywhatkit`
```sh
pip install pywhatkit
```

### Step 2: Install `flask`
```sh
pip install flask
```

### Step 3: Install `pyautogui`
```sh
pip install pyautogui
```

## How to Use

1. **Enter the Target Phone Number, Your Message, and the Time:**
   - Provide the target phone number.
   - Enter the message you want to send.
   - Specify the time (hour and minute) in 24-hour format. For example, `23, 23` for 11:23 PM.

2. **Run the File:**
   - If there is no Run Code icon, you can run the file using `Ctrl+Alt+N`.
   - If you do not have the Code Runner extension installed, you can install it from the VSCode Extensions Marketplace.

## Example

Here is an example of how to use the script:

```python
import pywhatkit as kit

# Send a WhatsApp message to the target phone number at 23:23 (11:23 PM)
kit.sendwhatmsg("+1234567890", "Hello, this is an automated message!", 23, 23)
```

## Note

- Make sure your computer has internet access.
- Ensure WhatsApp Web is logged in on your default browser.
- The script will open WhatsApp Web and send the message automatically at the specified time.

---
