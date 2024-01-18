word = input("Write a word : ")

word_tuple = word.replace(" " , "")

print(f"The Content of the phrase without spaces is as follows : \n  {word_tuple}")

word_set = set(word)

print(f"The Content of the phrase without duplication is as follows : \n  {word_set}")
