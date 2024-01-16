nums = input(" Enter 10 numbers separated by a space : \n ")

nums_tuple = (nums)

list = nums_tuple.split()

if len(list) == 10:
    sort_order = input("Enter (asc) to sort in ascending and (desc) to sort in descending order : \n ")
    
    if sort_order == "asc" :
        sorted_tuple_asc = (sorted(list , reverse=False))
        print(f"The numbers are arranged in ascending order : \n {sorted_tuple_asc}")
        
    elif sort_order == "desc" :
        sorted_tuple_desc = (sorted(list , reverse=True))
        print(f"The numbers are arranged in descending order : \n {sorted_tuple_desc}")
        
    else:
        print("Invalid Option ...! ")
        
else :
    print("Enter 10 numbers separated by a space ")


