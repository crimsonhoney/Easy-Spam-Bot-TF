
import time

limit = int(input("Enter the number of messages: "))
message = input("Enter the spam message: ")

# Wait 5 seconds to open WhatsApp and place the cursor on the message input field
time.sleep(5)

i = 0
while i < limit:
    pt.typewrite(message)  # The message is entered at the cursor position
    pt.press("enter")  # Send message by pressing Enter
    i += 1
