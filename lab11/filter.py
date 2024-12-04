from functools import reduce

def custom_filter(func, target_list: list):
    return reduce(
        lambda acc, x: acc + [x] if func(x) else acc,
        target_list,
        []
    )

print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))  # [2, 4]