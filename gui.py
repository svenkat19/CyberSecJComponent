import tkinter as tk
import mysql.connector
import random

def cast_vote(candidate):
    # Randomly determine if Eve intercepts the vote
    intercepted = random.choice([True, False])

    if intercepted:
        status_label.config(text="Vote Invalid (Eve Intercepted)", fg="red")
        valid = False
    else:
        status_label.config(text="Vote Cast Successfully", fg="green")
        valid = True

    # Insert vote into the database
    insert_vote(candidate, valid)

def insert_vote(candidate, valid):
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="voter"
)
    cursor = db.cursor()

    cursor.execute("INSERT INTO votes (candidate, valid) VALUES (%s, %s)", (candidate, valid))
    db.commit()
    db.close()

# Create the GUI
root = tk.Tk()
root.title("Voting System")

candidate_list = ["Candidate 1", "Candidate 2", "Candidate 3"]

for i, candidate in enumerate(candidate_list):
    tk.Button(root, text=candidate, command=lambda c=candidate: cast_vote(c)).grid(row=i, column=0)

status_label = tk.Label(root, text="", fg="black")
status_label.grid(row=len(candidate_list), column=0)

root.mainloop()
