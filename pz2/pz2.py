while True:
    try:
        N = int(input("Введите количество секунд: "))
        minutes = N // 60
        print(f"Количество полных минут: {minutes}")
        break
    except ValueError:
        print("Ошибка: введите целое число!")