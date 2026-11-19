# запрашиваем число
n = int(input("Введите число: "))

original = n # сохраняем исходное число n
digit = 0 # будем хранить последнюю цифру
reversedNum = 0 # будем хранить перевернутое число

# высчитываем обратное число
while n > 0:
    digit = n % 10
    reversedNum = reversedNum * 10 + digit
    n //= 10

# проверка является ли число палиндромом
if original == reversedNum:
    print(f"Число {original} - палиндром")
else:
    print(f"Число {original} - не палиндром")
