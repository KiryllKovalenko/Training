"""Ex. 5
Написать ф-ю, которая выводит сегодн дату, текущее время и приветствие."""
from datetime import datetime
def current_time():
    current_date = datetime.now()
    print(f"Привет пользователь.Сейчас {current_date}")
current_time()
