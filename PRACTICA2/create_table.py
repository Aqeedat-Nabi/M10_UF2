from connection import *


sql = """ CREATE TABLE USERS(
                user_id SERIAL PRIMARY KEY ,
                user_name VARCHAR(255) NOT NULL ,
                user_surname VARCHAR(255) NOT NULL ,
                user_age BIGINT NOT NULL ,
                user_email VARCHAR(255) NOT NULL ,
                user_address VARCHAR(255)
)"""

print(sql)

connection.execute(sql)

print(connection)

conn.commit()

#connection.close()
#conn.close()
