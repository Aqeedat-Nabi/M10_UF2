num = int(input("Enter a number between 0 and 12: "))

if num > 0 and num <= 12:
    month_tuple = tuple(range(1 , num + 1))
    print(f"A tuple is created with the numbers from 1 to {num} , and is displayed on the screen as follows : ")
    print(month_tuple)
else:
    print("The number RANGE is 0 to 12 ONLY..!")
