from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('k.html')

@app.route('/login', methods=['POST'])
def login():
    # Check username and password from form submission
    username = request.form['username']
    password = request.form['password']

    # Here, you would typically check the credentials against a database
    # For simplicity, we'll just check if the username is 'admin' and password is 'password'
    if username == 'admin' and password == 'password':
        return redirect(url_for('dashboard'))  # Redirect to dashboard if login is successful
    else:
        return render_template('k.html', message='Invalid username or password')  # Render index.html with an error message

@app.route('/dashboard')
def dashboard():
    # Render the dashboard.html template
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
