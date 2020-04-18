import sqlite3
import sqlite3
db = sqlite3.connect("C:/Users/manop/Documents/databases/assesment 3.db")
cursor = db.cursor()
shopper_id = input("Enter shopper id:")
sql_query = ("SELECT sh.order_id, sh.order_date, p.product_description, s.seller_name, o.price, o.quantity, o.ordered_product_status\
               FROM ordered_products o\
               INNER JOIN products p ON p.product_id = o.product_id\
                INNER JOIN shopper_orders sh ON sh.order_id = o.order_id\
                   LEFT OUTER JOIN sellers s ON s.seller_id = o.seller_id\
                   ORDER BY sh.order_date")
cursor.execute(sql_query)
all_rows = cursor.fetchall()
print("Order ID\tOrder Date\t product Description\t Seller\t  Price\t  QTY\t Status\n")
for row in all_rows:
    order_id = row[0]
    order_date = row[1]
    product_description = row[2]
    seller_name = row[3]
    price= row[4]
    quantity  = row[5]
    ordered_product_status = row[6]
    print("{0}. {1}. {2}. {3}. {4}. {5}. {6}".format(order_id,order_date,product_description,seller_name,price,quantity,ordered_product_status))
db.close()


