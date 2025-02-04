import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the cleaned dataset
csv_file_path = "C:\\Users\\abhan\\Downloads\\kaggle_data\\cleaned_naukri_data_science_jobs_india.csv"
df = pd.read_csv(csv_file_path)

# Strip extra spaces from column names to avoid KeyErrors
df.columns = df.columns.str.strip()

# Print cleaned column names to confirm
st.write("Cleaned Column Names:", df.columns)

# Visualize top companies hiring for Data Science roles
top_companies = df['Company'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_companies.index, y=top_companies.values, hue=top_companies.index, palette='Set3', legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Companies Hiring for Data Science Roles')
plt.tight_layout()
st.pyplot()  # For Streamlit

# Visualize the locations of the jobs
top_locations = df['Location'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.index, y=top_locations.values, hue=top_locations.index, palette='Set2', legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Job Locations')
plt.tight_layout()
st.pyplot()  # For Streamlit
