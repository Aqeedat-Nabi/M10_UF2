from connection import *

sql_delete = """ DELETE FROM public.users WHERE user_id = 1
"""
connection.execute(sql_delete)

conn.commit()

print("DELETED SUCCESSFULLY !")


