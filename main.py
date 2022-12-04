# # Fundamental Data Types: List of data types in python
# # int & float
# # print(type(6))
# # print(type(2 - 4))
# # print(type(2 * 4))
# # print(type(2 / 4))  #.5

# # print(2 ** 3)
# # print(5 // 4)
# # print(6 % 4)

# # Math Functions
# # print(round(3.9))

# # bool
# # str
# # list
# # tuple
# set
# # dict

# # Classes -> custom types

# #Specialized Data types
# # name = input("what is your name?")
# # print("hello " + name)

# # Operator Precedence
# # print(20 - 3 * 4)

# # ()
# # **
# # * /
# # + -

# # Binary Operator
# # print(bin(5))
# # print(int('0b101', 2))

# #Python Variables
# # iq = 190

# # user_age = iq / 4

# # a = user_age

# # print(a)

# # Use HI (Block Letters) to assign a constant variable in python

# # #Augmented Assignment Operator
# # some_value = 5
# # some_value += 2
# # some_value -= 1
# # some_value *= 3

# # print(some_value)

# #strings
# # print(type('Hello'))
# # username = 'World'
# # password = 'Super Secret'

# #Long String is the way to store large text messages

# # long_string = '''
# # WOW
# # O O
# # ---
# # '''
# # print(long_string)

# # first_name = 'Aayush'
# # last_name = 'Mohan'

# # full_name = first_name + ' ' + last_name

# # print(full_name)

# #string concatenation

# # print('hello ' + 'aayush')

# # #Type Conversion
# # a = str(100)
# # b = int(a)
# # c = type(b)

# # print(c)

# # #Escape Sequence
# # # Here (\) is used to add a quotation mark in a string
# # # \n is use to add a new line and \t is used to add a tab

# # weather = ('It\'s a sunny day\n')

# # day = ('\t It\'s perfect to go out')

# # print(weather + day)

# # #Formatted String

# # name = 'Johnny'
# # age = 55

# # print(f'Hi {name}. You are {age} years old')

# # #String Indexes
# # selfish = ('01234567')
# #           # 01234567

# # #[start:stop:stepover]

# # print(selfish[::-1])

# # #Built in functions + methods

# # quote = 'to be or not to be'

# # print(quote.replace('be', 'me'))
# # print(quote)

# # #Booleans

# # name = 'Aayush'

# # is_cool = False
# # is_cool = True

# # print(is_cool)

# # #Type Conversion Exercise

# # birth_year = input('What year were you were born?')

# # age = 2022 - int(birth_year)

# # print(f'You\'re {age} years old')

# # #Password Checker Exercise

# # username = input('What is your Name ')
# # password = input('What is your password ')

# # password_length = len(password)

# # hidden_password = password_length * '*'

# # print(
# #   f'Hello {username }, Your password, {hidden_password } is {password_length}  is letters long'
# # )/

# # #Lists
# # #List in python is just like Arrays in other programming languages

# # amazon_cart = ['notebooks', 'shades', 'toys', 'grapes']

# # amazon_cart[0] = 'laptop'
# # new_cart = amazon_cart[:]
# # new_cart[0] = 'gum'

# # print(new_cart)
# # print(amazon_cart[0])

# #Matrix

# matrix = [[0, 5, 0],[0, 1, 0],[1, 0, 1]]

# print(matrix[0][1])

### List Methods
# basket = [1, 2, 3, 4, 5]

# # # Use Append method to add things at the end of the list

# basket = ['a', 'b', 'f', 'c', 'd', 'e']

# # Use (in) keyword to get a boolean value of the list
# print('d' in basket)

# print('I' in 'Hi my name is Ian')

# print(basket.count('d'))
# #Use count to check how many times a value occurs in our list

# basket.sort() #Use sort keyword for sorting of list
# basket.copy() #Use copy to copy the same list
# basket.reverse() #Use reverse to reverse the list

# print(basket[:])
# print(len(basket))

# Use list range to find the range of the list or To Generate a list
# print(list(range(101)))

# #list unpacking
# #use *others for unpacking the list
# a, b, c, *others = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(a)
# print(b)
# print(c)

# print(others)

# #None
# score = None
# print(score)

###Dictionary
### Dictionary: A dictionary is an unordered key-value pair. And as long as we know the key, that is whatever the key we're looking for, then we just give that and our computer will know.

# dictionary={
#   {
#   'a': [1,2,3],
#   'b': 'hello',
#   'c': True,
#   },
# }

# my_list=[
#   {
#   'a': [1,2,3],
#   'b': 'hello',
#   'c': True,
#   },
#   {
#   'a': [4,5,6],
#   'b': 'bye',
#   'c': True,
#   }
# ]

# print(my_list[0] ['a'][2])

# #Dictionary Method
# user = {'basket': [1, 2, 3], 'greet': 'Hello', 'age': 20}

# print(user.get('age', 55))

# # Uncommon Way of Creating a dictionary

# user2 = dict(name="JohnJohn")
# print(user2)

#Dictionary Method 2

# user = {'basket': [1, 2, 3], 'greet': 'Hello', 'age': 20}

# print('Hello' in user.keys()) #use .keys() to return a list containing the dictionary's keys

# print('Hello' in user.values()) #use .values() to return a list of all the values in the dictionary.

# print(user.items()) #use .items() to return a list containing a tuple for each key value pair.

# print(user.clear()) #use .clear() to remove all the elements from the dictionary

# user2 = user.copy() #use .copy() to return a copy of the dictionary

# print(user.clear())
# print(user2)

# print(user.popitem()) #use .popitem() to remove the last inserted key value pair

# print(user.update({'age': 56})) #use .update() to update the dictionary with specified key value pairs
# print(user)

# #Tuple

# my_tuple = (1, 2, 3, 4, 5)
# print(5 in my_tuple)

# user = {(1, 2): [1, 2, 3], 'greet': 'hello', 'age': 20}

# x, y, z, *other = (1, 2, 3, 4, 5)

# print(other)

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple.count(5)) # use .count to check how many items are in the list