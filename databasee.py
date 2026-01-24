import mysql.connector
query="CREATE TABLE USERS(name VARCHAR(10),age INT);"
try:
    connection=mysql.connector.connect(host='localhost',database='py',user='root',password='123456') # host=127.o.o.1
    cursor=connection.cursor()
    cursor.execute(query)

except:
    print("something went wrong")
finally:
    if connection.is_connected():
        connection.close()
