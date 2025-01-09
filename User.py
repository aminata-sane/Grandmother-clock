import time
from datetime import datetime, timedelta
# Fonction pour afficher l'heure en temps réel
def display_clock(hours, minutes, seconds):
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
# Programme principal
if __name__ == "__main__":
    # Demander une heure à l'utilisateur
    hours, minutes, seconds = ask_time()
    # Afficher l'horloge en temps réel avec l'heure réglée
    display_clock(hours, minutes, seconds)



    

