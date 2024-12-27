import tkinter as tk
import customtkinter as ctk
import oracledb
from tkinter import messagebox, Toplevel, Scrollbar, Canvas
from reportlab.pdfgen import canvas
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


# Function to connect to Oracle Database
def connect_to_db():
    return oracledb.connect(
        user="c##project", 
        password="123", 
        dsn="localhost:1521/xe"
    )

# Function to clear the current form
def clear_frame():
    for widget in frame.winfo_children():
        widget.grid_forget()

# Save Product Data
def save_product():
    p_id = p_id_entry.get()
    p_name = p_name_entry.get()
    cat_name = p_cat_name_entry.get()
    author = p_author_entry.get()
    if p_id and p_name and cat_name and author:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO product (p_id, cat_id, p_name, author) VALUES "
                       "(:p_id, (SELECT cat_id FROM category WHERE cat_name = :cat_name), :p_name, :author)", 
                       {"p_id": p_id, "cat_name": cat_name, "p_name": p_name, "author": author})
        connection.commit()
        cursor.close()
        connection.close()
        p_id_entry.delete(0, ctk.END)
        p_name_entry.delete(0, ctk.END)
        p_cat_name_entry.delete(0, ctk.END)
        p_author_entry.delete(0, ctk.END)
        messagebox.showinfo("Success", "Product added successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Save Employee Data
def save_employee():
    emp_id = emp_id_entry.get()
    emp_name = emp_name_entry.get()
    emp_position = emp_position_entry.get()
    if emp_id and emp_name and emp_position:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (emp_id, emp_name, emp_position) VALUES (:emp_id, :emp_name, :emp_position)", 
                       {"emp_id": emp_id, "emp_name": emp_name, "emp_position": emp_position})
        connection.commit()
        cursor.close()
        connection.close()
        emp_id_entry.delete(0, ctk.END)
        emp_name_entry.delete(0, ctk.END)
        emp_position_entry.delete(0, ctk.END)
        messagebox.showinfo("Success", "Employee added successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Save Customer Data
def save_customer():
    c_id = c_id_entry.get()
    cname = cname_entry.get()
    caddress = caddress_entry.get()
    if c_id and cname and caddress:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customer (c_id, cname, caddress) VALUES (:c_id, :cname, :caddress)", 
                       {"c_id": c_id, "cname": cname, "caddress": caddress})
        connection.commit()
        cursor.close()
        connection.close()
        c_id_entry.delete(0, ctk.END)
        cname_entry.delete(0, ctk.END)
        caddress_entry.delete(0, ctk.END)
        messagebox.showinfo("Success", "Customer added successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# View Products
def view_products():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT p_id, p_name, cat_name, author FROM product "
                   "JOIN category ON product.cat_id = category.cat_id")
    rows = cursor.fetchall()
    connection.close()

    # Create a new window for viewing products
    view_window = Toplevel(app)
    view_window.title("View Products")
    view_window.geometry("600x400")

    # Create a canvas and scrollbar for scrolling
    canvas = Canvas(view_window)
    scrollbar = Scrollbar(view_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold product data
    data_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Display the data
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            ctk.CTkLabel(data_frame, text=col).grid(row=i, column=j, padx=10, pady=10)

    data_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# View Employees
def view_employees():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT emp_id, emp_name, emp_position FROM employees")
    rows = cursor.fetchall()
    connection.close()

    # Create a new window for viewing employees
    view_window = Toplevel(app)
    view_window.title("View Employees")
    view_window.geometry("600x400")

    # Create a canvas and scrollbar for scrolling
    canvas = Canvas(view_window)
    scrollbar = Scrollbar(view_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold employee data
    data_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Display the data
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            ctk.CTkLabel(data_frame, text=col).grid(row=i, column=j, padx=10, pady=10)

    data_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# View Customers
def view_customers():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT c_id, cname, caddress FROM customer")
    rows = cursor.fetchall()
    connection.close()

    # Create a new window for viewing customers
    view_window = Toplevel(app)
    view_window.title("View Customers")
    view_window.geometry("600x400")

    # Create a canvas and scrollbar for scrolling
    canvas = Canvas(view_window)
    scrollbar = Scrollbar(view_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold customer data
    data_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Display the data
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            ctk.CTkLabel(data_frame, text=col).grid(row=i, column=j, padx=10, pady=10)

    data_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# View Stock
def view_stock():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT stock_id, stock_name, stock_address FROM stock")
    rows = cursor.fetchall()
    connection.close()

    # Create a new window for viewing stock
    view_window = Toplevel(app)
    view_window.title("View Stock")
    view_window.geometry("600x400")

    # Create a canvas and scrollbar for scrolling
    canvas = Canvas(view_window)
    scrollbar = Scrollbar(view_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold stock data
    data_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Display the data
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            ctk.CTkLabel(data_frame, text=col).grid(row=i, column=j, padx=10, pady=10)

    data_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# View Total Sales
def view_total_sales():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(price * qty) FROM saledetails")
    total_sales = cursor.fetchone()[0]
    connection.close()

    # Show the total sales in a new window
    total_sales_window = Toplevel(app)
    total_sales_window.title("Total Sales")
    total_sales_window.geometry("300x200")
    total_sales_window.configure(bg='black')  # Set black background

    # Add label with white text
    total_sales_label = ctk.CTkLabel(total_sales_window, text=f"Total Sales: {total_sales}", text_color="white", bg_color="black")
    total_sales_label.pack(padx=20, pady=20)

# Create Product Form
def create_product_form():
    clear_frame()
    
    p_id_label = ctk.CTkLabel(frame, text="Product ID:")
    p_id_label.grid(row=0, column=0, padx=10, pady=10)
    global p_id_entry
    p_id_entry = ctk.CTkEntry(frame)
    p_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    p_name_label = ctk.CTkLabel(frame, text="Product Name:")
    p_name_label.grid(row=1, column=0, padx=10, pady=10)
    global p_name_entry
    p_name_entry = ctk.CTkEntry(frame)
    p_name_entry.grid(row=1, column=1, padx=10, pady=10)
    
    p_cat_name_label = ctk.CTkLabel(frame, text="Category Name:")
    p_cat_name_label.grid(row=2, column=0, padx=10, pady=10)
    global p_cat_name_entry
    p_cat_name_entry = ctk.CTkEntry(frame)
    p_cat_name_entry.grid(row=2, column=1, padx=10, pady=10)
    
    p_author_label = ctk.CTkLabel(frame, text="Author:")
    p_author_label.grid(row=3, column=0, padx=10, pady=10)
    global p_author_entry
    p_author_entry = ctk.CTkEntry(frame)
    p_author_entry.grid(row=3, column=1, padx=10, pady=10)
    
    save_button = ctk.CTkButton(frame, text="Save Product", command=save_product, fg_color='black', text_color='white')
    save_button.grid(row=4, column=1, padx=10, pady=20)

# Create Employee Form
def create_employee_form():
    clear_frame()
    
    emp_id_label = ctk.CTkLabel(frame, text="Employee ID:")
    emp_id_label.grid(row=0, column=0, padx=10, pady=10)
    global emp_id_entry
    emp_id_entry = ctk.CTkEntry(frame)
    emp_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    emp_name_label = ctk.CTkLabel(frame, text="Employee Name:")
    emp_name_label.grid(row=1, column=0, padx=10, pady=10)
    global emp_name_entry
    emp_name_entry = ctk.CTkEntry(frame)
    emp_name_entry.grid(row=1, column=1, padx=10, pady=10)
    
    emp_position_label = ctk.CTkLabel(frame, text="Position:")
    emp_position_label.grid(row=2, column=0, padx=10, pady=10)
    global emp_position_entry
    emp_position_entry = ctk.CTkEntry(frame)
    emp_position_entry.grid(row=2, column=1, padx=10, pady=10)
    
    save_button = ctk.CTkButton(frame, text="Save Employee", command=save_employee, fg_color='black', text_color='white')
    save_button.grid(row=3, column=1, padx=10, pady=20)

# Create Customer Form
def create_customer_form():
    clear_frame()

    c_id_label = ctk.CTkLabel(frame, text="Customer ID:")
    c_id_label.grid(row=0, column=0, padx=10, pady=10)
    global c_id_entry
    c_id_entry = ctk.CTkEntry(frame)
    c_id_entry.grid(row=0, column=1, padx=10, pady=10)

    cname_label = ctk.CTkLabel(frame, text="Customer Name:")
    cname_label.grid(row=1, column=0, padx=10, pady=10)
    global cname_entry
    cname_entry = ctk.CTkEntry(frame)
    cname_entry.grid(row=1, column=1, padx=10, pady=10)

    caddress_label = ctk.CTkLabel(frame, text="Address:")
    caddress_label.grid(row=2, column=0, padx=10, pady=10)
    global caddress_entry
    caddress_entry = ctk.CTkEntry(frame)
    caddress_entry.grid(row=2, column=1, padx=10, pady=10)

    save_button = ctk.CTkButton(frame, text="Save Customer", command=save_customer, fg_color='black', text_color='white')
    save_button.grid(row=3, column=1, padx=10, pady=20)
# View Stock Balance
def view_stock_balance():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT stock_name, SUM(qty) AS total_stock
        FROM saledetails
        JOIN stock ON saledetails.stock_id = stock.stock_id
        GROUP BY stock_name
    """)
    rows = cursor.fetchall()
    connection.close()

    # Create a new window for viewing stock balance
    view_window = Toplevel(app)
    view_window.title("Stock Balance")
    view_window.geometry("600x400")

    # Create a canvas and scrollbar for scrolling
    canvas = Canvas(view_window)
    scrollbar = Scrollbar(view_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold stock balance data
    data_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Display the data
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            ctk.CTkLabel(data_frame, text=col).grid(row=i, column=j, padx=10, pady=10)

    data_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# View Customer Balance
def view_customer_balance():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT cname, SUM(price * qty) AS total_spent
        FROM saledetails
        JOIN sales ON saledetails.sale_id = sales.sale_id
        JOIN customer ON sales.c_id = customer.c_id
        GROUP BY cname
    """)
    rows = cursor.fetchall()
    connection.close()

    # Create a new window for viewing customer balance
    view_window = Toplevel(app)
    view_window.title("Customer Balance")
    view_window.geometry("600x400")

    # Create a canvas and scrollbar for scrolling
    canvas = Canvas(view_window)
    scrollbar = Scrollbar(view_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold customer balance data
    data_frame = ctk.CTkFrame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Display the data
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            ctk.CTkLabel(data_frame, text=col).grid(row=i, column=j, padx=10, pady=10)

    data_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
def create_sell_form():
    clear_frame()  # Clears the current frame (assumes this function exists)

    global c_id_entry, cname_entry, caddress_entry, p_id_entry, qty_entry, price_entry, discount_entry, payment_method_var

    # Customer ID
    c_id_label = ctk.CTkLabel(frame, text="Customer ID:")
    c_id_label.grid(row=0, column=0, padx=10, pady=10)
    c_id_entry = ctk.CTkEntry(frame)
    c_id_entry.grid(row=0, column=1, padx=10, pady=10)

    # Customer Name
    cname_label = ctk.CTkLabel(frame, text="Customer Name:")
    cname_label.grid(row=1, column=0, padx=10, pady=10)
    cname_entry = ctk.CTkEntry(frame)
    cname_entry.grid(row=1, column=1, padx=10, pady=10)

    # Customer Address
    caddress_label = ctk.CTkLabel(frame, text="Customer Address:")
    caddress_label.grid(row=2, column=0, padx=10, pady=10)
    caddress_entry = ctk.CTkEntry(frame)
    caddress_entry.grid(row=2, column=1, padx=10, pady=10)

    # Product ID
    p_id_label = ctk.CTkLabel(frame, text="Product ID:")
    p_id_label.grid(row=3, column=0, padx=10, pady=10)
    p_id_entry = ctk.CTkEntry(frame)
    p_id_entry.grid(row=3, column=1, padx=10, pady=10)

    # Quantity
    qty_label = ctk.CTkLabel(frame, text="Quantity:")
    qty_label.grid(row=4, column=0, padx=10, pady=10)
    qty_entry = ctk.CTkEntry(frame)
    qty_entry.grid(row=4, column=1, padx=10, pady=10)

    # Price per Item
    price_label = ctk.CTkLabel(frame, text="Price per Item:")
    price_label.grid(row=5, column=0, padx=10, pady=10)
    price_entry = ctk.CTkEntry(frame)
    price_entry.grid(row=5, column=1, padx=10, pady=10)

    # Discount (%)
    discount_label = ctk.CTkLabel(frame, text="Discount (%):")
    discount_label.grid(row=6, column=0, padx=10, pady=10)
    discount_entry = ctk.CTkEntry(frame)
    discount_entry.grid(row=6, column=1, padx=10, pady=10)

    # Payment Method
    payment_method_label = ctk.CTkLabel(frame, text="Payment Method:")
    payment_method_label.grid(row=7, column=0, padx=10, pady=10)
    payment_method_var = ctk.StringVar(value="Cash")
    cash_button = ctk.CTkRadioButton(frame, text="Cash", variable=payment_method_var, value="Cash")
    cash_button.grid(row=7, column=1, padx=5, pady=10)
    bank_button = ctk.CTkRadioButton(frame, text="Bank", variable=payment_method_var, value="Bank")
    bank_button.grid(row=7, column=2, padx=5, pady=10)

    # Save Sale button (next to Payment Method options)
    save_button = ctk.CTkButton(frame, text="Save Sale", command=sell_product, fg_color='black', text_color='white')
    save_button.grid(row=7, column=3, padx=10, pady=10)


def sell_product():
    try:
        c_id = c_id_entry.get()
        cname = cname_entry.get()
        caddress = caddress_entry.get()
        p_id = p_id_entry.get()
        qty = int(qty_entry.get())
        price = float(price_entry.get())
        discount = float(discount_entry.get())
        payment_method = payment_method_var.get()

        if not (c_id and cname and caddress and p_id and qty and price and payment_method):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        total_amount = price * qty * (1 - discount / 100)
        messagebox.showinfo("Success", f"Sale completed successfully.\nTotal amount: {total_amount:.2f}")

        print("\n" + "="*30)
        print("ELMI Stationary Mart")
        print("="*30)
        print(f"Customer Name: {cname}")
        print(f"Address: {caddress}")
        print(f"Product ID: {p_id}")
        print(f"Quantity: {qty}")
        print(f"Price per Item: {price:.2f}")
        print(f"Discount: {discount}%")
        print(f"Payment Method: {payment_method}")
        print(f"Total Amount: {total_amount:.2f}")
        print("="*30)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for Quantity, Price, and Discount.")
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from tkinter import messagebox

# Example product name mapping based on product ID
product_dict = {
    1: "Notebook",
    2: "Pen",
    3: "Pencil",
    4: "Eraser",
    5: "Sharpener",
    # Add more products as needed
}

# Function to get the product name from the database using product ID
# Function to get the product name from the database using product ID
def get_product_name_from_db(p_id):
    try:
        # Connect to the Oracle Database using Easy Connect (no need for tnsnames.ora)
        conn = oracledb.connect(user="c##project", password="123", dsn="localhost:1521/xe")
        cursor = conn.cursor()

        # Query to get the product name from the PRODUCT table by product ID
        query = "SELECT p_name FROM product WHERE p_id = :id"
        cursor.execute(query, (p_id,))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            return result[0]  # Return the product name if found
        else:
            print(f"Product with ID {p_id} not found.")  # Log this case
            return "Unknown Product"  # Return a default name if not found
    
    except oracledb.DatabaseError as e:
        # Log the error and show it to the user
        error, = e.args
        print(f"Database error: {error.message}")
        return "Error retrieving product name"
    
    finally:
        # Ensure the database connection is closed
        cursor.close()
        conn.close()

# Function to generate a larger PDF bill with table layout and product name
def generate_pdf_bill(cname, caddress, p_id, qty, price, discount, payment_method, total_amount):
    # Get the product name using the product ID
    product_name = get_product_name_from_db(p_id)
    
    # Define the directory where the PDF will be saved
    save_directory = r"C:\Users\SHC\Desktop\Project\Mart"  # Directory where the bill will be saved
    
    # Check if the directory exists, and create it if not
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create the directory if it doesn't exist
    
    # Create the full file path where the PDF will be saved
    file_name = os.path.join(save_directory, f"bill_{cname}_{p_id}.pdf")
    
    # Create a SimpleDocTemplate object to generate the PDF
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    
    # Create a title for the bill
    styles = getSampleStyleSheet()
    title = Paragraph("ELMI STATIONERY MART", styles['Title'])
    
    # Add some space after the title
    spacer = Spacer(1, 12)
    
    # Create a list for the table data with appropriate field names
    table_data = [
        ["Customer Name", cname],
        ["Customer Address", caddress],
        ["Product Name", product_name],  # Use product name instead of product ID
        ["Quantity", qty],
        ["Price per Item", f"{price:.2f}"],
        ["Discount", f"{discount}%"],
        ["Payment Method", payment_method],
        ["Total Amount", f"{total_amount:.2f}"]
    ]
    
    # Create a Table object using the data
    table = Table(table_data, colWidths=[200, 300], rowHeights=30)
    
    # Define a TableStyle to style the table with more space
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 14),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),  # Align values to the left
    ])
    
    # Apply the TableStyle to the table
    table.setStyle(table_style)
    
    # Build the PDF with the title and table
    doc.build([title, spacer, table])
    
    # Optionally, show a message box to inform the user that the bill was saved
    messagebox.showinfo("Success", f"Bill saved as {file_name}")


