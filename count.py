import tkinter as tk
from tkinter import font, messagebox
import mysql.connector

def get_vote_counts():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="voter"
    )
    cursor = db.cursor()

    cursor.execute("SELECT candidate, SUM(valid) FROM votes GROUP BY candidate")
    results = cursor.fetchall()

    db.close()

    return results

def display_vote_counts():
    vote_counts = get_vote_counts()
    
    result_label.config(state="normal")
    result_label.delete(1.0, tk.END)  # Clear previous content
    result_label.insert(tk.END, "Vote Counts\n\n")
    
    result_font = font.Font(family="Helvetica", size=14, weight="bold")
    
    for candidate, count in vote_counts:
        result_label.insert(tk.END, f"{candidate}: {count} votes\n")
    
    winner = max(vote_counts, key=lambda x: x[1])
    if winner[0] == "EveIntercepted":
        result_label.insert(tk.END, "\nElection Rigged - Please reconduct it.", "error")
    else:
        result_label.insert(tk.END, f"\nThe winner is {winner[0]} with {winner[1]} votes!", "winner")

    result_label.config(state="disabled")

root = tk.Tk()
root.title("Voting System")

# Customize the GUI styling
root.geometry("400x400")
root.config(bg="lightblue")

title_font = font.Font(family="Helvetica", size=20, weight="bold")

title_label = tk.Label(root, text="Vote Counts", font=title_font, bg="lightblue")
title_label.pack(pady=20)

show_counts_button = tk.Button(root, text="Show Vote Counts", command=display_vote_counts)
show_counts_button.pack(pady=10)

result_label = tk.Text(root, height=10, width=40, wrap=tk.WORD)
result_label.config(state="disabled")
result_label.tag_configure("error", foreground="red")
result_label.tag_configure("winner", foreground="green")
result_label.pack()

root.mainloop()
