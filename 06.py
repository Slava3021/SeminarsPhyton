# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 ->no
ticketNumber = int(input("Ведите номер билета (целое шестизначное число)"))
a = ticketNumber
summa1 = 0
while a > ticketNumber//1000:
    summa1 = summa1 + a%10
    a = a//10
b = ticketNumber//1000
summa2 = 0
while b > 0:
    summa2 = summa2 + b%10
    b = b//10
if summa1==summa2:
    print("Yes")
else:
    print("NO")

    
