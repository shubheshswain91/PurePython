import tkinter as tk
from tkinter import messagebox
import sqlite3
import os

# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', ':0.0')
#     #setting = os.environ.__getitem__('DISPLAY')

def save_job_application():
    # Retrieve data from GUI input fields
    company = company_entry.get()
    job_title = job_title_entry.get()
    job_description_link = job_description_link_entry.get()
    date = date_entry.get()
    result = result_entry.get()
    location = location_entry.get()

    # Insert data into the database
    conn = sqlite3.connect('job_applications.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO job_applications 
        (company, job_title, job_description_link, date, result, location)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (company, job_title, job_description_link, date, result, location))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Job application saved successfully!")

# Create GUI window
root = tk.Tk()
root.title("Job Application Tracker")

# Create input fields and labels
tk.Label(root, text="Company:").grid(row=0, column=0)
company_entry = tk.Entry(root)
company_entry.grid(row=0, column=1)

tk.Label(root, text="Job Title:").grid(row=1, column=0)
job_title_entry = tk.Entry(root)
job_title_entry.grid(row=1, column=1)

tk.Label(root, text="Job Description Link:").grid(row=2, column=0)
job_description_link_entry = tk.Entry(root)
job_description_link_entry.grid(row=2, column=1)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=3, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1)

tk.Label(root, text="Result:").grid(row=4, column=0)
result_entry = tk.Entry(root)
result_entry.grid(row=4, column=1)

tk.Label(root, text="Location:").grid(row=5, column=0)
location_entry = tk.Entry(root)
location_entry.grid(row=5, column=1)

# Save button
save_button = tk.Button(root, text="Save", command=save_job_application)
save_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
