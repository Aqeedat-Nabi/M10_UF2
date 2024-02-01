from connection import *

sql_update = """ UPDATE public.users SET user_age = 30 
                    WHERE user_id = 1
"""

connection.execute(sql_update)

conn.commit()

result = connection.rowcount

print(" Modified id : " , result ," Changes made without errors .. ")



