import mysql.connector
DB=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='NewPassword',
    auth_plugin='mysql_native_password'
)

cursorObject = DB.cursor()

cursorObject.execute("Create Database DCRM")
 
print("Database Connected!")