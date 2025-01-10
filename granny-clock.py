import time
from customtkinter import *
from threading import Thread

# function to verify the hour of alarm
def check_alarm():
    while True:
        current_time = time.strftime("%H:%M:%S")
        selected_time = f"{hour_var.get()}:{minute_var.get()}:{second_var.get()}"
        print(f"actual hour : {current_time} | alarm hour : {selected_time}")  # terminal print
        
        if current_time == selected_time:
            alarm_status.set("🔔 time to wake up !")
            print("🔔 time to wake up !")  # terminal print
            break
        time.sleep(1)

# function to activate the alarm
def start_alarm():
    alarm_status.set("⏳ Alarm activate...")
    print("⏳ Alarm activate...")  # terminal print
    Thread(target=check_alarm, daemon=True).start()

# Initialisation of app
app = CTk()
app.geometry("400x300")
app.title("Alarm")

# main 
frame = CTkFrame(master=app, fg_color="white")
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Title
label = CTkLabel(master=frame, text="wake up/Alarm", font=("Arial", 20))
label.pack(pady=10)

# Selection of hour, minute, second
hour_var = IntVar(value=0)
minute_var = IntVar(value=0)
second_var = IntVar(value=0)

time_frame = CTkFrame(master=frame, fg_color="lightgray")
time_frame.pack(pady=10)

# Scroll the selection hour 
hour_scroll = CTkComboBox(
    master=time_frame,
    values=[f"{i:02}" for i in range(24)],
    variable=hour_var,
    width=80,
    font=("Arial", 16),
    justify="center",
)
hour_scroll.grid(row=0, column=0, padx=5)

# Scroll the selection minute
minute_scroll = CTkComboBox(
    master=time_frame,
    values=[f"{i:02}" for i in range(60)],
    variable=minute_var,
    width=80,
    font=("Arial", 16),
    justify="center",
)
minute_scroll.grid(row=0, column=1, padx=5)

# Scroll the selection second
second_scroll = CTkComboBox(
    master=time_frame,
    values=[f"{i:02}" for i in range(60)],
    variable=second_var,
    width=80,
    font=("Arial", 16),
    justify="center",
)
second_scroll.grid(row=0, column=2, padx=5)

# Button to activate alarm
btn = CTkButton(master=frame, text="activate alarm", command=start_alarm)
btn.pack(pady=10)

# state of alarm
alarm_status = StringVar()
alarm_status.set("⏳ wait please...")
status_label = CTkLabel(master=frame, textvariable=alarm_status, font=("Arial", 16), text_color="red")
status_label.pack(pady=20)

# execution of app
app.mainloop()