# Function to sell products and generate the bill
def sell_product():
    try:
        # Retrieve input values
        c_id = c_id_entry.get()
        cname = cname_entry.get()
        caddress = caddress_entry.get()
        p_id = int(p_id_entry.get())  # Ensure p_id is an integer
        qty = int(qty_entry.get())
        price = float(price_entry.get())
        discount = float(discount_entry.get())
        payment_method = payment_method_var.get()

        if not (c_id and cname and caddress and p_id and qty and price and payment_method):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        total_amount = price * qty * (1 - discount / 100)

        # Database connection
        connection = connect_to_db()
        cursor = connection.cursor()

        # Get the next sale_id using the sequence
        cursor.execute("SELECT SALE_ID_SEQ.NEXTVAL FROM dual")
        sale_id = cursor.fetchone()[0]

        # Get the next bill_no using a sequence (assuming BILL_NO_SEQ exists)
        cursor.execute("SELECT BILL_NO_SEQ.NEXTVAL FROM dual")
        bill_no = cursor.fetchone()[0]

        # Insert into sales table with generated sale_id
        cursor.execute("""
            INSERT INTO sales (sale_id, c_id, sale_date) 
            VALUES (:1, :2, SYSDATE)
        """, [sale_id, c_id])

        # Insert into saledetails table (using generated bill_no)
        cursor.execute("""
            INSERT INTO saledetails (bill_no, sale_id, p_id, qty, price)
            VALUES (:1, :2, :3, :4, :5)
        """, [bill_no, sale_id, p_id, qty, price])

        # Commit and close the connection
        connection.commit()
        connection.close()

        messagebox.showinfo("Success", f"Sale completed successfully.\nTotal amount: {total_amount:.2f}")

        # Generate the PDF bill
        generate_pdf_bill(cname, caddress, p_id, qty, price, discount, payment_method, total_amount)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values for Quantity, Price, and Discount.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



