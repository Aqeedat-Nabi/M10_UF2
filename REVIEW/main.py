from exercise4 import *
from exercise1 import range

def user_input():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a second number : "))
    return num1 , num2

def main():
    user_nums = user_input()
    # output = add_nums(*user_nums)
    # print(f"The sum of {user_nums[0]} and {user_nums[1]} is: {output}")
    
    # output = random_num(*user_nums)
    # print(f"The random num between {user_nums[0]} and {user_nums[1]} is: {output}")
    
    result_numbers, result_sum = range(*user_nums)

    # Display the result
    print(f"Numbers between {user_nums[0]} and {user_nums[1]}: {result_numbers}")
    print(f"Sum of the numbers: {result_sum}")
    
    
if __name__ == "__main__" :
    main()
    