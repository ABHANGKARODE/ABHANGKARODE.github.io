import pandas as pd

# Load the dataset
csv_file_path = "C:\\Users\\abhan\\Downloads\\kaggle_data\\naukri_data_science_jobs_india.csv"
df = pd.read_csv(csv_file_path)

# 1. Show the initial data to understand the structure
print("Initial Data:")
print(df.head())

# 2. Remove any unnecessary columns (use the actual column names)
# Example: Dropping 'Job Experience' and 'Skills/Description' columns
df.drop(columns=['Job Experience', 'Skills/Description'], inplace=True)

# 3. Handle missing data (fill with a default value or drop rows)
# Example: Fill missing 'Location' values with 'Unknown'
df['Location'].fillna('Unknown', inplace=True)

# Example: Drop rows with missing values in any column
df.dropna(inplace=True)

# 4. Standardize the data (e.g., make all text lowercase, strip extra spaces)
df['Job_Role'] = df['Job_Role'].str.lower().str.strip()  # Convert 'Job_Role' column text to lowercase and remove extra spaces
df['Company'] = df['Company'].str.strip()  # Strip extra spaces in 'Company'

# 5. Remove duplicates
df.drop_duplicates(inplace=True)

# 6. Check and handle specific issues (e.g., fix incorrect data formats)
# Example: Ensure 'Location' is properly formatted (capitalize first letter of each word)
df['Location'] = df['Location'].apply(lambda x: x.title() if isinstance(x, str) else x)

# 7. Save the cleaned data into a new CSV file
cleaned_csv_file_path = "C:\\Users\\abhan\\Downloads\\kaggle_data\\cleaned_naukri_data_science_jobs_india.csv"
df.to_csv(cleaned_csv_file_path, index=False)

print(f"Cleaned data saved to: {cleaned_csv_file_path}")

print("Cleaned Data:")
print(df.head())
