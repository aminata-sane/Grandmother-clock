from datetime import datetime, timedelta
import time

# Fonction pour demander l'heure au format 24 heures
def ask_time_24h():
    while True: 
        try:
            # Demander l'heure, les minutes et les secondes
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
            print("Error: Please enter a valid integer.") # Nombre entier pour integer

# Fonction pour demander l'heure au format 12 heures (AM/PM)
def ask_time_12h():
    while True:
        try:
            # Demander l'heure, les minutes et les secondes
            hours = int(input("Enter the hour (1-12): "))
            minutes = int(input("Enter the minutes (0-59): "))
            seconds = int(input("Enter the seconds (0-59): "))
            
           # Vérifier que les valeurs sont valides
            if 1 <= hours <= 12 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
                # Ask for "AM" or "PM"
                period = input("Is it AM or PM? (AM/PM): ").strip().upper()
                if period in ["AM", "PM"]:
                    print(f"Time set: {hours:02}:{minutes:02}:{seconds:02} {period}")
                    return hours, minutes, seconds, period
                else:
                    print("Error: Please enter AM or PM.")
            else:
                print("Error: Please enter valid values for hours (1-12), minutes (0-59), and seconds (0-59).")
        except ValueError:
            print("Error: Please enter a valid integer.") # Nombre entier pour integer

# Fonction pour afficher une horloge en temps réel à partir d'une heure donnée
def real_time_clock(hours, minutes, seconds):
    current_time = datetime.now().replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
    while True:
        print(current_time.strftime("%H:%M:%S"), end="\r")
        current_time += timedelta(seconds=1)
        time.sleep(1)

# Menu principal pour choisir le format de l'heure
def choose_time_format():
    while True:
        print("Choose the time format:")
        print("1. 24-hour format (0-23)")
        print("2. 12-hour format (AM/PM)")
        
        choice = input("Your choice (1/2): ")
        if choice == "1":
            return ask_time_24h()
        elif choice == "2":
            return ask_time_12h()
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")

# Programme principal
if __name__ == "__main__":
    result = choose_time_format()
    if len(result) == 3:  # Format 24 heures
        hours, minutes, seconds = result
    else:  # Format 12 heures
        hours, minutes, seconds, period = result
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0
    real_time_clock(hours, minutes, seconds)


