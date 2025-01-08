
import time

def combined_show_time_and_alarm():
    alarme = None  # Змінна для збереження часу будильника

    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(current_time, end="\r")
        
        if alarme is None:  # Якщо будильник ще не встановлений
            alarme = input("\n Set the alarm time in format HH:MM:SS: ").strip()
            print(f"Your alarm time {alarme} is confirmed.")
        elif current_time == alarme:  # Якщо поточний час дорівнює будильнику
            print("\n It's time to wake up!")
            break
        
        time.sleep(1)

combined_show_time_and_alarm()