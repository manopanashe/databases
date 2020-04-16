import sqlite3
db = sqlite3.connect('C:\Users\manop\Documents\databases\assesment3.db')
cursor = db.cursor()
shopper_id = input("Enter shopper id:")
sql_query = ("")