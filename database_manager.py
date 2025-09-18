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
