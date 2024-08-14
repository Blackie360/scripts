import pyautogui
import webbrowser
import time

# Set the target WhatsApp number and the message
target_number = "+254703198968"
message = "Your message here"

try:
    # Step 1: Open WhatsApp Web directly with the target number
    webbrowser.open("https://web.whatsapp.com/send?phone=" + target_number)
    print("WhatsApp Web opened successfully.")

    # Step 2: Wait for WhatsApp Web to load and allow time for manual login if needed
    time.sleep(30)  # Adjust this if your system needs more time

    # Step 3: Ensure the browser window is in focus (this step may vary based on your OS)
    print("Typing the message...")
    pyautogui.click()  # Click on the browser window to bring it into focus
    time.sleep(5)  # Small delay to ensure focus
    
    # Step 4: Type the message and send it
    pyautogui.write(message)
    time.sleep(20)  # Wait before sending
    pyautogui.press("enter")
    
    print("Message successfully sent!")

except Exception as e:
    print(f"An error occurred: {str(e)}")
