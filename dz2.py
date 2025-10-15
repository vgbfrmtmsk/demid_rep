number = int(input("Введите число до 100: "))

if number < 0 or number > 100:
    print("Число должно быть от 0 до 100")
else:
    tens = number // 10
    units = number % 10

    print(f"Число {number} состоит из:")
    print(f"Десятков: {tens}")
    print(f"Единиц: {units}")