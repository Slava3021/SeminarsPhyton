# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
n = int (input("Введите целое трехзначное число "))
a = n%10
n = n//10
b = n%10
n = n//10
c = n%10
print("Сумма цифр трехзначного числа =", a+b+c)
