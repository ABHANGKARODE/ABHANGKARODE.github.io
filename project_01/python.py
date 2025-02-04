import psycopg2
import pandas as pd
import kaggle

# PostgreSQL Connection
conn = psycopg2.connect(
    dbname="job_db",
    user="postgres",  # Default username
    password="Abhangk10@",  # Your PostgreSQL password
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Create jobs table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT
);
""")
conn.commit()

# Step 1: Download dataset from Kaggle using Kaggle API
# Authenticate using Kaggle API key
kaggle.api.authenticate()

# Download the dataset from Kaggle (provide the correct dataset path)
dataset_name = 'kaggle_data/naukri_data_science_jobs_india'  # Update with your dataset path
kaggle.api.dataset_download_files(dataset_name, path='C:\\Users\\abhan\\Downloads\\kaggle_data', unzip=True)

# Step 2: Load dataset from Kaggle CSV
csv_file_path = "C:\\Users\\abhan\\Downloads\\kaggle_data\\naukri_data_science_jobs_india.csv"
df = pd.read_csv(csv_file_path)

# Insert data into PostgreSQL from Kaggle CSV
for _, row in df.iterrows():
    try:
        # Update column names according to your CSV
        title = row['Job_Role']  # Column name from the CSV
        company = row['Company']  # Column name from the CSV
        location = row['Location']  # Column name from the CSV
        
        # Insert data into jobs table
        cursor.execute(
            "INSERT INTO jobs (title, company, location) VALUES (%s, %s, %s)",
            (title, company, location)
        )
        conn.commit()

    except Exception as e:
        print("Error inserting job from CSV:", e)

print("Data from Kaggle CSV inserted into PostgreSQL.")

# Close database connection
cursor.close()
conn.close()

# Explanation why scraping might not work from Naukri.com:
# 1. **Dynamic Content Loading**: Naukri.com loads job data dynamically using JavaScript, which means that simply sending a GET request does not load the data.
# 2. **Selectors may change**: The CSS selectors used in this code might not be correct or could change if Naukri updates their website layout. This can break the scraper.
# 3. **Anti-Bot Mechanisms**: Naukri.com might implement anti-bot measures like CAPTCHA or IP blocking, making scraping difficult.
# 4. **Legal Issues**: Scraping Naukri.com may violate its terms of service. Always ensure that you are complying with a website's terms before scraping.
