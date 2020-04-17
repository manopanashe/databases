import sqlite3
import sqlite3
db = sqlite3.connect("C:/Users/manop/Documents/databases/assesment 3.db")
cursor = db.cursor()
shopper_id = input("Enter shopper id:")
sql_query = ("SELECT shopper_id \
               FROM shoppers")
cursor.execute(sql_query)
shopper_id = cursor.fetchone()
orinoco_shopper_main_menu =["Display your order history",
"Add an item to your basket", "view your basket",
"checkout", "Exit"]
print("orinoco shopper's main menu".center(30))
option_num = 1
for menu_option in orinoco_shopper_main_menu:
    print("{0}. {1}".format(option_num,menu_option))
    option_num = option_num + 1
db.close()


