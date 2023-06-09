import mysql.connector
from embeddedQueries import query2, query1
from tabulate import tabulate
from matplotlib import pyplot as plt
import datetime

def main_menu():
    print('''
    1. Customer realted queries
    2. Employee related queries
    3. Medicine related queries
    4. Supplier related queries
    5. Sale related queries
    6. Purchase related queries
    7. Invoice related queries
    8. Report geneartion
    9. Add admin
    10. Exit''')


def customer_menu():
    print('''
    1. Add a new Customer
    2. Add customer contact details
    3. Delete a Customer
    4. List all the Customers
    5. Print Customer details
    6. Go back to main menu''')


def employee_menu():
    print('''
    1. Add an Employee
    2. Add an Employee contact details
    3. Delete an Employee
    4. List all the Employees
    5. Print Employee details
    6. Go back to main menu''')

def medicine_menu():
    print('''
    1. Add a new Medicine
    2. List all the Medicines
    3. Print Medicine details
    4. Go back to main menu''')

def supplier_menu():
    print('''
    1. Add a new Supplier
    2. Add a new Supplier contact details
    3. List all the Suppliers
    4. Print Supplier details
    5. Go back to main menu''')

def sale_menu():
    print('''
    1. Create a sale order
    2. List all the sale orders
    3. Print sale order details
    4. Go back to main menu''')

def purchase_menu():
    print('''
    1. Create a purchase order
    2. Mark a purchase order as delivered
    3. List all the purchase orders
    4. Print purchase order details
    5. Go back to main menu''')

def invoice_menu():
    print('''
    1. Print Invoice
    2. List all the invoices
    3. Go back to main menu''')

def report_menu():
    print('''
    1. Tell the employee of the month
    2. Tell the employee of the year
    3. Graph sale in a month wise
    4. Graph sale in a year-wise
    5. Graph loss in a month wise
    6. Graph loss in a year-wise
    7. Go back to main menu''')



