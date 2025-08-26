import pandas as pd
import matplotlib.pyplot as plt
import os

# Make visuals folder
# This will be created in the same directory as your analysis.py script.
os.makedirs("visuals", exist_ok=True)

# Load all 5 CSVs from the 'data' subfolder
df_top15 = pd.read_csv("data/01_top15_oldest_companies.csv")
df_country = pd.read_csv("data/02_old_companies_by_country.csv")
df_industry = pd.read_csv("data/03_old_companies_by_industry.csv")
df_oldest_per_country = pd.read_csv("data/04_oldest_per_country.csv")
df_century = pd.read_csv("data/05_companies_by_century.csv")


# --- Chart 1: Countries with most old businesses ---
plt.figure(figsize=(10, 6))
df_country_sorted = df_country.sort_values("old_companies", ascending=False)
plt.bar(df_country_sorted["country"], df_country_sorted["old_companies"])
plt.xticks(rotation=45, ha="right")
plt.title("Countries with Most 200+ Year Old Companies")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("visuals/by_country.png")
plt.close()

# --- Chart 2: Industries with most old businesses ---
plt.figure(figsize=(10, 6))
# Fill missing industry values with 'Unknown' for cleaner plotting
df_industry["industry"] = df_industry["industry"].fillna("Unknown").astype(str)
df_industry_sorted = df_industry.sort_values("total_companies", ascending=False)
plt.bar(df_industry_sorted["industry"], df_industry_sorted["total_companies"])
plt.xticks(rotation=45, ha="right")
plt.title("Industries with Most Old Companies")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("visuals/by_industry.png")
plt.close()

# --- Chart 3: Companies by century ---
plt.figure(figsize=(8, 5))
plt.plot(df_century["century"], df_century["total_companies"], marker="o")
plt.title("Companies Founded by Century")
plt.xlabel("Century")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("visuals/by_century.png")
plt.close()

# --- Chart 4: Top 15 oldest companies ---
plt.figure(figsize=(12, 6))
# Sorting by 'founded_year' in ascending order to find the oldest
df_top15_sorted = df_top15.sort_values("founded_year")
plt.barh(df_top15_sorted["company"], df_top15_sorted["founded_year"])
# Invert y-axis to show the oldest company at the top
plt.gca().invert_yaxis()
plt.title("Top 15 Oldest Companies by Founding Year")
plt.xlabel("Year Founded")
plt.ylabel("Company")
plt.tight_layout()
plt.savefig("visuals/top15_oldest.png")
plt.close()

# --- NEW Chart 5: Oldest company per country (Top 20) ---
plt.figure(figsize=(12, 8))
# Sort by oldest founding year and take the top 20 for readability
df_opc_sorted = df_oldest_per_country.sort_values("founded_year").head(20)
# Create a clear label combining company and country
labels = df_opc_sorted['company'] + ' (' + df_opc_sorted['country'] + ')'
plt.barh(labels, df_opc_sorted['founded_year'])
# Invert y-axis to have the oldest at the top
plt.gca().invert_yaxis()
plt.title('Top 20 Oldest Operating Companies by Country')
plt.xlabel('Year Founded')
plt.tight_layout()
plt.savefig('visuals/oldest_per_country.png')
plt.close()


print("✅ 5 charts saved successfully in the 'visuals' folder.")