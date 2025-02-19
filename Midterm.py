#Q1
a = 6
a = a - 2
print(a * 2)
a = a * 2
print(a + 1)
a = a // 3
print(a)

#Q2

print((3 + 10**2 / 2) or 70.0)

#Q3

import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#Q4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
A = "4257304920394478392772938744930294037524"
B = "0974101607733149676776769413377061014790"
C = "7798338247658278460338648728567428338977"
D = "2704702208931031198668911301398022074072"

print("A:", palindrome(A))
print("B:", palindrome(B))
print("C:", palindrome(C))
print("D:", palindrome(D))

#Q5

def count_b_something_bob(text):
    count = 0
    i = 0
    while True:
        # Find the next 'b' from position i
        start = text.find('b', i)
        if start == -1:
            break  # no more 'b' found

        # Find the next 'Bob' after that 'b'
        end = text.find('Bob', start + 1)
        if end == -1:
            break  # no more 'Bob' found

        # Extract the substring from 'b' up to (and including) 'Bob'
        # 'Bob' is 3 characters, so we do end+3
        substring = text[start : end + 3]

        # The middle part is everything after 'b' and before 'Bob'
        middle = substring[1:-3]

        # Check if the middle part is only letters (or empty)
        only_letters = True
        for ch in middle:
            if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
                only_letters = False
                break

        # If valid, increment count and jump past this 'Bob'
        if only_letters:
            count += 1
            i = end + 3
        else:
            # Otherwise, just move forward by 1 to keep searching
            i = start + 1

    return count



#Q6


# Lists are MUTABLE
my_list = [10, 20, 30]
print("Original list:", my_list)

# We can change an element directly:
my_list[0] = 99
print("After changing first element:", my_list)

# We can append a new element:
my_list.append(40)
print("After appending:", my_list)

# Strings are IMMUTABLE
my_str = "Hello"
print("Original string:", my_str)

# Trying to change one character directly would cause an error:
# my_str[0] = "Y"  # <-- NOT ALLOWED, will crash

# Instead, we must create a new string:
new_str = "Y" + my_str[1:]
print("New string:", new_str)
print("Original string still unchanged:", my_str)


#Q7


import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Explanation:
# We'll loop over the list with a 'while' and remove odd numbers in place.
# If we remove an element, we do NOT increment i (because the list shrinks).
# If it's even, we double it and move on.

i = 0
while i < len(random_numbers):
    if random_numbers[i] % 2 != 0:
        # If the number is odd, remove it
        del random_numbers[i]
        # Do NOT increment i here because the list is now shorter
    else:
        # If it's even, double it
        random_numbers[i] = random_numbers[i] * 2
        i += 1

# Print the final list of doubled even numbers
print(random_numbers)


#Q8

def is_valid_url(url):
    """
    Returns True if 'url' looks like a valid URL based on these simple rules:
      - Starts with 'http://', 'https://', or 'www.'
      - Has at least one '.' not at the very end
    Otherwise, returns False.
    """
    # 1) Figure out which prefix we have, if any
    if url[:7] == "http://":
        prefix_length = 7
    elif url[:8] == "https://":
        prefix_length = 8
    elif url[:4] == "www.":
        prefix_length = 4
    else:
        return False  # does not start with a known prefix

    # 2) Look for '.' after the prefix
    dot_position = url.find('.', prefix_length)
    if dot_position == -1:
        return False  # no '.' found
    if dot_position == len(url) - 1:
        return False  # '.' is at the very end => invalid

    return True

#Q9

def days_excluding_birth_and_current():
    birthday_str = "10-09-2005"  # DD-MM-YYYY
    current_year = 2025

    # Extract the birth year from the substring "YYYY" (index 6..10)
    birth_year = int(birthday_str[6:])

    total_days = 0
    # We sum days from birth_year+1 (2006) up to current_year-1 (2024)
    for y in range(birth_year + 1, current_year):
        # Check if y is a leap year
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            total_days += 366
        else:
            total_days += 365

    # Print the total days for all those full years
    print(total_days)


# Run the function:
days_excluding_birth_and_current()

