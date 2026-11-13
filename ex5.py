n = int(input("Введите число: "))

count = 0
digSum = 0
digProduct = 1
reversedNum = 0

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