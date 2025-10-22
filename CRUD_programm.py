employees = []
print("1. Добавить сотрудника \n2. Вывести список всех сотрудников \n3. Найти сотрудника по ID \n4. Выйти")
while True:
    x = input("Выберите: ")
    if x == '1':
        name = input("Введите имя сотрудника: ")
        ID = input("Введите id сотрудника: ")
        position= input("Введите должность сотрудника: ")
        salary = input("Введите зарплату сотрудника: ")
        employees.append({
            'name': name,
            'id': ID,
            'position': position,
            'salary': salary
        })
    elif x == '2':  
        if not employees:
            print("Список пуст")
        else:
            print("Список сотрудников: ")
            for employee in employees:
                print(f"Имя: {employee['name']}\nID: {employee['id']}\nПозиция: {employee['position']}\nЗарплата: {employee['salary']}")
    elif x == '3':
        find = input("Введите id сотрудника: ")
        found = False
        for employee in employees:
            if (employee['id']) == find:
                print(f"Сотрудник найден, его имя - {employee['name']}")
                found = True
                break
        if not found:
                print("Сотрудник не найден")
    elif x == '4':
        print("Выход из программы")
        break
