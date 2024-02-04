from connection import connect

# This function connects the database & creates a cursor 
# (my_cursor) associated with that connection.
# {A cursor is used to execute SQL commands.} --> : DEF
def create_user(user_id , user_name , user_surname ,
                user_age , user_email , user_address):
    
    connection = connect()
    my_cursor = connection.cursor()
    
    #Defining SQL insert statement:
    sql_insert = """ INSERT INTO public.users(user_id , user_name , 
                            user_surname , user_age , user_email , user_address)
                            VALUES (%s , %s , %s , %s , %s , %s)
                            """
    
    # These values are provided as arguments to the function created above.
    insert = (user_id , user_name , user_surname ,
                user_age , user_email , user_address)
    
    # Execute the SQL insert statement
    my_cursor.execute(sql_insert ,insert )
    
    # Commit changes made and close cursor and connection from database:
    connection.commit()
    
    my_cursor.close()
    connection.close()
    
    print("INSERTED SUCCESSSFULLY !")
