from datetime import datetime, timedelta


users = [
    {'name': 'Богдан', 'birthday': datetime(2023, 6, 28)},
    {'name': 'Володимир', 'birthday': datetime(2023, 6, 20)},
    {'name': 'Дарія', 'birthday': datetime(2023, 7, 1)},
    {'name': 'Олександра', 'birthday': datetime(2023, 6, 26)},
    {'name': 'Іван', 'birthday': datetime(2023, 6, 23)},
    {'name': 'Мирослава', 'birthday': datetime(2023, 6, 21)},
    {'name': 'Олег', 'birthday': datetime(2023, 6, 25)},
    {'name': 'Марія', 'birthday': datetime(2023, 6, 30)},
    {'name': 'Андрій', 'birthday': datetime(2023, 6, 27)},
    {'name': 'Олена', 'birthday': datetime(2023, 6, 29)},
    {'name': 'Святослава', 'birthday': datetime(2023, 6, 22)},
    {'name': 'Ярослав', 'birthday': datetime(2023, 6, 24)},
    {'name': 'Анастасія', 'birthday': datetime(2023, 6, 20)},
    {'name': 'Ростислав', 'birthday': datetime(2023, 6, 23)},
    {'name': 'Ігор', 'birthday': datetime(2023, 6, 24)},
    {'name': 'Катерина', 'birthday': datetime(2023, 6, 30)},
    {'name': 'Михайло', 'birthday': datetime(2023, 6, 22)},
    {'name': 'Олексій', 'birthday': datetime(2023, 6, 25)},
    {'name': 'Юлія', 'birthday': datetime(2023, 6, 27)},
    {'name': 'Віктор', 'birthday': datetime(2023, 6, 21)},
    {'name': 'Наталія', 'birthday': datetime(2023, 6, 28)},
    {'name': 'Богдана', 'birthday': datetime(2023, 7, 3)},
    {'name': 'Олександр', 'birthday': datetime(2023, 6, 30)},
    {'name': 'Ірина', 'birthday': datetime(2023, 7, 2)},
    {'name': 'Юрій', 'birthday': datetime(2023, 7, 5)},
    {'name': 'Олег', 'birthday': datetime(2023, 7, 3)},
    {'name': 'Анна', 'birthday': datetime(2023, 7, 1)},
    {'name': 'Василь', 'birthday': datetime(2023, 7, 2)},
    {'name': 'Марина', 'birthday': datetime(2023, 7, 4)},
    {'name': 'Оксана', 'birthday': datetime(2023, 7, 7)},
    {'name': 'Петро', 'birthday': datetime(2023, 7, 9)},
    {'name': 'Олена', 'birthday': datetime(2023, 7, 6)},
    {'name': 'Іванна', 'birthday': datetime(2023, 7, 8)},
    {'name': 'Олексій', 'birthday': datetime(2023, 7, 3)},
    {'name': 'Марія', 'birthday': datetime(2023, 7, 5)},
    {'name': 'Михайло', 'birthday': datetime(2023, 7, 10)},
    {'name': 'Анастасія', 'birthday': datetime(2023, 7, 12)},
    {'name': 'Володимир', 'birthday': datetime(2023, 7, 15)},
    {'name': 'Оксана', 'birthday': datetime(2023, 7, 13)},
    {'name': 'Петро', 'birthday': datetime(2023, 7, 17)},
    {'name': 'Олександр', 'birthday': datetime(2023, 7, 14)},
    {'name': 'Марія', 'birthday': datetime(2023, 7, 11)},
    {'name': 'Василь', 'birthday': datetime(2023, 7, 16)},
    {'name': 'Анна', 'birthday': datetime(2023, 7, 18)},
    {'name': 'Іван', 'birthday': datetime(2023, 7, 20)},
    {'name': 'Олена', 'birthday': datetime(2023, 7, 23)},
    {'name': 'Микола', 'birthday': datetime(2023, 7, 25)},
    {'name': 'Софія', 'birthday': datetime(2023, 7, 28)},
    {'name': 'Андрій', 'birthday': datetime(2023, 7, 22)},
    {'name': 'Марина', 'birthday': datetime(2023, 7, 24)},
    {'name': 'Оксана', 'birthday': datetime(2023, 7, 26)},
    {'name': 'Петро', 'birthday': datetime(2023, 7, 29)},
    {'name': 'Олександр', 'birthday': datetime(2023, 7, 21)},
    {'name': 'Юлія', 'birthday': datetime(2023, 7, 30)}
    ]


def birthdays_per_week(users):
    today = datetime.today().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    birthdays = {}
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        
        if start_of_week <= birthday <= end_of_week:
            weekday = weekday_names[birthday.weekday()]
            if weekday not in birthdays:
                birthdays[weekday] = []
            birthdays[weekday].append(name)
    
    for weekday, names in birthdays.items():
        names_str = ', '.join(names)
        print(f"{weekday}: {names_str}")

birthdays_per_week(users)
