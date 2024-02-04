# Import connect function:
from connection import connect

def user_update(user_id , modification):
    connection = connect()
    my_cursor = connection.cursor()
    
    # Define SQL update statement:
    # updates all the fields based on the provided parameters 
    sql_update = """ UPDATE public.users 
                    SET user_name = %s , 
                    user_surname = %s ,
                    user_age = %s ,
                    user_email = %s ,
                    user_address = %s
                    WHERE user_id = %s;
                """
    
    # updates all the fields with the provided modification values by the user            
    my_cursor.execute(sql_update, (
        modification['user_name'],
        modification['user_surname'],
        modification['user_age'],
        modification['user_email'],
        modification['user_address'],
        user_id
    ))
    
    # Commit changes made and close cursor and connection from database:
    connection.commit()
    
    print(" Changes made without errors .. ")
    
    my_cursor.close()
    connection.close()
    
#result = connection.rowcount
