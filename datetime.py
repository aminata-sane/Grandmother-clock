# Exercsise 1
import time
def showTime ():
     while True:
         current_time = time.strftime("%H:%M:%S", time.localtime())
         print(current_time, end="\r")
         time.sleep(1)
showTime()

# Exercise 3

# def display_time():
#      alarme = input("Select the alarm time in format XX:XX : ").strip()
#      print( f"Your alarm time {alarme} is confirmed.")
#      while True:
#          current_time = time.strftime("%H:%M:%S")
#          if current_time == alarme:
#              print("\n It's time to wake up")
#              break
#          time.sleep(1)
# display_time () 

# Exercise 2
# import time
# def display_time():
#     print( "It's current time. To change it - press 'Enter'.")
#     your_time = None

#     while True:
#          current_time = time.strftime("%H:%M:%S", time.localtime())
#          if your_time is None:
#             print(f"Current time: {current_time}", end="\r")
#          else:
#             print(f"Set time: {your_time}", end="\r")
#          if input("\nPress Enter to input new time or wait: ").strip() == "":
#             your_time = input("Select time in format XX:XX:XX :").strip()
#             print(f"New time {your_time}")
#          time.sleep(1)
# display_time()


