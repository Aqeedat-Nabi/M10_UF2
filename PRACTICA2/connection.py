# This function is used to establish a connection 
# to a PostgreSQL database using the psycopg2 
import psycopg2

# It creates a connection to a PostgreSQL database
# and it is a reusable function
def connect():
    conn = psycopg2.connect(
        database = "postgres" ,
        user = "user_postgres" ,
        password = "pass_postgres" ,
        host = "localhost" ,
        port = "5432"
    )
    
    return conn

#{creates a cursor object (connection) associated with the PostgreSQL database 
# connection (conn).}----> explanation of the line below : 
#connection = conn.cursor()
    
# showing the memory address of the cursor object created above :    
#print(connection)
