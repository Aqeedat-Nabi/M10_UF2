
nums_tuple = []

list = nums_tuple.split()

nums = input(" Enter numbers separated by a space : ")

while True:
    
    if nums == "0":
        print("The Program finished after putting a zero (0) . ")
        break
    
    else :
        nums_tuple = (nums)
    
    list = nums_tuple.split()
    
    # if nums == 0:
    #     print("The Program finished after putting a zero (0) . ")
    #     break
    
    # else :
    #     list.append(nums)
        
if len(nums_tuple) != 0:
    sort_order = input("Enter (asc) to sort in ascending and (desc) to sort in descending order : \n ")
    
    if sort_order == "asc" :
        sorted_tuple_asc = (sorted(nums_tuple , reverse=False))
        print(f"The numbers are arranged in ascending order : \n {sorted_tuple_asc}")
        
    elif sort_order == "desc" :
        sorted_tuple_desc = (sorted(nums_tuple , reverse=True))
        print(f"The numbers are arranged in descending order : \n {sorted_tuple_desc}")  
    else:
        print("Invalid Option ...! ")
        
else:
    print("Enter some numbers separated by a space .. ")
        



























# # 15 

# # Initialize an empty list to store numbers
# numbers_list = []

# # Keep taking input until the user enters 0
# while True:
#     user_input = float(input("Enter a number (enter 0 to finish): "))
    
#     if user_input == 0:
#         break  # Exit the loop if the user enters 0
#     else:
#         numbers_list.append(user_input)

# # Check if the user entered at least one number
# if len(numbers_list) > 0:
#     # Ask the user for the sorting order
#     sorting_order = input("Enter 'asc' to sort in ascending and 'desc' to sort in descending order: ").lower()

#     if sorting_order == "asc":
#         # Create a tuple and sort it in ascending order
#         sorted_tuple = tuple(sorted(numbers_list))
#         order_label = "Ascending"
#     elif sorting_order == "desc":
#         # Create a tuple and sort it in descending order
#         sorted_tuple = tuple(sorted(numbers_list, reverse=True))
#         order_label = "Descending"
#     else:
#         print("Invalid sorting order. Please enter 'asc' or 'desc'.")
#         exit()

#     # Display the sorted tuple
#     print(f"\n{order_label} Sorted Tuple:")
#     print(sorted_tuple)
# else:
#     print("No numbers entered. Exiting the program.")




# # 16

# # Ask the user for a phrase
# user_phrase = input("Enter a phrase: ")

# # Remove spaces from the phrase and create a tuple
# char_tuple = tuple(user_phrase.replace(" ", ""))

# # Display the contents of the tuple
# print("\nTuple containing characters (without spaces):")
# print(char_tuple)