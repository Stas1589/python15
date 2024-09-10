# empty = []
# empty = list()
# print(type(empty)) # list()
# print(bool(empty)) # empty list give false value

# x = 10
#
# filled = [123, 0.123, 'hello', x, [1,2,[3,4,5],6], True, True, True]
# print(len(filled))
# print(filled[4][2][1])

# courses = ['History', 'Math', 'Literature', 'Physics', 'Programming']

# print(courses[1:4])
# # print(courses[::-2])
#
# # courses[0] = 'Art'
# # print(courses)
#
# # courses.append('Art')
# # print(courses)
# # courses.insert(0, 'English')
# # print(courses)
#
# # courses.remove('Math')
# # print(courses)
# # courses.pop(0)
# # print(courses)
#
# # print(courses.reverse())
# # print(courses)
#
# # courses.sort()
# # print(courses)
#
# # numbers = [45, 23, 12.32, 9.043, 24]
# # numbers.sort(reverse=True)
# # print(numbers)
#
# # print(min(courses))
# # print(max(courses))
# # print(min('Hello world!'))
# # print(max('Hello world!'))
# # print(sum(courses))
# #
# # a = 'one'
# # b = a
# # a += 'two'
# # print(a, b)
# #
# # a = [1, 2, 3, 4, 5]
# # b = a
# # a.append(555)
# # b.append(777)
# # print(a)
# # print(b)
#
# # empty = ()
# # empty = tuple()
# # print(type(empty)) # tuple()
# #
# # x = (1, )
# # print(type(x))
# #
# # print(courses.count('Math'))
# # print(courses.index('Math'))
# # courses = list(courses)
# # courses.append('Art')
# # courses = tuple(courses)
# # print(courses)
#
# # print([1, 2, 3] + [3, 2, 1])
# # print((1, 2, 3) + (3, 2, 1))
#
# # x = set() # set()
# # print(type(x))
# # courses = {'History', 'Math', 'Literature', 'Physics', 'Programming'}
# # print(courses)
# #
# # courses2 = {'Marh', 'Economics', 'History', 'Spanish'}
# # print(courses.difference(courses2))
# # print(courses2.difference(courses))
# #
# # print(courses.intersection(courses2))
#
#
# # Print to console what is different in each set compared to another
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
#
# # Elements in set_a but not in set_b
# print("Elements in set_a but not in set_b:", set_a - set_b)
#
# # Elements in set_b but not in set_a
# print("Elements in set_b but not in set_a:", set_b - set_a)
#
# # Create a string from a list and save it to a variable
# # Make each name on a new line.
# names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
# names_string = "\n".join(names)
# print("Names string:\n", names_string)
#
# # Print sum of all numbers in a list
# numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
# print("Sum of all numbers:", sum(numbers))
#
# # Print sum of all unique numbers in a list
# unique_numbers = set(numbers)
# print("Sum of all unique numbers:", sum(unique_numbers))

# Create a new list from studentsA and studentsB
# Make sure there are no duplicates in the new list
# studentsA = ['Jack', 'Bob', 'Mary']
# studentsB = ['Bob', 'Sarah', 'Simon']
# unique_students = list(set(studentsA + studentsB))
# print("Unique students list:", unique_students)
#
# # What elements are common for both tuples?
# numbersA = (23, 52, 12, 75, 42)
# numbersB = (75, 22, 42, 94, 70)
# common_elements = set(numbersA) & set(numbersB)
# print("Common elements in both tuples:", common_elements)
#
# # Add 5 to the tuple in the correct position
# a = (1, 2, 3, 4, 6, 7)
# a = a[:4] + (5,) + a[4:]
# print("Tuple after adding 5:", a)

# x = 5
# sample = {
#     'name': 'Jack',
#     'courses' : ['Art', 'English', 'Programming'],
#     1: 'int key',
#     0.2: 'float key',
#     x: 'variable key',
#     'dictinary' : {'name': 'Bob', 'surname': 'Smith'},
# }
# # print(sample['courses'])
# print(sample.get('fyufuffuyf', False))

# sample['name'] = 'Sarah'
# sample['phone'] = '555-555-5555'
# print(sample)
#
# sample.update({'name': 'Bob', 'address': 'Tallinn'})
# print(sample)
# del sample ['name']
# print(sample)
#
# courses = sample.pop('courses')
# print(courses)
# print(sample)

# sample2 = {'name': 'Jack', 'surname': 'Smith', 'age': 40}
# for x in sample2:
#     print(sample2[x])
#
#     print(sample2.keys())
#     print(sample2.values())
#     print(sample2.items())
#
#     for key, value in sample2.items():
#         print(key, value)

# def say_Hello(name, surname):
#     print(f'Hello {name} {surname}!')
#
# x = say_Hello('Roman', 'Kutselepa')
# print(x)

# def short_or_long(string):
#     if len(string) > 5:
#         return  'long'
#     else:
#         return  'short'
#
# print(short_or_long('Interstellar'))
#
# words = ['Sun', 'Earth', 'Millenium', 'People', 'World']
# for word in words:
#     print(short_or_long(word))


# def fizz_buzz(start, end):
#     for num in range(start, end + 1):
#         if num % 3 == 0 and num % 5 == 0:
#             print(num, 'FIZZBUZZ')
#         elif num % 3 == 0:
#             print(num, 'FIZZ')
#         elif num % 5 == 0:
#             print(num, 'BUZZ')
#
# fizz_buzz(-100, 200)

# a = 1
# b = 2
# c = 3
# def sample():
#     a = 10
#     b = 20
#     c = 30
#     print(a, b, c)
#
# print(a, b, c)
# sample()

# def traingle_area(a, b, c):
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p -b)) ** 0.5
#     return area
#
# def print_result():
#     print(f'The area of triangle is {traingle_area(3, 4, 5 )} cm2')
#
# print_result()
#
# def sum_two_or_three(a, b, c=0):
#     a = int(a)
#     return a + b + c
#
# print(sum_two_or_three(2, 3))
# print(sum_two_or_three(2, 3, 4))
#
#
# print('Hello', 'world!', sep='***', end='\n')
# print('Good bye!')

# def sum_all_of_them(*args):
#     return sum(args)
#
# print(sum_all_of_them(123, 121, 5232, 4, 5, 6, 7, 8, 9))

# def concat_all(*args):
#     res = ''
#     for word in args:
#         res += word
#     return res
#
#
#
#  print(concat_all('Hello', 'people', 'of', 'planet', 'Earth'))
#
# def tester(a, b, c=0, *args, **kwargs):
#     print(a, b)
#     print(c)
#     print(args)
#     print(**kwargs)
#
#
# tester(2, 3, 1, 't', 'h', True, None, [1, 2, 3], {'name': 'Jack'}, name='Jack', surname='Smith', age=20)

