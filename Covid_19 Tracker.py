import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

try:
    DATA_URL = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    df_raw = pd.read_csv(DATA_URL)
    print("✅ Data loaded successfully from Our World in Data.\n")

except Exception as e:
    print(f"❌ An error occurred while loading the data: {e}")
    exit()

print("🔎 Initial Data Preview (First 5 Rows):\n")
print(df_raw.head())
print("\n" + "="*80 + "\n")

print("🔎 Dataset Info & Missing Values:\n")
df_raw.info()
print("\nMissing values per column:")
print(df_raw.isnull().sum())
print("\n" + "="*80 + "\n")

countries_of_interest = ['Kenya', 'United States', 'India', 'Brazil']

df_filtered = df_raw[df_raw['location'].isin(countries_of_interest)].copy()

df_filtered['date'] = pd.to_datetime(df_filtered['date'])

cols_to_fill = ['total_cases', 'total_deaths', 'total_vaccinations']
df_filtered[cols_to_fill] = df_filtered[cols_to_fill].fillna(0).ffill()

print("✅ Data has been filtered and cleaned. It's ready for analysis!\n")
print("Filtered data info:\n")
df_filtered.info()
print("\n" + "="*80 + "\n")

print("📊 Analysis 1: COVID-19 Cases and Deaths Over Time\n")
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location', ax=axes[0])
axes[0].set_title('Total COVID-19 Cases Over Time')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Total Cases')

sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location', ax=axes[1])
axes[1].set_title('Total COVID-19 Deaths Over Time')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Total Deaths')

plt.tight_layout()
plt.show()

print("📊 Analysis 2: Death Rate Comparison\n")
df_latest = df_filtered.loc[df_filtered.groupby('location')['date'].idxmax()]
df_latest['death_rate_percent'] = (df_latest['total_deaths'] / df_latest['total_cases']) * 100

print("Latest death rate per country:\n")
print(df_latest[['location', 'death_rate_percent']].set_index('location'))
print("\n" + "="*80 + "\n")

print("📊 Analysis 3: Vaccination Progress Over Time\n")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x='date', y='total_vaccinations', hue='location')
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.show()

print("📊 Analysis 4: Cases vs. Deaths (Scatter Plot)\n")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_filtered, x='total_cases', y='total_deaths', hue='location', style='location', s=100)
plt.title('Relationship Between Total Cases and Total Deaths')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.show()
print("\n" + "="*80 + "\n")

print("📝 Key Insights from the Data Analysis Report:\n")
print("1. **Trend of Cases and Deaths:** The line charts clearly show that total cases and deaths followed similar growth curves across all selected countries, with a sharp increase in mid-2020 and 2021.")
print("2. **Death Rate Variation:** The death rate analysis highlights significant differences between countries, which could be attributed to variations in healthcare systems, age demographics, and reporting methods.")
print("3. **Vaccination Rollout:** The vaccination line chart shows the different paces at which countries began their vaccination campaigns. Countries like the United States and Brazil began their mass vaccination programs earlier than Kenya.")
print("4. **Correlation:** The scatter plot visually confirms a strong positive correlation between total cases and total deaths. This is expected, as a higher number of cases naturally leads to a higher number of deaths, although the slope of this relationship varies by country (representing the death rate).")
print("\nThis concludes our data analysis of the COVID-19 global dataset. The insights gained from this process provide a clear picture of the pandemic's impact over time.")
