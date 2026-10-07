import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os




df = pd.read_csv("dataset/cleaned_facility_data.csv")

print("=" * 60)
print("FACILITY DATA ANALYSIS")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())




numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

print("\nKEY STATISTICS")
print("=" * 60)

print(df[numeric_columns].describe())




print("\nAverage Cleanliness:",
      round(df["cleanliness_score"].mean(), 2))

print("Average Odor Score:",
      round(df["odor_score"].mean(), 2))

print("Average Waste Level:",
      round(df["waste_level"].mean(), 2))

print("Average Footfall:",
      round(df["footfall"].mean(), 2))

print("Average Complaints:",
      round(df["complaints"].mean(), 2))




location_stats = df.groupby("location").agg({
    "cleanliness_score": "mean",
    "odor_score": "mean",
    "waste_level": "mean",
    "footfall": "mean",
    "complaints": "mean"
})

print("\nLOCATION-WISE STATISTICS")
print("=" * 60)

print(location_stats)




def find_outliers(data, column):

    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[
        (data[column] < lower_bound) |
        (data[column] > upper_bound)
    ]

    return outliers


print("\nOUTLIER ANALYSIS")
print("=" * 60)

for column in numeric_columns:

    outliers = find_outliers(df, column)

    print(
        f"{column}: {len(outliers)} outliers"
    )




correlation = df[numeric_columns].corr()

print("\nCORRELATION MATRIX")
print("=" * 60)

print(correlation)




os.makedirs("visualizations", exist_ok=True)




plt.figure(figsize=(10, 6))

cleanliness = df.groupby(
    "location"
)["cleanliness_score"].mean().sort_values()

cleanliness.plot(kind="bar")

plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/cleanliness_by_location.png",
    dpi=300
)

plt.close()




plt.figure(figsize=(10, 6))

complaints = df.groupby(
    "location"
)["complaints"].mean().sort_values()

complaints.plot(kind="bar")

plt.title("Average Complaints by Location")
plt.xlabel("Location")
plt.ylabel("Average Complaints")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visualizations/complaints_by_location.png",
    dpi=300
)

plt.close()




plt.figure(figsize=(10, 6))

plt.hist(
    df["footfall"].dropna(),
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Facility Footfall")
plt.xlabel("Footfall")
plt.ylabel("Number of Facilities")

plt.tight_layout()

plt.savefig(
    "visualizations/footfall_distribution.png",
    dpi=300
)

plt.close()




plt.figure(figsize=(10, 6))

plt.scatter(
    df["footfall"],
    df["complaints"],
    alpha=0.7
)

plt.title("Footfall vs Complaints")
plt.xlabel("Footfall")
plt.ylabel("Complaints")

plt.tight_layout()

plt.savefig(
    "visualizations/footfall_vs_complaints.png",
    dpi=300
)

plt.close()




plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Facility Variables")

plt.tight_layout()

plt.savefig(
    "visualizations/correlation_heatmap.png",
    dpi=300
)

plt.close()




highest_complaints_location = (
    df.groupby("location")["complaints"]
    .mean()
    .idxmax()
)

lowest_cleanliness_location = (
    df.groupby("location")["cleanliness_score"]
    .mean()
    .idxmin()
)

footfall_complaint_correlation = (
    df["footfall"].corr(df["complaints"])
)

cleanliness_complaint_correlation = (
    df["cleanliness_score"].corr(df["complaints"])
)


print("\nKEY INSIGHTS")
print("=" * 60)

print(
    "1. Location with highest average complaints:",
    highest_complaints_location
)

print(
    "2. Location with lowest average cleanliness:",
    lowest_cleanliness_location
)

print(
    "3. Correlation between footfall and complaints:",
    round(footfall_complaint_correlation, 2)
)

print(
    "4. Correlation between cleanliness and complaints:",
    round(cleanliness_complaint_correlation, 2)
)


print("\nAnalysis completed successfully!")