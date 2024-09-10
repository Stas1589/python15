# age = 20
#
# if age > 0:
#     if age >= 10:
#         print('He is a child.')
#     elif age < 18:
#         print('He is a teenager')
#     else:
#         print('He is adult.')
# else:
#     print('Check your age!')
#
#     print('Good bye!')

# username = input('Enter your username: ')
# if username:
#     print(f'Hello {username}')
# else:
#     print('Hello stranger')

# idcode = '38803160272'
# if idcode.isdecimal():
#     print(idcode)
#     print(type(idcode))
#     if len(idcode) != 11:
#     if len(idcode) < 11:
#         print('ID you entered is not 11 digits long!')
# else:
#     print('ID is correct')
# else:
# print('ID you entered is not numeric!')

#
# age = 20
#
#
#     if age <= 10 and > 0:
#         print('He is a child.')
#     if age < 18:
#         print('He is a teenager')
#     if: age >= 18:
#         print('He is adult.')
#
# numbers = range(0, 101)
# # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# odds = []
# evens = []
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)
#
#         print(odds)
#         print(evens)

# names = ['Jack', 'Samantha', 'Sarah', 'Bob', 'Simon']
#
# for name in names:
#     print(f'Hello {name}')

# people = [
#     ['Jack', 34, 'm'],
#     ['Samantha', 20, 'f'],
#     ['Sarah', 27, 'f'],
#     ['Bob', 16, 'm'],
#     ['Simon', 42, 'm'],
#     ]
# # for person in people:
# #     if person[2] == 'm':
# #         print(f'This is {person[0]}. He is {person[1]} years old')
# #     elif person[2] == 'f':
# #         print(f'This is {person[0]}. She is {person[1]} years old')
#
# for name, age, gender in people:
#     if gender == 'm':
#         print(f'This is {name}. He is {age} years old')
#     elif gender == 'f':
#         print(f'This is {name}. She is {age} years old')

# while True:
#     idcode = input('Please enter your national id ')
#     if idcode.isdecimal():
#
#         if len(idcode) != 11:
#         if len(idcode) < 11:
#             print('ID you entered is not 11 digits long!')
#
#     else:
#         print('ID is correct')
#     else:
#     print('ID you entered is not numeric!')
#     continue
#
#     print('Good bye')

# try:
#     # int('123')
#     # 5/0
# name = input('Enter name: ')
# if not name:
#     raise  Exception
# except ValueError:
#     print('Can\'t convert to int.')
#     except ZeroDivisionError:
# print('Dont divide by 0')
# except
# else:
#     print('NO ERROR')
#
# finally:
#     print('Good bye!')