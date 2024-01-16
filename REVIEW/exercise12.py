months_tuple = ( "January", "February", "March", "April",
          "May", "June", "July", "August","September",
          "October", "November", "December")

num = int(input("Enter a number between 0 and 12: "))

if num == 0:
    print("The Program ends ... ")

    
elif num > 0 and num <= 12:
    print(f"The corresponding month is : {months_tuple[num - 1]}")
        
else:
    print("The number RANGE is 0 to 12 ONLY..!")
