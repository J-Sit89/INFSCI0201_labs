from functools import reduce

def group_by(func, target_list: list):
    return reduce(
        lambda acc, x: {**acc, func(x): acc.get(func(x), []) + [x]},
        target_list,
        {}
    )

print(group_by(len, ["hi", "dog", "me", "bad", "good"]))  # {2: ['hi', 'me'], 3: ['dog', 'bad'], 4: ['good']}
