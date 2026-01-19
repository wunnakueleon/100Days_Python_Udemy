# new_list = [n + 1 for n in range(1, 5)]
# print(new_list)

# names = ["Broew", "Chowd", "dsoi"]
# new = [name for name in names if len(name)]


# raw = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd = [True if num % 2 == 0 else False for num in raw]
# print(even_odd)
# print(len(even_odd))

import random

names = ["Alex", "Beth", "Carolina", "Paul"]
dict = {student:random.randint(1, 5) for student in names}
print(dict)
new_pass = {student:score for (student, score) in dict.items() if score >= 3}
print(new_pass)

