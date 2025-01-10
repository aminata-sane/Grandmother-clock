# To show the time
# import time
# def showTime ():
#      while True:
#          current_time = time.strftime("%H:%M:%S", time.localtime())
#          print(current_time, end="\r")
#          time.sleep(1)
# showTime()

# # To suspend the time
# showTime = time.sleep(5) 

# doesn't work
# import time
# from datetime import datetime 

# def stop_clock():
#     valid_choise = ("+", "-")
#     is_paused = False 
#     # suspend_time = input("Voulez-vous arrêter l'horloge ?").strip()

#     while True:
#         now = datetime.now()
#         if not is_paused:
#             current_time = now.strftime("%H:%M:%S")
#             print(current_time, end= "\r")

#         suspend_time = input("Voulez-vous arrêter l'horloge ? (+ - pour arrêter or - pour relancer) : ").strip()

#         if suspend_time not in valid_choise:
#             print ("Choix invalide. Veuillez entrer + ou -.")
        
        
#         if suspend_time == "+":
#             print("Horloge mise en pause.")
#             is_paused = True
#         elif suspend_time == "-":
#             print("Horloge relancée.")
#             is_paused = False
#         # time.sleep(3)
# stop_clock()



import time
from datetime import datetime

def horloge_avec_pause():
    is_paused = False  # Before calling the function 
    print("Press '+' to pause the clock or '-' to resume:")
    user_input = None
    
    while True:
        if not is_paused:
            user_input = None
            # Current time
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\rCurrent time : {current_time}", end="\r") 
            time.sleep(1) 
        else:
            print("\r The clock is paused. ", end="" )

        # time.sleep(5)

        # Request input from the user
        if is_paused:
            user_input = input("\nPress '+' to pause the clock or '-' to resume: ").strip()

        # Input verification
        if user_input == "+":
            print("\nThe clock is paused.")
            is_paused = True  # Stop the clock
            break
        elif user_input == "-":
            print("\nThe clock is restarted.")
            is_paused = False  # Restore the clock
            user_input = None
            current_time = now.strftime("%H:%M:%S")
            time.sleep(1)
            
        else:
            print("\nInvalid entry. Try again.")

# Function call
horloge_avec_pause()

# def stop_clock():
#     valid_choise = ("+", "-")
#     suspend_time = input("Voulez-vous arrêter l'horloge ?").strip()

#     while suspend_time not in valid_choise:
#         current_time = now.strftime("%H:%M:%S", time.localtime())
#         print(current_time, end= "\r")
#         suspend_time = input("Voulez-vous arrêter l'horloge ?").strip()
#     while True:
#         now = datetime.now()
#         if suspend_time == "+":
#             current_time = time.strftime("%H:%M:%S", time.localtime())
#             time.sleep(5)
#         else:
#             current_time = time.strftime("%H:%M:%S", time.localtime())
# stop_clock()