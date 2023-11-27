# app.py
from flask import Flask, render_template, request, redirect
import sqlite3
from flask import render_template_string
import time
app = Flask(__name__)


# ... (existing code)

# Sample data

# ... (existing code)

# Create a simple SQLite database
conn = sqlite3.connect('watches.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        price REAL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        address TEXT,
        zip_code TEXT,
        credit_card TEXT
    )
''')
conn.commit()
conn.close()

# Sample data
products = [
    {"name": "Blackhead Remover Vacuum, Black Head Extractions Tool with Camera ", "description": "Blackhead Remover Vacuum, Black Head Extractions Tool with Camera for USB Interface Type Pore Vacuum, Men and Women Pore Cleaner, 6 Suction Heads & 3 Adjustment Modes (Pink)", "price": 49},

    # Add more products as needed
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/buy/<int:product_id>')
def buy(product_id):
    product = products[product_id - 1]
    return render_template('gshockbuy.html', product=product)
# ... (previous code)


# ... (existing code)

# ... (existing code)

@app.route('/purchase', methods=['POST'])
def purchase():
    try:
        if request.method == 'POST':
            # Retrieve data from the form
            name = request.form.get('name')
            address = request.form.get('address')
            zip_code = request.form.get('zip_code')
            credit_card = request.form.get('credit_card')
            exp = request.form.get('exp')
            cvc = request.form.get('cvc')
            email = request.form.get('email')
            product_id = int(request.form.get('product_id', 0))

            # Validate form data
            if not all([name, address, zip_code, credit_card, exp, cvc, email]):
                raise ValueError("All form fields must be filled.")

            # Retrieve the product information based on the product_id
            product = products[product_id - 1]

            # Print the information to the console (for demonstration purposes)
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Address: {address}")
            print(f"ZIP Code: {zip_code}")
            print(f"Credit Card: {credit_card}")
            print(f"CVC: {cvc}")
            print(f"Exp Date: {exp}")

            # Print the product information

            print(f"Price: ${product['price']}")

            # Save the information to the database
            conn = sqlite3.connect('watches.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO purchases (name, address, zip_code, credit_card, product_id, cvc, exp, email)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, address, zip_code, credit_card, product_id, cvc, exp, email))
            conn.commit()
            conn.close()

        return render_template('thank_you.html')

    except Exception as e:
        # Log the error (replace print with appropriate logging mechanism)
        print(f"Error during purchase: {str(e)}")

    # Redirect to the home page in case of an error
        return render_template('thank_you.html')


# ... (existing code)


if __name__ == '__main__':
    app.run(debug=True, port=5000)