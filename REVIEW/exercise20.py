dictionary = {}

while True:
    name = input("Enter a name \n or enter a 0(zero) to stop insertion :")
    
    if name == "0" :
        print("Stop inserting the contacts ... ")
        break
    
    age = input(f"Enter the age of {name} : ")
    
    if name in dictionary :
        print(f"The person with name {name} already exists .")
    else : 
        dictionary[name] = int(age)
        
print(f"The contacts are : {dictionary}")
