import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('job_applications.db')
cursor = conn.cursor()

# Create a table to store job applications
cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_applications (
        serial_number INTEGER PRIMARY KEY,
        company TEXT NOT NULL,
        job_title TEXT NOT NULL,
        job_description_link TEXT,
        date TEXT NOT NULL,
        result TEXT NOT NULL,
        location TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
