num = int(input("Enter a number between 1 and 10 : \n"))

if 1 <= num <=10 :
    print(f" Multiplication Table : \n ")
    for i in range (1 , 11):
        answer = num * i
        
        if i < 9:
            print(answer , end=" , ")
        elif i == 10:
             print(f" and  {answer}")
        else:
            print(answer , end = "")

else:
    print("Enter a number between 1 and 10 .")
    