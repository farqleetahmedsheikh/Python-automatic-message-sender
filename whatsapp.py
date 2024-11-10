import pywhatkit
import time

currentTime = f"Current time is {time.localtime().tm_hour} : {time.localtime().tm_min}"

print(currentTime)

# hour = time.localtime().tm_hour + 1

# number = input("Enter Number with country code: (+923333333333) : ")
# msg = input("Enter message you want to send in Loop ")

# print(f"Your {msg} message will start transfer from {hour} : 00 to {number} Number")

# while True:
#     pywhatkit.sendwhatmsg(number, msg, hour,0)
#     hour += 1
#     if hour == 24:
#         hour = 0
#     time.sleep(3590)