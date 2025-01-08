import time

def display_time ():
    current_time = time.localtime()
    

    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(current_time, end="\r")
        new_time = None
        
        if new_time is None:
            new_time = input("Press Enter to input new time in format HH:MM:SS :").strip()
            print(new_time, end="\r")

            # current_time = time.strftime("%H:%M:%S", time.localtime())
            # print(current_time, end= "\r")
        elif current_time == new_time:
            print (new_time)

        # input("Press Enter to input new time in formet HH:MM:SS :").strip() == "":
            # new_time = newTime()  
        time.sleep(1)
display_time()


# def newTime ():
#     return input("Press Enter to input new time in formet HH:MM:SS :").strip()

# import time

# def afficher_heure(heures, minutes, secondes):
#     """
#     Функція для відображення часу на основі переданого кортежу.
#     Приймає кортеж (heures, minutes, secondes).
#     """
#     # Перетворюємо час у формат, який можна відображати
#     return f"{heures:02}:{minutes:02}:{secondes:02}"

# def display_time():
#     print("Current time is displayed. To set a custom time, press 'Enter'.")

#     your_time = None  # Спочатку часу не задано

#     while True:
#         # Якщо не задано користувачем час, відображається поточний
#         if your_time is None:
#             current_time = time.strftime("%H:%M:%S", time.localtime())
#             print(f"Current time: {current_time}", end="\r")
#         else:
#             # Якщо задано новий час, відображається цей час
#             current_time = afficher_heure(your_time[0], your_time[1], your_time[2])
#             print(f"Time: {current_time}", end="\r")

#         # Запит на введення часу
#         if input("\nPress Enter to input new time or wait: ").strip() == "":
#             your_time_input = input("Select time in format HH:MM:SS: ").strip()
#             try:
#                 # Перевіряємо, чи правильний формат введеного часу
#                 hours, minutes, seconds = map(int, your_time_input.split(":"))
#                 your_time = (hours, minutes, seconds)  # Оновлюємо час
#                 print(f"New time set to: {your_time_input}")
#             except ValueError:
#                 print("Invalid time format. Please use HH:MM:SS.")
#                 continue  # Якщо формат невірний, просимо ввести час знову

#         time.sleep(1)  # Затримка на 1 секунду

# # Виклик функції
# display_time()