import tkinter as tk
from tkinter import font, messagebox
import mysql.connector
import random

def cast_vote(candidate):
    intercepted = random.choice([True, False])

    if intercepted:
        show_eve_error_box()  # Display the error message box for Eve's interception
    else:
        success_message = f"Vote for {candidate} was cast successfully!"
        show_success_box(success_message)  # Display a success message dialog
    update_vote_count(candidate)  # Increment the valid votes in the database

def update_vote_count(candidate):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="voter"
    )
    cursor = db.cursor()

    # Check if a record for the candidate exists
    cursor.execute("SELECT id FROM votes WHERE candidate = %s", (candidate,))
    result = cursor.fetchone()

    if result:
        # If a record exists, increment the valid column
        cursor.execute("UPDATE votes SET valid = valid + 1 WHERE candidate = %s", (candidate,))
    else:
        # If no record exists, insert a new record with a valid vote
        cursor.execute("INSERT INTO votes (candidate, valid) VALUES (%s, %s)", (candidate, 1))

    db.commit()
    db.close()

def show_eve_error_box():
    messagebox.showerror("Eve Intercepted", "Your vote has been intercepted by Eve. Please try again.")
    update_vote_count("EveIntercepted")  # Increment the valid votes for Eve

def show_success_box(message):
    messagebox.showinfo("Vote Successful", message)

root = tk.Tk()
root.title("Voting System")

# Customize the GUI styling
root.geometry("400x300")
root.config(bg="lightblue")

title_font = font.Font(family="Helvetica", size=20, weight="bold")
button_font = font.Font(family="Helvetica", size=14)
status_font = font.Font(family="Helvetica", size=12, weight="bold")

title_label = tk.Label(root, text="Vote for your Candidate", font=title_font, bg="lightblue")
title_label.pack(pady=20)

candidate_list = ["Candidate 1", "Candidate 2", "Candidate 3"]

for i, candidate in enumerate(candidate_list):
    button = tk.Button(root, text=candidate, command=lambda c=candidate: cast_vote(c), font=button_font, bg="lightgreen")
    button.pack(pady=10)

status_label = tk.Label(root, text="", font=status_font, fg="black", bg="lightblue")
status_label.pack()

root.mainloop()
