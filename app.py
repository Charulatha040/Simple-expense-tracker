%%writefile app.py  # Save this code as 'app.py'

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="expense_db"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense_name = request.form['expenseName']
    expense_amount = request.form['expenseAmount']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (name, amount) VALUES (%s, %s)", (expense_name, expense_amount))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  # disable auto-reloading for Jupyter
