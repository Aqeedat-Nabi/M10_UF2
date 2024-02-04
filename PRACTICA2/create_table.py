# import function that is responsible for connection
from connection import connect

# This function, when executed,connects to a PostgreSQL 
# database and creates a table named "USERS" if it does not already exist .
def create_table():
    # a connection to the PostgreSQL database
    connection = connect()
    my_cursor = connection.cursor()
    
    # Defining the SQL table creation statement :
    sql_table = """ CREATE TABLE IF NOT EXISTS USERS(
        user_id SERIAL PRIMARY KEY ,
        user_name VARCHAR(255) NOT NULL ,
        user_surname VARCHAR(255) NOT NULL ,
        user_age BIGINT NOT NULL ,
        user_email VARCHAR(255) NOT NULL ,
        user_address VARCHAR(255)
        );"""
        
    print(sql_table)
    
    # Commit changes made and close cursor and connection from database:
    my_cursor.execute(sql_table)
    print(my_cursor)
    
    connection.commit()
    
    my_cursor.close()
    connection.close()

# if __name__ == "__main__":
#     create_table()
    