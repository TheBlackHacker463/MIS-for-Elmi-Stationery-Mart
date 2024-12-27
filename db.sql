create table tb_category
(
cat_id int constraint same_category_id primary key,
cat_name varchar2(30)
);

create table tb_product
(
p_id int constraint same_product_id primary key,
cat_id int references tb_category(cat_id),
p_name varchar2(30),
author varchar2(30),
publish_date date
);

create table tb_stock
(
stock_id int constraint same_stock_id primary key,
stock_name varchar2(30),
stock_address varchar2(30)
);

create table tb_customer
(
c_id int constraint same_customer_id primary key,
cname varchar2(30),
caddress varchar2(30)
);

create table tb_employees
(
emp_id int constraint same_emp_id primary key,
emp_name varchar2(30),
emp_position varchar2(30)
);

create table tb_sales
(
sale_id int constraint same_sale_id primary key,
c_id int references tb_customer(c_id),
sale_date date
);

create table tb_saledetails
(
bill_no int constraint same_bill_number primary key,
sale_id int references tb_sales(sale_id),
p_id int references tb_product(p_id),
stock_id int references tb_stock(stock_id),
qty int,
price int
);


create table tb_supplier
(
sup_id int constraint same_supplier_id primary key,
sup_name varchar2(30),
sup_address varchar2(30),
sup_phone number(10)
);

create table tb_purchase 
(
pur_id int constraint same_purchase_id primary key,
sup_id int references tb_supplier(sup_id),
pur_date date
);



create table tb_purchasedetails
(
ser_number int constraint same_serial_number primary key,
pur_id int references tb_purchase(pur_id),
p_id int references tb_product(p_id),
stock_id int references tb_stock(stock_id),
qty int,
price int
);

create table tb_payment
(
py_id int constraint same_payment_id primary key,
emp_id int references tb_employees(emp_id),
pur_id int references tb_purchase(pur_id),
py_date date,
paid int,
);