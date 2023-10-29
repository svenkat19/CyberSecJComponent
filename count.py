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

# Display the vote counts
vote_counts = get_vote_counts()
for candidate, count in vote_counts:
    print(f"{candidate}: {count} votes")
