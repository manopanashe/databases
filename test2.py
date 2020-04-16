import sqlite3
db = sqlite3.connect('C:\Users\manop\Documents\databases\dtabase3.db')
cursor = db.cursor()
# enable foreign key constraints
cursor.execute("PRAGMA foreign_keys=ON")
cust_name = input("Enter the name of the new customer: ")
cust_repid = input("Enter their sales rep id: ")
cust_creditlimit = int(input("Enter their creditlimit: "))
# check if the sales rep id entered is a valid SALESMAN in the employee table 
sql_query = "SELECT empno \
            FROM emp \
            WHERE empno=? \
            AND job='SALESMAN'"
cursor.execute(sql_query,(cust_repid,))
emp_row = cursor.fetchone()
if emp_row is not None:
    # if the sales rep id exists, insert a new row into the customer table
    sql_insert = "INSERT INTO customer (name, repid, creditlimit) \
                  VALUES (?,?,?)"
    cursor.execute(sql_insert,(cust_name,cust_repid,cust_creditlimit))
    # commit the changes
    db.commit()
    print("Customer ",cust_name, "inserted successfully")
else:
    # if the sales rep id doesnt exist, print an error message
    print ("Sales rep id not found in the database")


