# Main Application
app = ctk.CTk()
app.title("ELMI Stationary Mart")  # Set title here
app.geometry("700x700")

# Title Label at the top
title_label = ctk.CTkLabel(app, text="ELMI Stationary Mart", font=("Arial", 24), fg_color="black", text_color="white")
title_label.pack(padx=20, pady=20)

# Create navigation frame with buttons for each table
nav_frame = ctk.CTkFrame(app)
nav_frame.pack(padx=20, pady=10, fill="x")

# Buttons for adding and viewing tables (4 buttons per row)
button_data = [
    ("Add Product", create_product_form), 
    ("Add Employee", create_employee_form), 
    ("Add Customer", create_customer_form), 
    ("See Products", view_products),
    ("See Employees", view_employees), 
    ("See Customers", view_customers),
    ("See Stock", view_stock), 
    ("See Total Sales", view_total_sales),
    ("Stock Balance", view_stock_balance),
    ("Customer Balance", view_customer_balance),
    ("New Bill", create_sell_form)  # New button for the Sell form
]

# Arrange buttons in rows of 4
# Arrange buttons in rows of 4
for i, (text, command) in enumerate(button_data):
    row = i // 4
    col = i % 4
    button = ctk.CTkButton(nav_frame, text=text, command=command, fg_color="#0066cc", text_color="white")  # Blue background, white text
    button.grid(row=row, column=col, padx=10, pady=10)

# Create the frame that will hold the form
frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Run the application
app.mainloop()
