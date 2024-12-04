from itertools import zip_longest
from collections import Counter

def zipmap(key_list: list, value_list: list, override=False):
    if not override and len(set(key_list)) != len(key_list):  # Check for duplicates in key_list
        return {}
    
    zipped = zip_longest(key_list, value_list)  # Handles mismatched lengths
    if override:
        result = dict(zipped)
    else:
        result = dict((k, v) for k, v in zipped if key_list.count(k) == 1)
    return result

print(zipmap(['a', 'b', 'c'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3}
print(zipmap(['a', 'b', 'a'], [1, 2, 3], override=True))  # {'a': 3, 'b': 2}
print(zipmap(['a', 'b', 'a'], [1, 2, 3], override=False))  # {}