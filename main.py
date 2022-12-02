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

#List Methods
basket = [1, 2, 3, 4, 5]

# Use Append method to add things at the end of the list
# Adding
basket.append(100)
basket.insert(0, 0)
basket.extend([101])

new_list = basket

# print(new_list)

# Removing
basket.pop()
basket.pop()
basket.pop(0)

basket.remove(3)

print(basket)