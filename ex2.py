n = int(input("Введите число n: "))

sumNum = 0
factorial = 1
sumSquare = 0

for i in range(1, n + 1):
    sumNum += i
    factorial *= i
    sumSquare += i**2

print(f"Сумма от 1 до n: {sumNum}")
print(f"Факториал n: {factorial}")
print(f"Сумма квадратов: {sumSquare}")
