import sqlite3
db = sqlite3.connect('U:\databases\databases\dtabase3.db')
cursor = db.cursor()
prodid = input("Enter the prodid for the product: ")
qty = input("Enter the minimum order quantity: ")
#retrieve the details for the order selected
sql_query = "SELECT c.custid, o.ordid, i.qty, p.descrip \
            FROM customer c \
                INNER JOIN ord o ON c.custid = o.custid \
                INNER JOIN item i ON o.ordid = i.ordid \
                INNER JOIN product p ON p.prodid = i.prodid \
            WHERE p.prodid = ? \
            AND i.qty >= ? \
            ORDER BY c.custid,o.ordid"
cursor.execute(sql_query, (prodid,qty))
all_order_rows = cursor.fetchall()
#if any rows were returned, print the order details
if all_order_rows:
    print("\nCustomers who have placed orders for at least quantity",qty,"of product",prodid)
    print("\nCust\tOrd\t Qty\tProduct Description")
    #print the order lines
    for order_row in all_order_rows:
        cust_id = order_row[0]
        order_id = order_row[1]
        order_qty = order_row[2]
        prod_description = order_row[3]
        print("{0:4}\t{1:3d}\t{2:4d}\t{3}" \
		 .format(cust_id,order_id,order_qty,prod_description))
#if no row was returned, print a helpful error message
else:
    print("No customers have placed an order for that number of the selected product")
db.close()






















