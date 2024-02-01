import psycopg2

# def connect():
conn = psycopg2.connect(
    database = "postgres" ,
    user = "user_postgres" ,
    password = "pass_postgres" ,
    host = "localhost" ,
    port = "5432"
)
    
    # return conn
    
connection = conn.cursor()
    
#print(connection)
