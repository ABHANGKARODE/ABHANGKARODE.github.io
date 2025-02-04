import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="job_db",
    user="postgres",  # Your PostgreSQL username
    password="Abhangk10@",  # Your PostgreSQL password
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM jobs")

# Fetch all rows
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
