import sqlite3


#ddl command(create,alter)
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        date_of_birth DATE,
        gender TEXT,
        mobile_number TEXT,
        email_address TEXT
    );
""")

 
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")   