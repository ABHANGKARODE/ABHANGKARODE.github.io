import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the cleaned dataset
csv_file_path = "C:\\Users\\abhan\\Downloads\\kaggle_data\\cleaned_naukri_data_science_jobs_india.csv"
df = pd.read_csv(csv_file_path)

# Streamlit page configuration
st.title("Job Role Insights in Data Science Jobs")

# Display cleaned data
st.subheader("Cleaned Data Preview")
st.write(df.head())



# Visualizing top companies
st.subheader("Top Companies Hiring for Data Science Roles")
top_companies = df['Company'].value_counts().nlargest(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_companies.index, y=top_companies.values, palette='Set3')
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# Visualizing job locations
st.subheader("Job Locations Distribution")
top_locations = df['Location'].value_counts().nlargest(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_locations.index, y=top_locations.values, palette='Set1')
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)


# Footer message
st.markdown("### Data Source: Naukri Data Science Jobs (India)")

#streamlit run streamlit_app.py
