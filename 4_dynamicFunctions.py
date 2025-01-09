# def check_3_digits(number):
#     return number in range(100, 1000)

# result = check_3_digits(579)
# print(result)


# def check_3_digits(list1):
#     for n in list1:
#         if n in range(100, 1000):
#             print(True)
#         else:
#             pass

#     return False


# result = check_3_digits([555, 99, 600])
# print(result)


# def check_3_digits(list1):

#     three_digit_list = []

#     for n in list1:
#         if n in range(100, 1000):
#             three_digit_list.append(n)
#         else:
#             pass
#     return three_digit_list


# result = check_3_digits([555, 99, 600])
# print(result)


# coffee_prices = [('cappuccino', 1.5),
#                  ('espresso', 1.2),
#                  ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):
#     highest_price = 0
#     my_most_expensive_coffee = ''

#     for coffee, price in list_of_prices:
#         if price > highest_price:
#             highest_price = price
#             my_most_expensive_coffee = coffee
#         else:
#             pass
#     return(my_most_expensive_coffee, highest_price)

# print(most_expensive_coffee(coffee_prices))


# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(numbers): # this creates the function
    return all(n > 0 for n in numbers) # goes through every number in the numbers list, checking if every number is greater than 0 (checking if the number is positive)

numbers = [1, -2, 3, 4, -5] # the list containing the positive and negative values
print(all_positives(numbers)) # this then prints everything to check if the list contains all positives, if true it prints true, if not it prints false

# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(numbers): # creates the function
    return sum(n for n in numbers if 0 < n < 1000) # goes through every number in the list, checking if the number is more than 0 AND less than 1000, and then adding all the numbers that follow the requirements

numbers = [0, 10, -20, 500, 999, 1000, -10,] # the list that contains all of the numbers
print(sum_less(numbers)) # prints the function and gives the value of all of the numbers that follow the requirements

# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

def count_even(numbers): # creates the function
    return sum(n for n in numbers if n % 2 == 0) # goes through every number in the list, checking if the numbers are even, if they are they get added together

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # the list containing the numbers
print(count_even(numbers)) # this prints the function which has the value of all the numbers that are even added up