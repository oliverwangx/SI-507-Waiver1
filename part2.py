# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

mydb=sqlite3.connect("Northwind_small.sqlite")

cursor=mydb.cursor()


if sys.argv[1]=="customers":
    cursor.execute(" SELECT id,CompanyName from Customer")
    print("ID	Customer Name")
    for row in cursor:
        one=row[0].encode("utf-8")
        two=row[1].encode("utf-8")
        print (one+' '+two)




if sys.argv[1]=="employees":
    cursor.execute(" SELECT Id,FirstName,LastName from  Employee")
    print("ID	 Employee Name")
    for row in cursor:
        one = row[1].encode("utf-8")
        two=row[2].encode("utf-8")
        print (str(row[0])+' 	 '+one+' '+two)


if sys.argv[1]=="orders":
    if sys.argv[2][0:4]=='cust':
        cursor.execute(" SELECT CustomerId,OrderDate from  `Order`")
        print("Order dates")
        for row in cursor:
            if  row[0]==sys.argv[2][5:] :
                 print (row[1])
    elif sys.argv[2][0:3]=='emp':
        temp=-1
        cursor.execute(" SELECT Id, LastName from  Employee")
        for row in cursor:
            one = row[1].encode("utf-8")
            if one==sys.argv[2][4:]:
                temp=row[0]
                break
        cursor.execute(" SELECT EmployeeId, OrderDate from  `Order`")
        print("Order dates")
        for row in cursor:
            if row[0]==temp:
               print(row[1])


mydb.close()

#[(u'Employee',), (u'Category',), (u'Customer',), (u'Shipper',), (u'Supplier',), (u'Order',), (u'Product',), (u'OrderDetail',), (u'CustomerCustomerDemo',), (u'CustomerDemographic',), (u'Region',), (u'Territory',), (u'EmployeeTerritory',)]

