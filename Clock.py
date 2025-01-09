import time
# Fonction pour afficher l'heure à temps réelle
def display_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(current_time, end="\r")
        time.sleep(1)
if __name__ == "__main__":
    display_clock()
  





          



