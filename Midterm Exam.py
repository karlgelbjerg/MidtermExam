# Question 1
a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

# What will the following code print?
print((3+10**2/2) or 70.0)

# Fill in what the code below prints
import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

# Which of the below is not a palindrome?
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
numbers = [
"6892149109325320763773670235239019412986",

"9847255590886266818998186626880955527489",

"1414884937242655719669145562427394884141",

"6800923757255865070000705685527573290086"
]
for number in numbers:
    if not palindrome(number):
        print(f"{number} is not a palindrome.")


# Question about lists being mutable
lst = [1, 2, 3, 4, 5]
lst[1]
lst[1] = 6
print(lst)
lst[1] = lst[2]
print(lst)
lst[4] = 10
print(lst)


import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = None  # Removing numbers greater than 50
random_numbers = [num for num in random_numbers if num is not None] # making sure that the code doesn't print "none"
print(random_numbers)

#Question of words starting with C and ending with jeb
def find_pattern_occurrences(text):
    occurrences = 0
    for word in text.split():
        if word.startswith("C") and word.endswith("jeb"):
            occurrences += 1
    return occurrences


text = "CHellojeb Chellojab Cdotjeb Tdotjeb Cpatternjeb Ctestingeb Canotherpatternjeb"
print(find_pattern_occurrences(text))

# Question about parameters is a valid url or not
s = "http://cnn.com and then we could also include something like http://youtube.com or even a website like http://bbc.co.uk but not www.ieconnects.com "
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find(" ",start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end
