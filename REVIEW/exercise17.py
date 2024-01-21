phrase = input("Write a phrase : ")

phrase_tuple = phrase.replace(" " , "")

print(f"The Content of the phrase without spaces is as follows : \n  {phrase_tuple}")

phrase_set = set(phrase_tuple)

phrase_set_tuple = "".join(phrase_set)

print(f"The Content of the phrase without duplication is as follows : \n  {phrase_set_tuple}")

tuple_display = print(f"The tuple is : {tuple(phrase_set_tuple)}")
