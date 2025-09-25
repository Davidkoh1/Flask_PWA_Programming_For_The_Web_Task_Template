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
        query = "SELECT user_Id FROM User WHERE user_Name = ?"
        cur.execute(query, (username,))
        user_id = cur.fetchone()
        if user_id:
            return user_id[0]
        else:
            return None
    except sql.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()


def get_user_info(user_id):
    """Retrieves user information from the database by user ID."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        conn.row_factory = sql.Row
        cur = conn.cursor()
        query = "SELECT user_Name, first_Name, last_Name FROM User WHERE user_Id = ?"
        cur.execute(query, (user_id,))
        user_row = cur.fetchone()
        if user_row:
            return dict(user_row)
        else:
            return None
    except sql.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()


# ================================
# EVENT FUNCTIONS
# ================================

def get_all_events():
    """Fetch all events ordered by date and time."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        conn.row_factory = sql.Row  # lets us access columns by name
        cur = conn.cursor()
        query = """
        SELECT event_Id, name, description, date, time, image
        FROM Event
        WHERE date >= DATE('now')
        ORDER BY date, time
        """
        cur.execute(query)
        rows = cur.fetchall()
        print(rows)
        return [dict(row) for row in rows]
    except sql.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        if conn:
            conn.close()


def add_event(name, description, location, date, time, image):
    """Insert a new event into the Event table."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        cur = conn.cursor()
        query = """
        INSERT INTO Event (name, description, location, date, time, image)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cur.execute(query, (name, description, location, date, time, image))
        conn.commit()
    except sql.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def get_event_by_id(event_id):
    """Fetch a single event by its ID as a dictionary."""
    conn = None
    try:
        conn = sql.connect("database/data_source.db")
        conn.row_factory = sql.Row
        cur = conn.cursor()
        query = """
        SELECT event_Id, name, description, location, date, time, image
        FROM Event
        WHERE event_Id = ?
        """
        cur.execute(query, (event_id,))
        row = cur.fetchone()
        return dict(row) if row else None
    except sql.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()


