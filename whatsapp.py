import pywhatkit
import time
import random
import os

msgs = [""] # list where function will be added

# Functions to get messages from user and add them into a list

def input_msg():
    choice = 'y'
    while choice != 'n':
        print("If you want to close the program press CTRL+C")
        msg = input("Enter message you want to send in Loop ")
        msgs.append(msg)

        choice = input("Do you want to add another msg (y/n)").lower()
        os.system("clear")

hour = time.localtime().tm_hour + 1

# Getting user local time
currentTime = f"Current time is {time.localtime().tm_hour} : {time.localtime().tm_min}"

print(currentTime) # Printing current local time

# setting hours 

# Getting data from user like number and message which to be send
number = input("Enter Number with country code: (+923333333333) : ")

input_msg() # Calling function to add messages

# Printing some information about message and others
print(f"Your {msgs} messages will start transfer from {hour} : 00 to {number} Number")

# Running loop to send messages infinite times

while True:
    num = random.randint(2,len(msgs)-1)
    msg = msgs[num]
    pywhatkit.sendwhatmsg(number, msg, hour,00)
    hour += 1
    os.system("clear")
    print("If you want to close the program press CTRL+C")
    if hour == 24:
        hour = 0
    time.sleep(3590) # Program will sleep for 3590 seconds and then start again