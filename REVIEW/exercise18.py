count_letter = {}

word1 = input("Enter 1st word : ")

word2 = input("Enter 2nd word : ")

words_tuple = (word1 , word2)

print(f"The tuple of the given words are as follows : \n {words_tuple}")

for i, word in enumerate(words_tuple , 1):
    for letter in word :
        count_letter[letter] = count_letter.get(letter , 0) + 1
        
    print(f"\n Letters in the word{i} ({word}) : ")
    
    for letter , count in count_letter.items() :
        print(f"The letter {letter} appears : {count} time(s) .")

