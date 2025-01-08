# now = datetime.time.now()
# current_time = now
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")

# print("Current Time =", current_time)

# import time
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# for t in range (time):
    # while True:
        # print(current_time)


# Exercsise 1 + 3
# Showing current time
import time
def show_time_and_alarm():
    alarme = None
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print( current_time,  end="\r")
# Adding alarm time
        if alarme is None:
            alarme = input ("\n Select the alarm time in format XX:XX:XX : ").strip()
            print(f"Your alarm time {alarme} is confirmed.")
            
        elif current_time == alarme:
            print("\n It's time to wake up")
            break
        time.sleep(1)
show_time_and_alarm()




# Exercsise 1
# def showTime ():
    #  while True:
        #  current_time = time.strftime("%H:%M:%S", time.localtime())
        #  print(current_time, end="\r")
        #  time.sleep(1)
# showTime()

# Exercise 2
# import time
# def display_time (formatTime):
    # hours,minutes,seconds = formatTime
    # input ("Your Time :")
# while True:
        # current_time = time.strftime("%H:%M:%S:", time.localtime())
        # print(current_time, end="\r")
        # time.sleep(1)
# display_time()

# new_time = list(hh, mm, ss)


# Exercise 3
# import time
# import threading
# def display_time():
    #  alarme = input("Select the alarm time in format XX:XX : ").strip()
    #  print( f"Your alarm time {alarme} is confirmed.")
    #  while True:
        #  current_time = time.strftime("%H:%M:%S")
        #  if current_time == alarme:
            #  print("\n It's time to wake up")
            #  break
        #  time.sleep(1)
# display_time () 

