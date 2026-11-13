n = int(input("Введите число: "))

original = n
digit = 0
reversedNum = 0

while n > 0:
    digit = n % 10
    reversedNum = reversedNum * 10 + digit
    n //= 10

if original == reversedNum:
    print(f"Число {original} - палиндром")
else:
    print(f"Число {original} - не палиндром")
