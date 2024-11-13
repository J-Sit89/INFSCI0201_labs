def product_of_digits(x):
    x = abs(x)
    if x < 10: 
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)

def array_to_string(a, index=0):
    if index == len(a) - 1:  
        return str(a[index])
    else:
        return str(a[index]) + "," + array_to_string(a, index + 1)

def log(base, value):
    if base <= 1 or value <= 0:
        raise ValueError("Base must be greater than 1 and value must be greater than 0.")
    if value < base: 
        return 0
    else:
        return 1 + log(base, value // base)


# Testing the functions with examples
print(product_of_digits(234))  # Expected output: 24
print(product_of_digits(-12))  # Expected output: 2
print(array_to_string([1, 2, 3, 4]))  # Expected output: "1,2,3,4"
print(log(10, 123456))  # Expected output: 5
print(log(2, 64))  # Expected output: 6
