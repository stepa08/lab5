# запрашиваем число и переводим в int
n = int(input("Введите число n: "))

sumNum = 0 # будет хранить сумму цифр от 1 до n
factorial = 1 # будет хранить факториал числа n
sumSquare = 0 # будет хранить сумму квадратов от 1 до n

for i in range(1, n + 1):
    sumNum += i
    factorial *= i
    sumSquare += i**2

print(f"Сумма от 1 до n: {sumNum}")
print(f"Факториал n: {factorial}")
print(f"Сумма квадратов: {sumSquare}")
