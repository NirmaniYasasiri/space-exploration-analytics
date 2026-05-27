import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Load raw data
df = pd.read_csv('data/Space_Corrected.csv')
print("Raw shape:", df.shape)

# Drop artefact index columns
df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'], inplace=True)

# Rename columns to clean names
df.rename(columns={
    'Company Name'  : 'company',
    'Location'      : 'location',
    'Datum'         : 'datum',
    'Detail'        : 'detail',
    'Status Rocket' : 'rocket_status',
    ' Rocket'       : 'rocket_cost_mUSD',
    'Status Mission': 'mission_status'
}, inplace=True)

# Fix rocket cost column (was stored as text)
df['rocket_cost_mUSD'] = pd.to_numeric(df['rocket_cost_mUSD'], errors='coerce')

# Parse the date column into a proper datetime
df['launch_date'] = pd.to_datetime(
    df['datum'], format='%a %b %d, %Y %H:%M UTC', errors='coerce'
)
mask = df['launch_date'].isna()
df.loc[mask, 'launch_date'] = pd.to_datetime(
    df.loc[mask, 'datum'], format='mixed', errors='coerce'
)

# Create new useful columns
df['year']          = df['launch_date'].dt.year.astype('Int64')
df['month']         = df['launch_date'].dt.month.astype('Int64')
df['decade']        = (df['year'] // 10 * 10).astype('Int64')
df['country']       = df['location'].str.split(',').str[-1].str.strip()
df['launch_site']   = df['location'].str.split(',').str[0].str.strip()
df['rocket_family'] = df['detail'].str.split('|').str[0].str.strip()
df['is_success']    = (df['mission_status'] == 'Success').astype(int)

# Save the cleaned file
df.to_csv('data/space_cleaned.csv', index=False)
print("Cleaned shape:", df.shape)
print("Saved to data/space_cleaned.csv")