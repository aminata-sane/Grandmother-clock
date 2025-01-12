import time
from datetime import datetime, timedelta  

# ------------1.Fonction pour demander l'heure à temps réel------------
def display_clock():
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print(current_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAnother option.")

# Function to display user-set time
def display_time(hours, minutes, seconds):
    print("The clock starts with the set time...")
    now = datetime.now().replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
    try:
        while True:
            #Afficher l'heure actuelle
            current_time = now.strftime("%H:%M:%S")
            print(current_time, end="\r")
            now += timedelta(seconds=1)
            time.sleep(1)
    except KeyboardInterrupt:     
        print("\nClock stopped by user.")

# ------------2.Fonction pour demander l'heure à l'utilisateur------------
def ask_time():
    while True: 
        try:
            hours = int(input("Enter the hour (0-23): "))
            minutes = int(input("Enter the minutes (0-59): "))
            seconds = int(input("Enter the seconds (0-59): "))
            #Vérifier que les valeurs sont valides
            if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
                print(f"Time set: {hours:02}:{minutes:02}:{seconds:02}")  
                return hours, minutes, seconds
            else:
                print("Error: Please enter valid values for hours (0-23), minutes (0-59), and seconds (0-59).")  
        except ValueError:
            print("Error: Please enter a valid integer.")
  

#------------3.Alarme------------

# ------------4.Function to display 12/24 format------------
def display_format():
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
            
            print(f"\rCurrent time is: {current_time}", end="") #To show the time
            time.sleep(1) #Updating every sec
    except KeyboardInterrupt:
        print("\n The clock Clock is stopped.")

# ------------------------- Pause clock function------------------------------
def horloge_avec_pause():
    is_paused = False   #Before calling the function
    user_input = None

    try:
        while True:
            if not is_paused:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\rCurrent time: {current_time}", end="")
                time.sleep(1)

            user_input = input("\nPress '+' to pause or '-' to resume: ").strip()
            if user_input == "+":
                is_paused = True
                print("\nClock paused.")
                break
            elif user_input == "-":
                is_paused = False
                print("\nClock resumed.")
            else:
                print("\nInvalid input. Please press '+' or '-'.")
    except KeyboardInterrupt:
        print("\nClock stopped.")

# Main Menu
while True:
    print("\nMenu:")
    print("1. See the current time")
    print("2. Offer your own time")
    print("3. Select the alarm time")
    print("4. Select 12/24 format time")
    print("5. Stop the clock")
    print("6. Exit")

    choice = input("Make your choice: ")

    if choice == "1":
        display_clock()
    elif choice == "2":
        hours, minutes, seconds = ask_time()
        display_time(hours, minutes, seconds)
    elif choice == "3":
        print("Alarm functionality not implemented.")
    elif choice == "4":
        display_format()
    elif choice == "5":
        horloge_avec_pause()
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

