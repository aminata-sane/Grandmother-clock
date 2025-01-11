import time
from datetime import datetime, timedelta  

# --------------------1. Fonction pour afficher l'heure à temps réelle---------------------
def display_clock():
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(current_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Another option")
# if __name__ == "__main__":
    
# -------------------2. Fonction pour afficher l'heure en temps réel--------------------------
def display_time(hours, minutes, seconds):
    print("The clock starts with the set time...")
    now = datetime.now().replace(hour=hours, minute=minutes, second=seconds, microsecond=0)

    while True:
         # Afficher l'heure actuelle
        current_time = now.strftime("%H:%M:%S")
        print(current_time, end="\r")
        now += timedelta(seconds=1)
        time.sleep(1)
# Fonction pour demander une heure à l'utilisateur
def ask_time():
    while True: 
        try:
            hours = int(input("Enter the hour (0-23): "))
            minutes = int(input("Enter the minutes (0-59): "))
            seconds = int(input("Enter the seconds (0-59): "))
            # Vérifier que les valeurs sont valides
            if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
                print(f"Time set: {hours:02}:{minutes:02}:{seconds:02}")  
                return hours, minutes, seconds
            else:
                print("Error: Please enter valid values for hours (0-23), minutes (0-59), and seconds (0-59).")  
        except ValueError:
            print("Error: Please enter a valid integer.")       
 # Demander une heure à l'utilisateur
hours, minutes, seconds = ask_time()
# Afficher l'horloge en temps réel avec l'heure réglée
# Programme principal
# if __name__ == "__main__":

# -------------------3. Alarme---------------------------


# --------------------4. Select 12/24 format time--------------------------------
def display_format():
    # Select the time
    valid_formats = ("12", "24") 
    time_format = input("Select the time format (12 or 24): ").strip()
    
    while time_format not in valid_formats:
        print("You didn't select the format. Try again")
        time_format = input("Select the time format (12 or 24): ").strip()
    
    print(f"You selected {time_format}.")
    
    # Cycle d'horloge de base
    try:
        while True:
            now = datetime.now()

            if time_format == "12":
                current_time = now.strftime("%I:%M:%S %p")  # am/pm format
            else:
                current_time = now.strftime("%H:%M:%S")  # 24-format
            
            print(f"\rCurrent time is: {current_time}", end="")  # To show the time
            time.sleep(1)  # Updating every sec
    except KeyboardInterrupt:
        print("\nThe clock is stopped")


#-------------------------------- Stop clock------------------------------
def horloge_avec_pause():
    is_paused = False  # Before calling the function 
    user_input = None
    
    try:
        while True:
            if not is_paused:
                user_input = input("\nPress '+' to pause the clock or '-' to resume: ").strip()
            # Current time
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\rCurrent time : {current_time}", end="\r") 
                time.sleep(1) 
            else:
                print("\r The clock is paused. ", end="" )

        # Input verification

            if user_input == "+":
                print("\nThe clock is paused.")
                is_paused = True  # Stop the clock
                break
            if user_input == "-":
                is_paused = False  # Restore the clock
                user_input = None
            
            # Loop to update time after pressing "-"
                while not is_paused:  # Цикл для нарахування секунд
                    now = datetime.now()  
                    current_time = now.strftime("%H:%M:%S")
                    print(f"\rCurrent time : {current_time}", end="")
                    time.sleep(1)  
                           
        
            else:
                print("\nInvalid entry. Try again.")
    except KeyboardInterrupt:
        user_input = input("\nPress '+' to pause the clock or '-' to resume: ").strip()
        



    

# ----------------------------Menu-----------------------------
while True:
    print("\nMenu:")
    print("See the curent time - press 1: ")
    print("Offer your own time - press 2: ")
    print("Select the alarm time - press 3: ")
    print("Select 12/24 format time - press 4: ")
    print("Stop the clock - press 5: ")

    choise = input ("Make your choise: ")

    if choise == "1":
        display_clock()
    elif choise == "2":
        display_time(hours, minutes, seconds)
    elif choise == "3":
        print("alarm()")
    elif choise == "4":
        display_format()
    elif choise == "5":
        horloge_avec_pause()
    else:
        print("Invalid choice. Please try again.")

display_format()

# Function call to stop the clock
horloge_avec_pause()
