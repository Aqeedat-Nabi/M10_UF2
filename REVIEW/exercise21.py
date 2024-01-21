numbers = input("Enter 10 number separated by spaces : \n")

num_list = [float(num) for num in numbers.split()]

print(f"User numbers : {numbers}")

t_sum = sum(num_list)
print(f"The total sum is : {t_sum}")

avg = t_sum / len(num_list)
print(f"The average is : {avg}")
        
num_list.extend([t_sum,avg])
print(f"The new list is :\n {num_list}")
        