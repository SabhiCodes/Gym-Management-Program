from ast import Add
import mysql.connector
from mysql.connector import errorcode
from tabulate import tabulate
def emp_search():
    try:
        cnx = mysql.connector.connect(user = 'root', password = 'abhi1234', host = 'localhost', database = 'cbseexamdb') 
        cursor = cnx.cursor()
        ino = int(input('Enter the IDno whose record you want to see : '))
        qry = ("SELECT * FROM employee WHERE IDno = %s")
        rec_search= (ino,)
        cursor.execute(qry,rec_search)
        for (IDno, Name, Phone_number, Address, time) in cursor:
            head = [['IDno', 'Name', 'Phone_number', 'Address', 'time']]
            body = [IDno, Name, Phone_number, Address, time]
            head.append(body)
            print(tabulate(head, headers='firstrow', tablefmt='fancy_grid'))
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def emp_write():
    try:
        cnx = mysql.connector.connect(user = 'root', password = 'abhi1234', host = 'localhost', database = 'cbseexamdb') 
        cursor = cnx.cursor()
        NE = int(input('Enter the number of enteries you want to make in the table : '))
        for i in range(NE):
            IDno = int(input('Enter the ID number of the employee: '))
            name = input('Enter the name of the employee: ')
            Pno = int(input('Enter the Phone number of the employee: '))
            Address = input('Enter the Address of employee: ')
            time = input('Enter the time (in hours): ')
            Qry = ("INSERT INTO employee VALUES (%s,%s,%s,%s,%s)")
            data = (IDno,name,Pno,Address,time)
            cursor.execute(Qry,data)
            print('Done!')
        cnx.commit()
        cursor.close()
        cnx.close()
        print("New record inserted.......")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

def emp_del():
    try:
        cnx = mysql.connector.connect(user = 'root', password = 'abhi1234', host = 'localhost', database = 'cbseexamdb')
        Cursor = cnx.cursor()
        ino = int(input("Enter the IDno whose record you want to delete : "))
        query = ("DELETE FROM employee WHERE IDno = %s")
        del_rec = (ino,)
        Cursor.execute(query, del_rec)
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

