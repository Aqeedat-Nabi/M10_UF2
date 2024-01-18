words_tuple = []

word1 = input("Enter 1st word : ")

word2 = input("Enter 2nd word : ")

words_tuple = (word1 , word2)

print(f"The tuple of the given words are as follows : \n {words_tuple}")

count_letter = input("Enter the letter you wanna count : ")

word_count = words_tuple.count(count_letter)

print(f"The given letter appears {word_count} time .")