import sqlite3
def creating_db():
    try:
        sqliteConnection = sqlite3.connect('Map.db')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Murugappa_Login (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    username TEXT NOT NULL,
                                    pswrd TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

def inserting_values_into_db():
    try:
        sqliteConnection = sqlite3.connect('Map.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO Murugappa_Login
                            (username, pswrd) 
                            VALUES 
                            ('finalyearproject','myproject@murugappa')"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

creating_db()
inserting_values_into_db()