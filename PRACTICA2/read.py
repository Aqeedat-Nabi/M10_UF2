# by importing creates a connection to PostgreSQL database.
from connection import connect

# This function retrieve all user records from the "users" 
# table  after making connection inside the try block:
def read_user():
    try:
        connection = connect()
        my_cursor = connection.cursor()
        
        # executes the SQL query
        sql_read = """ SELECT * FROM public.users; """

        my_cursor.execute(sql_read)
        
        # get all user records
        result = my_cursor.fetchall()

        # close the cursor and the database connection 
        my_cursor.close()
        connection.close()

        #  it prints each user record to the console if found 
        # and if not found either 
        if result:
            print("All Users:")
            for user in result:
                print(user)
            return result
        else:
            print("No users found.")
            return None

    # handling exception in case of error : 
    except Exception as e:
        print(f"There's an error: {str(e)}")
        return None

# if __name__ == "__main__":
#     read_user()

    
    
# for i in result : 
#     print("user_id : " , i[0] , )
#     print("user_id : " , i[1] , )
#     print("user_id : " , i[2] , )
#     print("user_id : " , i[3] , )
#     print("user_id : " , i[4] , )
#     print("user_id : " , i[5] , "\n")
    
# print("The Users Table Shown .")
