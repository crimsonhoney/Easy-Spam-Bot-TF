
import time

limit = int(input("Enter the number of messages: "))
message = input("Enter the spam message: ")

# Warte 5 Sekunden, um WhatsApp zu öffnen und den Cursor auf das Nachrichteneingabefeld zu setzen
time.sleep(5)

i = 0
while i < limit:
    pt.typewrite(message)  # Die Nachricht wird an der Cursorposition eingegeben
    pt.press("enter")  # Nachricht senden durch Drücken der Eingabetaste
    i += 1
