import os
from flask import Flask, render_template, request, send_from_directory
from openpyxl import Workbook

app = Flask(__name__)

# Define a directory outside of the web server root to store sensitive files
UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

    # Store data in Excel
    excel_path = os.path.join(UPLOAD_FOLDER, 'registration_data.xlsx')
    if not os.path.exists(excel_path):
        wb = Workbook()
        ws = wb.active
        ws.append(['Name', 'Email', 'Phone', 'Message'])
    else:
        wb = load_workbook(excel_path)
        ws = wb.active

    ws.append([name, email, phone, message])
    wb.save(excel_path)

    # Provide feedback to user (optional)
    return 'Thank you for registering!'

# Route to download the Excel file (restricted access)
@app.route('/download_excel')
def download_excel():
    excel_path = os.path.join(UPLOAD_FOLDER, 'registration_data.xlsx')
    return send_from_directory(directory=UPLOAD_FOLDER, filename='registration_data.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
