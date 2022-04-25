import mysql.connector
from tkinter import *
from tkinter import messagebox
f=open("crclstp.txt","a+")
f.close()
while True:
    try:
        config = {
            'host': 'b90kql12ysrlvaipie7i-mysql.services.clever-cloud.com',
            'database': 'b90kql12ysrlvaipie7i',
            'user': 'uhcklicofusmikjq',
            'port': '3306',
            'password': 'O4WzZ8rRwRqjhKxBeaEi',
        }
        cnxn = mysql.connector.connect(**config)
    except:
        print("Connection failed")
        root = Tk()
        root.geometry('0x0')
        answer = messagebox.askretrycancel(title='Connection Issue',message='The database server is unreachable. Do you want to retry?')
        if answer:
            root.destroy()
            continue
        else:
            try:
                root.destroy()
            except:
                break
        root.mainloop()
    else:
        c = cnxn.cursor()
        c.execute("set autocommit=1")
        c.execute("create table if not exists users(user_id varchar(10) primary key,user_email varchar(45), password varbinary(255), role varchar(10))")
        c.execute("create table if not exists customers(customer_id varchar(10),customer_name varchar(45), customer_email varchar(45), address varchar(100))")
        c.execute("create table if not exists vendors(vendor_id varchar(10) primary key, vendor_name varchar(45), vendor_email varchar(45))")
        c.execute("create table if not exists orders(order_id int primary key,product_name varchar(50), total_value int, vendor_id varchar(10) references vendors(vendor_id),customer_id varchar(10) references customers(customer_id), order_quantity int, reward_point int)")
        c.execute("create table if not exists items(product_id int auto_increment primary key, product_name varchar(45),product_qty int, product_description varchar(100), vendor_id varchar(10) references vendors(vendor_id), product_price float, emi_available varchar(10))")
        break