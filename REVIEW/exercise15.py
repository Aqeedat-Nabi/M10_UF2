
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
        