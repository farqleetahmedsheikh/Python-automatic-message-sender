import pywhatkit
import time

# Getting user local time
currentTime = f"Current time is {time.localtime().tm_hour} : {time.localtime().tm_min}"

print(currentTime) # Printing current local time

hour = time.localtime().tm_hour + 1 # setting hours 

# Getting data from user like number and message which to be send
number = input("Enter Number with country code: (+923333333333) : ")
msg = input("Enter message you want to send in Loop ")

# Printing some information about message and others
print(f"Your {msg} message will start transfer from {hour} : 00 to {number} Number")

# Running loop to send messages infinite times
while True:
    pywhatkit.sendwhatmsg(number, msg, hour,0)
    hour += 1
    if hour == 24:
        hour = 0
    time.sleep(3590) # Program will sleep for 3590 seconds and then start again