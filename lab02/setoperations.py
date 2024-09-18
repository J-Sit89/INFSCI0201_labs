def make_set(data):
    if data is None: 
        return []
    
    result = []
    for item in data:
        if item not in result:
            result.append(item)
    
    return result

def is_set(data):
    if data is None: 
        return False
    return len(data) == len(make_set(data))

def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    
    result = make_set(setA + setB) 
    return result

def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    
    result = []
    for item in setA:
        if item in setB and item not in result:
            result.append(item)
    
    return result


print(make_set([1, 2, 3, 4, 4, 5]))  
print(is_set([1, 2, 3, 4, 5]))  
print(is_set([5, 5]))  
print(union([1, 2], [2, 3]))  
print(intersection([1, 2], [2, 3])) 
