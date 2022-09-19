# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

import random
import string

new_dict = {}
test_d = {}
final_dict = {}
# Creataing a tuple with lerrers for future dicts
list_of_letters = string.ascii_lowercase

# Creating an empty list with a random empty dicts
list_of_dicts = [{} for _ in range(random.randint(2, 10))]
print(list_of_dicts)
for d in list_of_dicts:
    for i in range(random.randint(0, len(list_of_letters))):
        d[random.choice(list_of_letters)] = random.randint(0, 100)
for d in list_of_dicts:
    for k in d:
        if not k in new_dict:
            new_dict[k] = d.get(k)

        else:
            for l in list_of_dicts:
                for t in l:
                    if k in new_dict:
                        new_dict[k + '_'] = max(new_dict[k], d[k])
                        new_dict.pop(k)
            # test_d[k] = d.get(k)

# for key in new_dict:
#     for key_t in test_d:
#         if key == key_t:
#             final_dict[key+'_'] = max(new_dict[key],test_d[key_t])


print(list_of_dicts)
print(new_dict)

