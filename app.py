from flask import Flask, render_template, request, jsonify
from openpyxl import load_workbook, Workbook
import os

app = Flask(__name__)

# Route to render registration form
@app.route('/')
def index():
    return render_template('register.html')

# Route to handle form submission
@app.route('/register', methods=['POST'])
def register():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Define the filename
    filename = 'registration_data.xlsx'

    # Check if the file exists
    if os.path.exists(filename):
        wb = load_workbook(filename)
        ws = wb.active
    else:
        wb = Workbook()
        ws = wb.active
        # Append headers if the file is new
        ws.append(['Name', 'Email', 'Phone', 'Message'])

    # Append the new data
    ws.append([name, email, phone, message])
    wb.save(filename)  # Save Excel file

    # Provide feedback to user (using JSON for simplicity)
    return jsonify({"message": "Thank you for registering!"})

if __name__ == '__main__':
    app.run(debug=True)
