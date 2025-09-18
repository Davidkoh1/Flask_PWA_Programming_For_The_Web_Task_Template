from flask import Flask, render_template, request, redirect, url_for
import database_manager as dbHandler

app = Flask(__name__)

# Route for the main page and index.html
@app.route('/', methods=['GET'])
@app.route('/landing.html', methods=['GET'])
def index():
    """Fetches data from the database and renders the main page."""
    data = dbHandler.listExtension()
    return render_template('landing.html', content=data)

# Route for the 'add' page
@app.route('/add.html', methods=['GET'])
def add():
    """Renders the form to add a new extension."""
    return render_template('add.html')

@app.route('/landing.html', methods=['GET'])
def landing():
    """Renders the form to add a new extension."""
    return render_template('landing.html')

# This function name has been changed to 'signup' to avoid a conflict.
@app.route('/signup.html', methods=['GET'])
def signup():
    """Renders the form for the sign-up page."""
    return render_template('signup.html')

@app.route('/login.html', methods=['GET'])
def login():
    """Renders the form for the sign-up page."""
    return render_template('login.html')

# New route to handle the form submission (POST request)
@app.route('/signup', methods=['POST'])
def process_signup():
    """
    Processes the signup form submission.
    This function is called when the form is submitted to the '/signup' URL.
    """
    # Extract data from the form fields using request.form
    first_name = request.form['first_Name']
    last_name = request.form['last_Name']
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']

    print("DEBUG: Attempting to call dbHandler.add_user()...")
    dbHandler.add_user(first_name, last_name, username, email, phone, password)
    print("DEBUG: dbHandler.add_user() call completed.")

    # Redirect the user back to the home page after a successful signup
    # This prevents the form from being resubmitted if the user
    # refreshes the page.
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def process_login():
    """
    Processes the login form submission.
    This function authenticates the user by checking their credentials.
    """
    username = request.form['username']
    password = request.form['password']

    if dbHandler.check_user_credentials(username, password):
        print("Login successful.")
        return redirect(url_for('index'))
    else:
        print("Login failed.")
        return redirect(url_for('login'))

if __name__ == '__main__':
    # Running in debug mode to see errors in the browser.
    app.run(debug=True, host='0.0.0.0', port=5000)
