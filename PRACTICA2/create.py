from connection import *


sql_insert = """ INSERT INTO public.users(user_id , user_name , user_surname , user_age , user_email , user_address)
                            VALUES ('1' , 'Jessica' , 'Robert' , 25 , 'jessi@gmail.com' , 'Skagen 21')
"""

connection.execute(sql_insert)

conn.commit()

print("CREATED SUCCESSSFULLY !")
