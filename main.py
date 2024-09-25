from datetime import datetime


# Функція для виведення всіх значень словника
def print_students(students):
    if not students:
        print("Словник порожній.")
        return

    # Виводимо заголовки для таблиці
    print(f"{'Прізвище та Ім\'я'.ljust(25)} {'По батькові'.ljust(15)} {'Дата народження'}")
    print("-" * 65)

    # Виводимо дані про кожного студента
    for key, value in students.items():
        surname_name = key.ljust(25)
        patronymic = value['По батькові'].ljust(15)
        birth_date = value['дата народження'].strftime("%Y-%m-%d")
        print(f"{surname_name} {patronymic} {birth_date}")

    print("-" * 65)


# Функція для додавання нового запису до словника з перевіркою
def add_student(students):
    surname = input("Введіть прізвище: ")
    if not surname.isalpha():
        print("Прізвище повинно містити лише літери.")
        return

    name = input("Введіть ім'я: ")
    if not name.isalpha():
        print("Ім'я повинно містити лише літери.")
        return

    patronymic = input("Введіть по батькові: ")
    if not patronymic.isalpha():
        print("По батькові повинно містити лише літери.")
        return

    birth_date = input("Введіть дату народження (рік-місяць-день): ")
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    except ValueError:
        print("Неправильний формат дати. Використовуйте рік-місяць-день.")
        return

    key = surname + " " + name

    # Перевірка, чи існує вже запис про цього учня
    if key in students:
        print(f"Запис про {surname} {name} вже існує.")
        return

    # Додавання нового запису
    students[key] = {
        'Прізвище': surname,
        "Ім'я": name,
        'По батькові': patronymic,
        'дата народження': birth_date
    }
    print(f"Новий запис про {surname} {name} додано.")


# Функція для видалення запису зі словника
def delete_student(students):
    surname = input("Введіть прізвище учня, якого потрібно видалити: ")
    name = input("Введіть ім'я учня, якого потрібно видалити: ")
    key = surname + " " + name

    if key in students:
        del students[key]
        print(f"Запис про {key} видалено.")
    else:
        print("Запис не знайдено.")


# Функція для перегляду вмісту словника за відсортованими ключами
def view_sorted_students(students):
    if not students:
        print("Словник порожній.")
        return

    sorted_keys = sorted(students.keys())

    print(f"{'Прізвище та Ім\'я'.ljust(25)} {'По батькові'.ljust(15)} {'Дата народження'}")
    print("-" * 70)

    for key in sorted_keys:
        student = students[key]
        surname_name = key.ljust(25)
        patronymic = student['По батькові'].ljust(15)
        birth_date = student['дата народження'].strftime("%Y-%m-%d")
        print(f"{surname_name} {patronymic} {birth_date}")

    print("-" * 65)

# Функція для перевірки, чи є в класі учні з днем народження сьогодні
def check_birthdays_today(students):
    today = datetime.now().date()
    found = False
    for key, value in students.items():
        if value['дата народження'].month == today.month and value['дата народження'].day == today.day:
            print(f"{value["Ім'я"]} {value['Прізвище']} сьогодні святкує день народження!")
            found = True
    if not found:
        print("Сьогодні немає іменинників.")


def main():
    students = {
        "Барна Лариса": {'Прізвище': 'Барна', "Ім'я": 'Лариса', 'По батькові': 'Тимурівна',
                        'дата народження': datetime(2000, 7, 24).date()},
        "Тащук Забава": {'Прізвище': 'Тащук', "Ім'я": 'Забава', 'По батькові': 'Іванівна',
                        'дата народження': datetime(2002, 10, 13).date()},
        "Ейбоженко Держислав": {'Прізвище': 'Ейбоженко', "Ім'я": 'Держислав', 'По батькові': 'Ярославович',
                        'дата народження': datetime(1999, 3, 29).date()},
        "Стрижак Йомер": {'Прізвище': 'Стрижак', "Ім'я": 'Йомер', 'По батькові': 'Устимович',
                        'дата народження': datetime(2008, 5, 30).date()},
        "Яримович Нонна": {'Прізвище': 'Яримович', "Ім'я": 'Нонна', 'По батькові': 'Адріанівна',
                        'дата народження': datetime(2107, 2, 7).date()},
        "Нагнибіда Ярослава": {'Прізвище': 'Нагнибіда', "Ім'я": 'Ярослава', 'По батькові': 'Пилипівна',
                           'дата народження': datetime(1156, 11, 22).date()},
        "Цимбалюк Малик": {'Прізвище': 'Цимбалюк', "Ім'я": 'Малик', 'По батькові': 'Любомирович',
                           'дата народження': datetime(2056, 8, 12).date()},
        "Дунець Улита": {'Прізвище': 'Дунець', "Ім'я": 'Улита', 'По батькові': 'Сарматівна',
                           'дата народження': datetime(1698, 6, 19).date()},
        "Таранченко Есмеральда": {'Прізвище': 'Таранченко', "Ім'я": 'Есмеральда', 'По батькові': 'Артурівна',
                           'дата народження': datetime(1834, 4, 30).date()},
        "Компанець Забава": {'Прізвище': 'Компанець', "Ім'я": 'Забава', 'По батькові': 'Пилипівна',
                           'дата народження': datetime(1543, 12, 1).date()}
    }

    while True:
        print("\nМеню:")
        print("1. Вивести всі значення словника")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Переглянути словник за відсортованими ключами")
        print("5. Перевірити іменинників")
        print("6. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            print_students(students)
        elif choice == '2':
            add_student(students)
        elif choice == '3':
            delete_student(students)
        elif choice == '4':
            view_sorted_students(students)
        elif choice == '5':
            check_birthdays_today(students)
        elif choice == '6':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()