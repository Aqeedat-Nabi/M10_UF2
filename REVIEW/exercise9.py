first = input("Enter  first word : ")
second = input("Enter  second word : ")

print(f"The First Word is : {first}")
print(f"The Second Word is : {second}")

print("Now Swapping the letters of both the words : ")

word1 = second[0:2] + first[2:]
word2 = first[0:2] + second[2:]

print(f"The NEW First Word is : {word1}")
print(f"The NEW Second Word is : {word2}")
