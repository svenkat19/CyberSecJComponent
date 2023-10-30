import tkinter as tk
from tkinter import font, messagebox
import mysql.connector
import random

def cast_vote(candidate):
    intercepted = random.choice([True, False])

    if intercepted:
        status_label.config(text="Vote Invalid (Eve Intercepted)", fg="red")
        valid = False
        show_eve_error_box()  # Call the error message box
    else:
        status_label.config(text="Vote Cast Successfully", fg="green")
        valid = True

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

def show_eve_error_box():
    messagebox.showerror("Eve Intercepted", "Your vote has been intercepted by Eve. Please try again.")

root = tk.Tk()
root.title("Voting System")

# Customize the GUI styling
root.geometry("400x300")
root.config(bg="lightblue")

title_font = font.Font(family="Helvetica", size=20, weight="bold")
button_font = font.Font(family="Helvetica", size=14)
status_font = font.Font(family="Helvetica", size=12, weight="bold")

title_label = tk.Label(root, text="Vote for Your Favorite Candidate", font=title_font, bg="lightblue")
title_label.pack(pady=20)

candidate_list = ["Candidate 1", "Candidate 2", "Candidate 3"]

for i, candidate in enumerate(candidate_list):
    button = tk.Button(root, text=candidate, command=lambda c=candidate: cast_vote(c), font=button_font, bg="lightgreen")
    button.pack(pady=10)

status_label = tk.Label(root, text="", font=status_font, fg="black", bg="lightblue")
status_label.pack()

root.mainloop()