def main(authorization_lvl):
    mydb = mysql.connector.connect(user="root", password="Ma@060304", host="localhost", database="mydb")
    cursor = mydb.cursor()

    while True:
        print("Welcome to RxPro - 'Exceeding expectations in pharmacy care.'")
        main_menu()
        choice = int(input("You choice: "))
        if choice == 1:
            while True:
                customer_menu()
                choice = int(input("You choice: "))
                if choice == 1:

                    firstname = input("Enter the firstname of the customer: ")
                    middlename = input("Enter the middlename of the customer: ")
                    lastname = input("Enter the lastname of the customer: ")
                    dob = input("Enter the date of birth of the customer format(yyyy-mm-dd): ")
                    house_no = input("Enter the house number of the customer: ")
                    street = input("Enter the street of the customer: ")
                    locality = input("Enter the locality of the customer: ")
                    city = input("Enter the city of the customer: ")
                    state = input("Enter the state of the customer: ")
                    pincode = input("Enter the pincode of the customer: ")
                    # contact = int(input("Enter the contact number of the customer: "))

                    query = f"insert into customer(firstname, middlename, lastname, dob, house_no, street, locality, city, state, pincode) values('{firstname}', '{middlename}', '{lastname}', '{dob}', '{house_no}', '{street}', '{locality}', '{city}', '{state}', {pincode})"
                    cursor.execute(query)
                    mydb.commit()
                    print("Customer added successfully!")


                elif choice == 2:

                    # add customer contact details
                    firstname = input("Enter the firstname of the customer: ")
                    middlename = input("Enter the middlename of the customer: ")
                    lastname = input("Enter the lastname of the customer: ")
                    dob = input("Enter the date of birth of the customer format(yyyy-mm-dd): ")

                    # select the customer id
                    query = f"select * from customer where firstname='{firstname}' and middlename='{middlename}' and lastname='{lastname}' and dob='{dob}'"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    # print the data in table using tabulate
                    print(tabulate(data, headers=['Customer ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                    customer_id = int(input("Enter the customer id: "))
                    phone = int(input("Enter the phone number: "))

                    query = f"insert into customer_contact(customer, phone_number) values({customer_id}, {phone})"
                    cursor.execute(query)
                    mydb.commit()
                    print("Customer contact details added successfully!")

                elif choice == 3:

                    firstname = input("Enter the firstname of the customer: ")
                    middlename = input("Enter the middlename of the customer: ")
                    lastname = input("Enter the lastname of the customer: ")
                    dob = input("Enter the date of birth of the customer format(yyyy-mm-dd): ")

                    # select the customer id
                    query = f"select * from customer where firstname='{firstname}' and middlename='{middlename}' and lastname='{lastname}' and dob='{dob}'"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    # print the data in table using tabulate
                    print(tabulate(data, headers=['Customer ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                    customer_id = int(input("Enter the customer id: "))
                    cursor.execute(f"delete from customer_contact where customer={customer_id}")
                    cursor.execute(f"delete from customer where customer_id={customer_id}")
                    mydb.commit()
                    print("Customer deleted successfully!")

                elif choice == 4:
                    cursor.execute("select * from customer")
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Customer ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))
               
                elif choice == 5:
                    customer_id = int(input("Enter the customer id: "))
                    cursor.execute(f"select * from customer where customer_id={customer_id}")
                    data = cursor.fetchall()
                    # convert all int to str
                    data = [[str(i) for i in j] for j in data]
                    print(tabulate(data, headers=['Customer ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                    # print contact details
                    cursor.execute(f"select phone_number from customer_contact where customer={customer_id}")
                    data = cursor.fetchall()
                    # convert all int to str
                    data = [[str(i) for i in j] for j in data]
                    print(tabulate(data, headers=['Contact'], tablefmt='psql'))

                elif choice == 6:
                    break

        elif choice == 2:
            if authorization_lvl == True:
                while True:
                    employee_menu()
                    choice = int(input("You choice: "))
                    if choice == 1:
                        firstname = input("Enter the firstname of the employee: ")
                        middlename = input("Enter the middlename of the employee: ")
                        lastname = input("Enter the lastname of the employee: ")
                        dob = input("Enter the date of birth of the employee format(yyyy-mm-dd): ")
                        house_no = input("Enter the house number of the employee: ")
                        street = input("Enter the street of the employee: ")
                        locality = input("Enter the locality of the employee: ")
                        city = input("Enter the city of the employee: ")
                        state = input("Enter the state of the employee: ")
                        pincode = input("Enter the pincode of the employee: ")

                        # select max employee id
                        cursor.execute("select max(employee_id) from employee")
                        data = cursor.fetchall()
                        employee_id = data[0][0] + 1

                        query = f"insert into employee(employee_id, firstname, middlename, lastname, dob, house_no, street, locality, city, state, pincode) values({employee_id}, '{firstname}', '{middlename}', '{lastname}', '{dob}', '{house_no}', '{street}', '{locality}', '{city}', '{state}', '{pincode}')"
                        cursor.execute(query)
                        mydb.commit()
                        print("Employee added successfully!")

                    elif choice == 2:

                        # add employee contact details
                        firstname = input("Enter the firstname of the employee: ")
                        middlename = input("Enter the middlename of the employee: ")
                        lastname = input("Enter the lastname of the employee: ")
                        dob = input("Enter the date of birth of the employee format(yyyy-mm-dd): ")

                        # select the employee id
                        query = f"select * from employee where firstname='{firstname}' and middlename='{middlename}' and lastname='{lastname}' and dob='{dob}'"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        # print the data in table using tabulate
                        print(tabulate(data, headers=['Employee ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                        employee_id = int(input("Enter the employee id: "))
                        phone = int(input("Enter the phone number: "))

                        query = f"insert into employee_contact(employee, phone_number) values({employee_id}, {phone})"
                        cursor.execute(query)
                        mydb.commit()
                        # print("Employee contact details added successfully!")

                    elif choice == 3:

                        firstname = input("Enter the firstname of the employee: ")
                        middlename = input("Enter the middlename of the employee: ")
                        lastname = input("Enter the lastname of the employee: ")
                        dob = input("Enter the date of birth of the employee format(yyyy-mm-dd): ")

                        # select the employee id
                        query = f"select * from employee where firstname='{firstname}' and middlename='{middlename}' and lastname='{lastname}' and dob='{dob}'"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        # print the data in table using tabulate
                        print(tabulate(data, headers=['Employee ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                        employee_id = int(input("Enter the employee id: "))
                        cursor.execute(f"delete from employee where employee_id={employee_id}")
                        mydb.commit()
                        print("Employee deleted successfully!")

                    elif choice == 4:
                        cursor.execute("select * from employee")
                        data = cursor.fetchall()
                        print(tabulate(data, headers=['Employee ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))
                    
                    elif choice == 5:
                        employee_id = int(input("Enter the employee id: "))
                        cursor.execute(f"select * from employee where employee_id={employee_id}")
                        data = cursor.fetchall()
                        # convert all int to str
                        data = [[str(i) for i in j] for j in data]
                        print(tabulate(data, headers=['Employee ID', 'First Name', 'Middle Name', 'Last Name', 'DOB', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                        # print contact details
                        cursor.execute(f"select phone_number from employee_contact where employee={employee_id}")
                        data = cursor.fetchall()
                        # convert all int to str
                        data = [[str(i) for i in j] for j in data]
                        print(tabulate(data, headers=['Contact'], tablefmt='psql'))

                    elif choice == 6:
                        break
            else:
                print("You are not authorized to access this menu!")
        
        elif choice == 3:
            while True:
                medicine_menu()
                choice = int(input("You choice: "))
                if choice == 1:
                    medicine_name = input("Enter the name of the medicine: ")
                    medicine_mfg_date = input("Enter the manufacturing date of the medicine format(yyyy-mm-dd): ")
                    medicine_expiry_date = input("Enter the expiry date of the medicine format(yyyy-mm-dd): ")
                    medicine_cost_price = int(input("Enter the cost price of the medicine: "))
                    medicine_selling_price = int(input("Enter the selling price of the medicine: "))
                    medicine_quantity = int(input("Enter the quantity of the medicine: "))
                    medicine_company = int(input("Enter the company id of the medicine: "))
                    
                    query = f"insert into medicine(name, mfg_date, exp_date, cost_price, selling_price, quantity, company) values('{medicine_name}', '{medicine_mfg_date}', '{medicine_expiry_date}', {medicine_cost_price}, {medicine_selling_price}, {medicine_quantity}, {medicine_company})"

                    cursor.execute(query)
                    mydb.commit()
                    print("Medicine added successfully!")
                
                elif choice == 2:
                    query = "select * from medicine"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Medicine ID', 'Medicine Name', 'Mfg Date', 'Exp Date', 'Cost Price', 'Selling Price', 'Quantity', 'Company'], tablefmt='psql'))
                
                elif choice == 3:
                    # print all details of a particular medicine
                    medicine_id = int(input("Enter the medicine id: "))
                    query = f"select * from medicine where medicine_id={medicine_id}"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Medicine ID', 'Medicine Name', 'Mfg Date', 'Exp Date', 'Cost Price', 'Selling Price', 'Quantity', 'Company'], tablefmt='psql'))

                elif choice == 4:
                    break
            
        elif choice == 4:
            if authorization_lvl:
                while True:
                    supplier_menu()
                    choice = int(input("You choice: "))
                    if choice == 1:
                        company_id = int(input("Enter the company id: "))
                        name = input("Enter the name of the supplier: ")
                        house_no = input("Enter the house number of the supplier: ")
                        street = input("Enter the street of the supplier: ")
                        locality = input("Enter the locality of the supplier: ")
                        city = input("Enter the city of the supplier: ")
                        state = input("Enter the state of the supplier: ")
                        pincode = int(input("Enter the pincode of the supplier: "))

                        query = f"insert into medicine_company(company_id, name, house_no, street, locality, city, state, pincode) values({company_id}, '{name}', '{house_no}', '{street}', '{locality}', '{city}', '{state}', {pincode})"
                        cursor.execute(query)
                        mydb.commit()
                        print("Supplier added successfully!")

                    elif choice == 2:
                        # add medicine company contact_details
                        company_id = int(input("Enter the company id: "))
                        phone = int(input("Enter the phone number of the supplier: "))

                        query = f"insert into company_contact(company, phone_number) values({company_id}, {phone})"
                        cursor.execute(query)
                        mydb.commit()
                        print("Supplier contact details added successfully!")

                    elif choice == 3:
                        # print all the suppliers
                        query = "select * from medicine_company"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(tabulate(data, headers=['Company ID', 'Name', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                    elif choice == 4:
                        # print details of a particular supplier
                        company_id = int(input("Enter the company id: "))
                        query = f"select * from medicine_company where company_id={company_id}"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(tabulate(data, headers=['Company ID', 'Name', 'House No', 'Street', 'Locality', 'City', 'State', 'Pincode'], tablefmt='psql'))

                        # print contact details
                        cursor.execute(f"select phone_number from company_contact where company={company_id}")
                        data = cursor.fetchall()
                        # convert all int to str
                        data = [[str(i) for i in j] for j in data]
                        print(tabulate(data, headers=['Contact'], tablefmt='psql'))
                    
                    elif choice == 5:
                        break
            else:
                print("You are not authorized to access this menu!")
            
        elif choice == 5:
            while True:
                sale_menu()
                choice = int(input("You choice: "))
                if choice == 1:
                    query1(cursor)
                    mydb.commit()
                elif choice == 2:
                    query = "select * from sale_order"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Order ID', 'Employee ID', 'Customer ID', 'Date', 'Total Amount'], tablefmt='psql'))
                elif choice == 3:
                    order_id = int(input("Enter the order id: "))
                    query = f"select * from sale_order where order_id={order_id}"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Order ID', 'Employee ID', 'Customer ID', 'Date', 'Total Amount'], tablefmt='psql'))
                    # select medicine from a sale_order
                    query = f"select sale_medicine.medicine_id, name, sale_medicine.quantity from sale_medicine, medicine where `order_id`={order_id} and sale_medicine.medicine_id=medicine.medicine_id"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Medicine ID', 'Medicine Name', 'Quantity'], tablefmt='psql'))

                    # select invoice from a sale_order
                    query = f"select * from invoice where `order`={order_id}"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Invoice ID', 'Date', 'Tax', 'Discount', 'Total Amount'], tablefmt='psql'))
                elif choice == 4:
                    break
        
        elif choice == 6:
            if authorization_lvl:

                while True:
                    purchase_menu()
                    choice = int(input("You choice: "))
                    if choice == 3:
                        query = "select * from purchase_order"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(tabulate(data, headers=['Order ID', 'Status', 'Date', 'Admin_ID', 'Company'], tablefmt='psql'))

                        
                    
                    elif choice == 4:
                        order_id = int(input("Enter the order id: "))
                        query = f"select * from purchase_order where order_id={order_id}"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(tabulate(data, headers=['Order ID', 'Status', 'Date', 'Admin_ID', 'Company'], tablefmt='psql'))

                        query = f"select medicine, name, purchase_medicine.quantity from purchase_medicine, medicine where `order_id`={order_id} and purchase_medicine.medicine=medicine.medicine_id"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(tabulate(data, headers=['Medicine ID', 'Quantity'], tablefmt='psql'))

                    
                    elif choice == 5:
                        break

                    elif choice == 2:
                        query2(cursor)
                        mydb.commit()
                    
                    elif choice == 1:
                        # create a purchase order
                        cursor.execute("select max(order_id) from purchase_order")
                        order_id = cursor.fetchone()[0] + 1
                        status = 'placed'
                        date = datetime.datetime.now().strftime("%Y-%m-%d")
                        admin_id = int(input("Enter the admin id: "))
                        company_id = int(input("Enter the company id: "))
                        query = f"insert into purchase_order(order_id, status, date, admin, company) values({order_id}, '{status}', '{date}', {admin_id}, {company_id})"
                        cursor.execute(query)

                        # add medicines to the order

                        cursor.execute(f"select medicine_id, name, cost_price, selling_price, quantity from medicine where company={company_id}")
                        data = cursor.fetchall()
                        print("Following medicines are sold by this comapanay:")
                        print(tabulate(data, headers=['Medicine ID', 'Name', 'Cost_price', 'Selling_price', 'Quantity'], tablefmt='psql'))

                        while True:
                            medicine_id = int(input("Enter the medicine id: "))
                            quantity = int(input("Enter the quantity of the medicine: "))
                            query = f"insert into purchase_medicine(order_id, medicine, quantity) values({order_id}, {medicine_id}, {quantity})"
                            cursor.execute(query)

                            add_more = input("Do you want to add more medicines to the order? (y/n): ")
                            if add_more == 'n':
                                break

                        mydb.commit()
            else:
                print("You are not authorized to access this menu!")

        elif choice == 7:
            while True:
                invoice_menu()
                choice = int(input("You choice: "))
                if choice == 2:
                    cursor.execute("select * from invoice")
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Invoice ID', 'Date', 'Tax', 'Discount', 'Total', 'Order ID'], tablefmt='psql'))
                elif choice == 1:
                    invoice_id = int(input("Enter the invoice id: "))
                    cursor.execute(f"select * from invoice where invoice_id={invoice_id}")
                    data = cursor.fetchall()
                    print(tabulate(data, headers=['Invoice ID', 'Date', 'Tax', 'Discount', 'Total', 'Order ID'], tablefmt='psql'))
                elif choice == 3:
                    break;
                    
        elif choice == 8:
            if authorization_lvl:
                while True:
                    report_menu()
                    choice = int(input("You choice: "))
                    if choice == 1:
                        # tell the employee of the month
                        cursor.execute("SELECT employee as employee_id,MONTH(date) as month,YEAR(date) as year,COUNT(order_id) as count FROM sale_order GROUP BY employee,YEAR(date),MONTH(date) WITH ROLLUP");
                        data = cursor.fetchall()
                        month = int(input("Enter the month number: "))
                        year = int(input("Enter the year: "))
                        max_employee = None
                        quantity_sold = 0
                        for i in data:
                            if str(i[1]) == str(month) and str(i[2]) == str(year) and i[3] > quantity_sold:
                                max_employee = i[0]
                                quantity_sold = i[3]
                        print(f"Employee ID is: {max_employee}")
                        query = f"select concat(firstname, ' ', middlename, ' ', lastname) from employee where employee_id={max_employee}"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(f"Employee name is: {data[0][0]}")

                    
                    elif choice == 2:
                        # tell the employee of the year
                        cursor.execute("SELECT employee as employee_id,MONTH(date) as month,YEAR(date) as year,COUNT(order_id) as count FROM sale_order GROUP BY employee,YEAR(date),MONTH(date) WITH ROLLUP");
                        data = cursor.fetchall()
                        year = int(input("Enter the year: "))
                        max_employee = None
                        quantity_sold = 0
                        for i in data:
                            if i[1] == None and str(i[2]) == str(year) and i[3] > quantity_sold:
                                max_employee = i[0]
                                quantity_sold = i[3]
                        print(f"Employee ID is: {max_employee}")
                        query = f"select concat(firstname, ' ', middlename, ' ', lastname) from employee where employee_id={max_employee}"
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(f"Employee name is: {data[0][0]}")
                    
                    elif choice == 3:
                        sale = []
                        timestamp = []
                        cursor.execute("select month(date) as month,year(date) as year,round(sum(total),2) as total_sale from invoice group by year(date),month(date) with rollup;")
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] is not None:
                                sale.append(i[2])
                                timestamp.append(str(i[0])+"/"+str(i[1]))
                        fig, ax = plt.subplots()
                        plt.bar(timestamp, sale, width=0.5)
                        ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
                        plt.show()

                    elif choice == 4:
                        sale = []
                        timestamp = []
                        cursor.execute("select month(date) as month,year(date) as year,round(sum(total),2) as total_sale from invoice group by year(date),month(date) with rollup;")
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] is None and i[1] is not None:
                                sale.append(i[2])
                                timestamp.append(str(i[1]))
                        fig, ax = plt.subplots()
                        plt.bar(timestamp, sale, width=0.5)
                        ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
                        plt.show()

                    elif choice == 5:
                        loss = []
                        timestamp = []
                        cursor.execute("SELECT YEAR(exp_date) AS year, MONTH(exp_date) AS month, ROUND(SUM(cost_price * quantity), 2) AS loss FROM medicine WHERE exp_date < CURRENT_DATE() GROUP BY YEAR(exp_date), MONTH(exp_date) WITH ROLLUP;")
                        data = cursor.fetchall()
                        for i in data:
                            if i[1] is not None:
                                loss.append(i[2])
                                timestamp.append(str(i[1]) + "/" + str(i[0]))
                        fig, ax = plt.subplots()
                        plt.bar(timestamp, loss, width=0.5)
                        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
                        plt.show()

                    elif choice == 6:
                        loss = []
                        timestamp = []
                        cursor.execute(
                            "SELECT YEAR(exp_date) AS year, MONTH(exp_date) AS month, ROUND(SUM(cost_price * quantity), 2) AS loss FROM medicine WHERE exp_date < CURRENT_DATE() GROUP BY YEAR(exp_date), MONTH(exp_date) WITH ROLLUP;")
                        data = cursor.fetchall()
                        for i in data:
                            if i[1] is None and i[0] is not None:
                                loss.append(i[2])
                                timestamp.append(str(i[0]))
                        fig, ax = plt.subplots()
                        plt.bar(timestamp, loss, width=0.5)
                        ax.set_xticklabels(ax.get_xticklabels(), rotation=30)
                        plt.show()

                    elif choice == 7:
                        break
            else:
                print("You are not authorized to access this data")

        elif choice == 10:
            mydb.commit()
            break

        elif choice == 9:
            # select max admin id from the admin table
            if authorization_lvl:
                cursor.execute("select max(admin_id) from admin")
                data = cursor.fetchall()
                admin_id = data[0][0] + 1

                # take input from the user
                print("Enter the details of the new admin")
                firstname = input("Enter the firstname: ")
                middlename = input("Enter the middlename: ")
                lastname = input("Enter the lastname: ")
                dob = input("Enter the date of birth (YYYY-MM-DD): ")
                house_no = input("Enter the house number: ")
                street = input("Enter the street: ")
                locality = input("Enter the locality: ")
                city = input("Enter the city: ")
                state = input("Enter the state: ")
                pincode = int(input("Enter the pincode: "))

                query = f"insert into admin values({admin_id},'{firstname}','{middlename}','{lastname}','{dob}','{house_no}','{street}','{locality}','{city}','{state}',{pincode})"
                cursor.execute(query)
                mydb.commit()
                print("Admin added successfully")
            else:
                print("You are not authorized to access this data")


    cursor.close()
    mydb.close()


if __name__ == "__main__":

    auth_conn = mysql.connector.connect(user="root", password="Ma@060304", host="localhost", database="mydb")
    auth_cursor = auth_conn.cursor()
    
    print('''Are you a Admin or Employee?''')
    print('''1. Admin''')
    print('''2. Employee''')
    choice = int(input("Enter your choice: "))

    if choice == 1:
        admin_id = int(input("Enter your admin id: "))
        admin_dob = input("Enter your date of birth (YYYY-MM-DD): ")
        query = f"select * from admin where admin_id={admin_id} and dob='{admin_dob}'"
        auth_cursor.execute(query)
        data = auth_cursor.fetchall()
        if len(data) == 0:
            print("Invalid credentials")
            auth_cursor.close()
            auth_conn.close()
            exit()
        else:
            auth_cursor.close()
            auth_conn.close()
            main(True)
    elif choice == 2:
        employee_id = int(input("Enter your employee id: "))
        employee_dob = input("Enter your date of birth (YYYY-MM-DD): ")
        query = f"select * from employee where employee_id={employee_id} and dob='{employee_dob}'"
        auth_cursor.execute(query)
        data = auth_cursor.fetchall()
        if len(data) == 0:
            print("Invalid credentials")
            auth_cursor.close()
            auth_conn.close()
            exit()
        else:
            auth_cursor.close()
            auth_conn.close()
            main(False)