value = input("Enter  between 1 to 3 words : ")
words = value.split()

if len(words) >= 1 and len(words) <= 3 :
    for word in words:
        print(f"The Word : {word}")
        print(f"Letters in the word are : {len(word)}")
        print(f"The first letters of the word is  : {word[0]}")
        print(f"The last letters of the word is  : {word[-1]}\n")
else:
    print("Enter exactly 1 , 2 or 3 words.. NOT MORE THAN 3 :")