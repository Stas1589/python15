#print((123 + 23) / 2 * 3
#print("hello world") #prints hello world

# print(500)
# print(type(500))   # INTEGER (INT)
#
# print(123.23)
# print(type(123.0))
# print(123 / 0.5)
#

# print(len("Hello world!"))
# print(type ("Hello World"))   # STRING (srt)
# print(type (""))
# print("123")
#
#
# print(True)
# print(False)
# print(type(True))    #BOOLEAN (bool)
#
# print(None)
# print(type(None))


# print((2 + 5 - b) * 3)
# print(9 / 4)
# print(9 // 4)
# print(9 % 4)   # 4 + 4 = 1
# print(5 ** 2)

# b = 10
# b = b + 10
# B += 10
#
# print(b + 2)

# b = 10
# print(b)
# b =+ 20
# print(b)

# name = "Jack"
# age = 25
# print("Hello " + name ". He is " + str(age) + " years old.")
#
# b = "123"
# print(int(b))

num = ""
# print(bool (num))

import math

# Данные
current_year = 2023
year_of_birth = 1988

code_1 = '354'
code_3 = 132

user_name = 'John'
user_surname = 'Smith'

x = 152
y = 132

# 1. Вычисление возраста
age = current_year - year_of_birth

# 2. Нахождение code_2
remainder = x % y
multiplied = remainder * 13
square_root = math.sqrt(multiplied)
code_2 = int(square_root)  # извлекаем целую часть

# 3. Соединение кода
secret_code = f"{code_1}-{code_2}-{code_3}"

# 4. Вывод строки
print(f"Hello {user_name} {user_surname}. You are {age} years old. Your secret code is {secret_code}.")
