from connection import connect

# This function makes connection to database and creates 
# a cursor to execute delete SQL query
def delete_user(user_id):
    
    connection = connect()
    my_cursor = connection.cursor()
    
    # Define SQL delete statement:
    sql_delete = """ DELETE FROM public.users 
                        WHERE user_id = %s
    """
    
    # Execute the SQL delete statement:
    my_cursor.execute(sql_delete , (user_id , ))
    
    # Commit delete changes and close cursor and connection from database:
    connection.commit()
    
    print("DELETED SUCCESSFULLY !")
    
    my_cursor.close()
    connection.close()
    