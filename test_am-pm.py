import time  

def display_clock():
    # Select the time
    valid_formats = ("12", "24") 
    time_format = input("Select the time format (12 or 24): ").strip()
    
    while time_format not in valid_formats:
        print("You didn't select the format. Try again")
        time_format = input("Select the time format (12 or 24): ").strip()
    
    print(f"You selected {time_format}.")
    
    # Основний цикл роботи годинника
    try:
        while True:
            if time_format == "12":
                current_time = time.strftime("%I:%M:%S %p")  # am/pm format
            else:
                current_time = time.strftime("%H:%M:%S")  # 24-format
            
            print(f"\rCurrent time is: {current_time}", end="")  # To show the time
            time.sleep(1)  # Updating every sec
    except KeyboardInterrupt:
        print("\nThe clock is stopped")

display_clock()