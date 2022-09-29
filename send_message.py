"""
Developer: @skywalkerSam
Purpose: To automate whatsapp messages
Date: 12022.09.29.14:23:00
"""

import pywhatkit as pwk
import pyfiglet as pfg


def intro():
    title = pfg.figlet_format("Whatsapp  Bot", "doom")
    print(title)


intro()


def send_message():
    try:
        phone_number = input("Enter a Phone Number (+1 9987654321): ")
        whatsapp_message = input("\n Enter the Whatsapp Message (Hello): ")
        hour_time, minute_time = input("\n  Time in Hours only (18): "), input(
            "Time in Minutes only (59): ")
        print("\n\t Please Wait, This won't take long :) \n")
        pwk.sendwhatmsg(phone_number, whatsapp_message, int(
            hour_time), int(minute_time), 5, True, 5)
    except KeyboardInterrupt:
        print("\n\t Operation Cancelled By User :( \n")
    except:
        print("\n\t Something went Wrong, Please Try Again!  :( \n")


if __name__ == '__main__':
    send_message()
