# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions


import fractions

first_fraction = str(input('Введите дробь вида a/b '))
second_fraction = str(input('Введите еще одну дробь вида a/b '))
f_1 = fractions.Fraction(int(first_fraction[0]),int(first_fraction[2]))
f_2 = fractions.Fraction(int(second_fraction[0]),int(second_fraction[2]))
sum_fraction = f_1 + f_2
mult_fraction = f_1 * f_2
print(f'сумма дробей {first_fraction} и {second_fraction} равна {sum_fraction}')
print(f'произведение дробей {first_fraction} и {second_fraction} равно {mult_fraction}')
