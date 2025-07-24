import matplotlib
matplotlib.use('TkAgg')  # Ensures GUI backend for plot windows

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load Datasets
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

# --------------------------------------------
# 1. Bar Plot: Average total bill by day
plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='total_bill', data=tips, estimator='mean', palette='viridis')
plt.title("Average Total Bill by Day")
plt.xlabel("Day of Week")
plt.ylabel("Average Total Bill")
plt.grid(True, linestyle='--', alpha=0.3)
plt.show(block=True)

# Insight
print("Bar Plot Insight:")
print("Saturday and Sunday have higher average total bills, indicating more dining on weekends.\n")

# --------------------------------------------
# 2. Scatter Plot: Total bill vs Tip
plt.figure(figsize=(8, 5))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex', style='smoker')
plt.title("Total Bill vs Tip by Gender and Smoking Status")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.grid(True, linestyle='--', alpha=0.3)
plt.show(block=True)

# Insight
print("Scatter Plot Insight:")
print("Higher total bills generally lead to higher tips. Smokers and non-smokers show slightly different tipping patterns.\n")

# --------------------------------------------
# 3. Histogram: Distribution of Total Bill
plt.figure(figsize=(8, 5))
plt.hist(tips['total_bill'], bins=20, color='coral', edgecolor='black')
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill Amount")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.3)
plt.show(block=True)

# Insight
print("Histogram Insight:")
print("Most total bills fall between $10 and $20, suggesting mid-range spending.\n")

# --------------------------------------------
# 4. Pie Chart: Gender Distribution
gender_counts = tips['sex'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen'])
plt.title("Gender Distribution")
plt.axis('equal')  # Equal aspect ratio
plt.show(block=True)

# Insight
print("Pie Chart Insight:")
print("Slightly more male customers than female in the dataset.\n")

# --------------------------------------------
# 5. Heatmap: Flight Passenger Numbers (Pivot Table)
flight_pivot = flights.pivot("month", "year", "passengers")
plt.figure(figsize=(12, 6))
sns.heatmap(flight_pivot, cmap='YlGnBu', annot=True, fmt='d', linewidths=.5)
plt.title("Monthly Flight Passengers Over Years")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show(block=True)

# Insight
print("Heatmap Insight:")
print("Passenger numbers increase year over year, with peak travel in summer months like July and August.\n")
