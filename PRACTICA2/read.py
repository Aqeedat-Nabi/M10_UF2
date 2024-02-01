from connection import *

sql_read = """ SELECT user_id , user_name , user_surname , user_age , user_email , user_address 
                FROM public.users
"""

connection.execute(sql_read)

result = connection.fetchall()

for i in result : 
    print("user_id : " , i[0] , )
    print("user_id : " , i[1] , )
    print("user_id : " , i[2] , )
    print("user_id : " , i[3] , )
    print("user_id : " , i[4] , )
    print("user_id : " , i[5] , "\n")
    
print("The Users Table Shown .")





