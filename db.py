import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="voter"
)

cursor = db.cursor()

# Create a table for votes
cursor.execute("CREATE TABLE IF NOT EXISTS votes (id INT AUTO_INCREMENT PRIMARY KEY, candidate VARCHAR(255), valid BOOLEAN)")
