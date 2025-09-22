import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute('SELECT * FROM extension').fetchall()
    con.close()
    return data


def add_user(first_name, last_name, username, email, phone, password):
    """Inserts a new user into the 'users' table."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        cur = conn.cursor()

        # SQL query using a parameterized statement to prevent SQL injection.
        query = """
        INSERT INTO User (first_name, last_name, user_Name, email, phone, password)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        cur.execute(query, (first_name, last_name, username, email, phone, password))
        conn.commit()
        print("User added successfully!")

    except sql.Error as e:
        print(f"Database error: {e}")


    finally:
        if conn:
            conn.close()


def check_user_credentials(username, password):
    """Checks if a user's credentials are valid."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        cur = conn.cursor()

        query = "SELECT user_Name, password FROM User WHERE user_Name = ? AND password = ?"
        cur.execute(query, (username, password))

        user = cur.fetchone()

        if user:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    except sql.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if conn:
            conn.close()

def get_user_Id(username):
    """Retrieves the user_Id for a given username."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        cur = conn.cursor()

        # The SQL query to select the user_Id where the user_Name matches
        query = "SELECT user_Id FROM User WHERE user_Name = ?"
        cur.execute(query, (username,))

        # Fetch the first result (since usernames should be unique)
        user_id = cur.fetchone()

        if user_id:
            # user_id is a tuple, so we get the first element
            print(f"User ID for {username} is: {user_id[0]}")
            return user_id[0]
        else:
            print(f"No user found with username: {username}")
            return None
    except sql.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

# Add this new function to your existing database_manager.py file

def get_user_info(user_id):
    """Retrieves user information from the database by user ID."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        conn.row_factory = sql.Row  # This will allow us to get results as a dictionary-like object
        cur = conn.cursor()

        query = "SELECT user_Name, first_Name, last_Name FROM User WHERE user_Id = ?"
        cur.execute(query, (user_id,))

        user_row = cur.fetchone()
        
        if user_row:
            # Return the row as a dictionary
            return dict(user_row)
        else:
            return None
    except sql.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()
