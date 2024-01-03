# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.


DIV_HEX = 16

original_num: int = int(input("Введите целое число "))
num = original_num
h = '0123456789abcdef'
result: str = ''
while num > 0:
    result = h[num % DIV_HEX] + result
    num //= DIV_HEX
check = str(hex(original_num))
if result == check[2:]:
    print(f'Число {original_num} в шестнадцатиричной системе {result}')
else:
    print('Что-то пошло не так')



