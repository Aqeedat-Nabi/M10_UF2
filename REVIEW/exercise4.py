import random

# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a second number : "))

def add_nums(num1 , num2) :
    return num1 + num2

# diff = num1 - num2
# print(f"The difference of the two number is : {diff}")

# prod = num1 * num2
# print(f"The product of the two number is : {prod}")

# quot = num1 / num2
# print(f"The quotient of the two number is : {quot}")

# mod = num1 % num2
# print(f"The modulus of the two number is : {mod}")

def random_num(num1, num2):
    return random.randint(min(num1, num2), max(num1, num2))