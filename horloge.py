import time

# Функція для відображення поточного часу
def afficher_heure():
    while True:
        # Отримуємо поточний час
        current_time = time.strftime("%H:%M:%S", time.localtime())
        # Виводимо час на екран
        print(current_time, end="\r")
        time.sleep(1)  # Затримка в 1 секунду, щоб оновлювати час кожну секунду

# Функція для зміни часу
def regler_heure(heure):
    # Функція приймає час у вигляді кортежу (години, хвилини, секунди)
    # і повертає відформатований рядок
    new_time = time.mktime(time.strptime(f"{heure[0]}:{heure[1]}:{heure[2]}", "%H:%M:%S"))
    return new_time

# Функція для встановлення будильника
def alarme(heure_alarm):
    while True:
        # Отримуємо поточний час
        current_time = time.strftime("%H:%M:%S", time.localtime())
        # Перевіряємо, чи співпадає поточний час з часом будильника
        if current_time == f"{heure_alarm[0]:02}:{heure_alarm[1]:02}:{heure_alarm[2]:02}":
            print("Будильник! Час вставати!")
            break
        time.sleep(1)  # Затримка в 1 секунду, щоб перевіряти кожну секунду

# Основна функція
def main():
    print("Програма відображає поточний час. Щоб змінити час або налаштувати будильник, введіть команду.")
    
    # Стартова година
    current_time = (12, 30, 0)  # Стартовий час - 12:30:00

    while True:
        # Виводимо поточний час
        print(f"Поточний час: {current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}")
        
        # Запитуємо користувача, чи хоче він змінити час або налаштувати будильник
        user_input = input("\nВведіть '1' для зміни часу, '2' для налаштування будильника, або 'q' для виходу: ").strip()
        
        if user_input == '1':
            # Запитуємо новий час
            new_hour = int(input("Введіть години: "))
            new_minute = int(input("Введіть хвилини: "))
            new_second = int(input("Введіть секунди: "))
            # Оновлюємо час
            current_time = (new_hour, new_minute, new_second)
            print(f"Час змінено на {current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}")
        
        elif user_input == '2':
            # Запитуємо час для будильника
            alarm_hour = int(input("Введіть години для будильника: "))
            alarm_minute = int(input("Введіть хвилини для будильника: "))
            alarm_second = int(input("Введіть секунди для будильника: "))
            # Налаштовуємо будильник
            alarme((alarm_hour, alarm_minute, alarm_second))
        
        elif user_input == 'q':
            # Виходимо з програми
            print("Вихід з програми.")
            break
        else:
            print("Невірний ввід! Спробуйте ще раз.")

# Запуск основної програми
main()
