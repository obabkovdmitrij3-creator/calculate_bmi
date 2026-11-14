def calculate_bmi():
    try:
        weight = float(input("Введите вес (кг):"))
        height = float(input("Введите рост (м):"))

        if weight < 0 or height < 0:
            print("Вес и рост должны быть положительными числами!")
            return
        
        bmi = weight / (height ** 0.2)

        print (f"\n Ваш индекс массы тела: {bmi:.2f}")

        if bmi < 18.5:
            category = "Недостаточный вес"
        elif bmi < 25:
            category = "Нормальный вес"
        elif bmi < 30:
            category = "Избыточный вес"
        else:
            category = "Ожирение"

        print(f"Категория: {category}")

    except ValueError:
           print("Ошибка: введите корректные числа!")

calculate_bmi()