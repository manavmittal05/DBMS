from datetime import datetime
from tabulate import tabulate


def query1(cursor):
    # query to create sale order
    entry = 1
    medicine = {}
    customer = int(input("Enter customer ID: "))
    employee = int(input("Enter employee ID: "))
    while entry == 1:
        med_id = int(input("Enter medicine ID: "))
        medicine[med_id] = int(input("Enter the quantity: "))
        entry = int(input("Want to add more press 1 else 0: "))
    date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute(
        f"insert into sale_order(date, customer, employee) values ('{date}', {customer}, {employee})")
    cursor.execute(
        f"select order_id from sale_order where date='{date}' and customer={customer} and employee={employee}")

    order_id = cursor.fetchall()[0][0]

    for i in medicine.keys():
        cursor.execute(
            f"insert into sale_medicine(medicine_id, quantity, order_id) value ({i}, {medicine[i]}, {order_id})")
        cursor.execute(f"update medicine set quantity=quantity-{medicine[i]} where medicine_id={i}")
    cursor.execute(
        f"select order_id,date,Total from (select order_id, date, round(sum(total)*0.9*1.18, 2) AS TOTAL from (select so.order_id, so.date, selling_price*sm.quantity total from sale_medicine sm, sale_order so, medicine m where sm.order_id=so.order_id and sm.medicine_id=m.medicine_id order by order_id) inv group by order_id order by order_id) t where order_id = {order_id}")
    data = cursor.fetchall()
    cursor.execute(f"insert into invoice (date, tax, discount, total, `order`) value ('{data[0][1]}', 18.0, 10.0, {data[0][2]}, {data[0][0]})")
    print("Order Created and Invoice generated successfully!")
    cursor.execute(f"select * from invoice where `order`={order_id}")
    print(tabulate(cursor.fetchall(), headers=['Invoice ID', 'Date', 'Tax', 'Discount', 'Total', 'Order ID']))


def query2(cursor):
    # query to update stock of the medicines automatically when a purchase order is delivered to the store
    order_id = int(input("Enter Order ID: "))
    cursor.execute(f"select status from purchase_order where order_id={order_id}")
    status = cursor.fetchall()
    if status[0][0] == 'delivered':
        return "Order has been already delivered! No stock is updated."
    cursor.execute(f"select medicine, quantity from purchase_medicine where order_id={order_id}")
    data = cursor.fetchall()
    for i in data:
        cursor.execute(f"update medicine set quantity=quantity+{i[1]} where medicine_id={i[0]}")
    cursor.execute(f'update purchase_order set status="delivered" where order_id={order_id}')
    return "Status updated successfully and quantities are added to the stock!"
