try:
    number = int(input("Введите число: "))

    sumDel = 0
    for i in range(1, number):
        if number % i == 0:
            sumDel += i

    if sumDel == number:
        print(f"число {number} - совершенное")
    else:
        print(f"число {number} - не совершенное")

except ValueError:
    print("Ошибка: нужно ввести целое число")