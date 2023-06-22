# Arithmetic Operators
x = 10
y = 3

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
floor_division = x // y
modulus = x % y
exponentiation = x ** y

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")

# Comparison Operators
a = 5
b = 7

print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Assignment Operators
x = 10

x += 5
print(f"Add and Assign: {x}")

x -= 3
print(f"Subtract and Assign: {x}")

x *= 2
print(f"Multiply and Assign: {x}")

x /= 4
print(f"Divide and Assign: {x}")

x %= 3
print(f"Modulus and Assign: {x}")

x //= 2
print(f"Floor Division and Assign: {x}")

x **= 3
print(f"Exponentiation and Assign: {x}")

# Logical Operators
p = True
q = False

print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")

# Membership Operators
my_list = [1, 2, 3, 4, 5]

print(f"3 in my_list: {3 in my_list}")
print(f"6 not in my_list: {6 not in my_list}")

# Identity Operators
x = 10
y = 10
z = 5

print(f"x is y: {x is y}")
print(f"x is not z: {x is not z}")

# Bitwise Operators
a = 60  # Binary: 0011 1100
b = 13  # Binary: 0000 1101

bitwise_and = a & b  # Binary: 0000 1100
bitwise_or = a | b   # Binary: 0011 1101
bitwise_xor = a ^ b  # Binary: 0011 0001
bitwise_not = ~a     # Binary: 1100 0011
left_shift = a << 2  # Binary: 1111 0000
right_shift = a >> 2 # Binary: 0000 1111

print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Left Shift: {left_shift}")
print(f"Right Shift: {right_shift}")
