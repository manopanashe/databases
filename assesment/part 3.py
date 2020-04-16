import sqlite3
db = sqlite3.connect("C:/Users/manop/Documents/databases/assesment3")
cursor = db.cursor()
shopper_id = input("Enter shopper id:")
sql_query = ("SELECT shopper_id \ FROM shoppers")
cursor.execute(sql_query)
shopper_id = cursor.fetchone()
print(shopper_id)
db.close()
