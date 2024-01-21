phrase = input("Write a phrase : ")

phrase_tuple = phrase.replace(" " , "")

print(f"The Content of the phrase without spaces is as follows : \n  {phrase_tuple}")

tuple_display = print(f"The tuple is : {tuple(phrase_tuple)}")