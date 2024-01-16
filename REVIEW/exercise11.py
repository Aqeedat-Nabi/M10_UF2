num = int(input("Enter a number between 10 and 100: "))

if num >= 10 and num <= 100:
    num_tuple = tuple(range(1 , num + 1))
    print(f"A tuple is created with the numbers from 1 to {num} , and is displayed on the screen as follows : ")
    print(num_tuple)
    
else:
    print("The number RANGE is 10 to 100 ONLY..!")
