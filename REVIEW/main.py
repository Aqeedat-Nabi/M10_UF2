from exercise27 import *
from exercise28 import *
from exercise29 import *
from exercise30 import *
from exercise31 import *
from exercise32 import *
from exercise33 import *
from exercise34 import *
from exercise35 import *

def user_input():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a second number : "))
    return num1 , num2

def main():
    #user_nums = user_input()
    
#27
    # output = add_nums(*user_nums)
    # print(f"The sum of {user_nums[0]} and {user_nums[1]} is: {output}")
    
#28
    # output = random_num(*user_nums)
    # print(f"The random num between {user_nums[0]} and {user_nums[1]} is: {output}")
    
#29
    # result_numbers ,  result_sum = show_range(*user_nums)

    # print(f"Numbers between {user_nums[0]} and {user_nums[1]}: {result_numbers}")
    # print(f"Sum of the numbers: {result_sum}")
    
#30
    # greet_user()
    
#31
    # amount = float(input("Enter the amount without VAT: "))
    # VAT = float(input("Enter the VAT rate (4%, 10%, or 21%): "))
    
    # calc_VAT(amount , VAT)
    
#32
    # numbers = [int(input(f"Enter number {i + 1} : ")) for i in range(10)]
    # result = calc_squares(numbers)
    # print("List of squares :", result)
    
#33
    # shopping_list = {}
    # num_products = int(input("Enter the number of products : "))

    # for i in range(1, num_products + 1):
    #     price = float(input(f"Enter the price for Product {i} : "))
    #     discount = float(input(f"Enter the discount for Product {i} (%): "))
    #     shopping_list[price] = discount

    # vat_rate = float(input("Enter the VAT rate: "))
    # calc_shopping(shopping_list, vat_rate)   
    
#34
    # numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(5)]
    
    # result = add_to_list(calcul_sq, numbers)

    # print("Original list:", numbers)
    # print("List with squares:", result)
    
#35
    sentence = input("Enter a sentence: ")
    result = count_words(sentence)
    print("Word count and lengths:", result)
    
if __name__ == "__main__" :
    main()
    