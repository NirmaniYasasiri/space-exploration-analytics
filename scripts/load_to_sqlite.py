import pandas as pd
import sqlite3

df = pd.read_csv('data/space_cleaned.csv')

# Create a local SQLite database file
conn = sqlite3.connect('data/space_launches.db')
df.to_sql('space_launches', conn, if_exists='replace', index=False)
conn.close()

print("Database created: data/space_launches.db")