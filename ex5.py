# запрашиваем у пользователя число
n = int(input("Введите число: "))


count = 0 # здесь будем хранить количество цифр n
digSum = 0 # будем хранить сумму цифр n
digProduct = 1 # будем хранить произведение цифр n
reversedNum = 0 # это будет перевернуто число

# в цикле высчитываем значения 4 переменных
while n > 0:
    digit = n % 10
    count += 1
    digSum += digit
    digProduct *= digit
    reversedNum = reversedNum * 10 + digit
    n //= 10

print(f"Количество цифр: {count}")
print(f"Сумма цифр: {digSum}")
print(f"Произведение цифр: {digProduct}")
print(f"Число наоборот: {reversedNum}")