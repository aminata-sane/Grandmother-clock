import time
from customtkinter import *
from threading import Thread

# Fonction pour vérifier l'heure de l'alarme
def check_alarm():
    while True:
        current_time = time.strftime("%H:%M:%S")
        selected_time = f"{hour_var.get():02}:{minute_var.get():02}:{second_var.get():02}"
        print(f"Heure actuelle : {current_time} | Heure d'alarme : {selected_time}")  # Affichage dans le terminal
        
        if current_time == selected_time:
            alarm_status.set("🔔 Alarme déclenchée !")
            print("🔔 Alarme déclenchée !")  # Affichage dans le terminal
            break
        time.sleep(1)

# Fonction pour démarrer l'alarme
def start_alarm():
    alarm_status.set("⏳ Alarme activée...")
    print("⏳ Alarme activée...")  # Affichage dans le terminal
    Thread(target=check_alarm, daemon=True).start()

# Initialisation de l'application
app = CTk()
app.geometry("400x300")
app.title("Alarme")

# Cadre principal
frame = CTkFrame(master=app, fg_color="white")
frame.pack(expand=True, fill="both", padx=20, pady=20)

# Titre
label = CTkLabel(master=frame, text="Réveil/Alarme", font=("Arial", 20))
label.pack(pady=10)

# Sélection des heures, minutes et secondes
hour_var = IntVar(value=0)
minute_var = IntVar(value=0)
second_var = IntVar(value=0)

time_frame = CTkFrame(master=frame, fg_color="lightgray")
time_frame.pack(pady=10)

hour_scroll = CTkComboBox(
    master=time_frame,
    values=[f"{i:02}" for i in range(24)],
    variable=hour_var,
    width=80,
    font=("Arial", 16),
    justify="center",
)
hour_scroll.grid(row=0, column=0, padx=5)

minute_scroll = CTkComboBox(
    master=time_frame,
    values=[f"{i:02}" for i in range(60)],
    variable=minute_var,
    width=80,
    font=("Arial", 16),
    justify="center",
)
minute_scroll.grid(row=0, column=1, padx=5)

second_scroll = CTkComboBox(
    master=time_frame,
    values=[f"{i:02}" for i in range(60)],
    variable=second_var,
    width=80,
    font=("Arial", 16),
    justify="center",
)
second_scroll.grid(row=0, column=2, padx=5)

# Bouton pour démarrer l'alarme
btn = CTkButton(master=frame, text="Démarrer l'alarme", command=start_alarm)
btn.pack(pady=10)

# État de l'alarme
alarm_status = StringVar()
alarm_status.set("⏳ En attente...")
status_label = CTkLabel(master=frame, textvariable=alarm_status, font=("Arial", 16), text_color="red")
status_label.pack(pady=20)

# Exécution de l'application
app.mainloop()
