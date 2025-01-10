import time
from datetime import datetime

def horloge_avec_pause():
    is_paused = False  # Before calling the function 
    user_input = None
    
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
        # Вихід з циклу, якщо буде нове введення
                # if input("\nPress '+' to pause the clock or '-' to continue: ").strip() == "+":
                #     print("\nThe clock is paused.")
                #     is_paused = True
                #     break
            
            
        else:
            print("\nInvalid entry. Try again.")

# Function call
horloge_avec_pause()