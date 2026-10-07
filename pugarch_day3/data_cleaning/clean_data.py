import pandas as pd
import os

# -----------------------------
# 1. Load Dataset
# -----------------------------

input_file = "dataset/facility_data.csv"

df = pd.read_csv(input_file)

print("=" * 60)
print("FACILITY DATA CLEANING")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())


# -----------------------------
# 2. Check Missing Values
# -----------------------------

print("\nMissing Values:")
print(df.isnull().sum())


# -----------------------------
# 3. Check Duplicate Rows
# -----------------------------

duplicate_rows = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_rows)


# -----------------------------
# 4. Check Duplicate Facility IDs
# -----------------------------

duplicate_ids = df["facility_id"].duplicated().sum()

print("Duplicate Facility IDs:", duplicate_ids)


# -----------------------------
# 5. Check Invalid Values
# -----------------------------

print("\nInvalid Cleanliness Scores:")

invalid_cleanliness = df[
    (df["cleanliness_score"] < 1) |
    (df["cleanliness_score"] > 10)
]

print(invalid_cleanliness)


print("\nInvalid Odor Scores:")

invalid_odor = df[
    (df["odor_score"] < 1) |
    (df["odor_score"] > 10)
]

print(invalid_odor)


print("\nInvalid Footfall:")

invalid_footfall = df[df["footfall"] < 0]

print(invalid_footfall)


print("\nInvalid Complaints:")

invalid_complaints = df[df["complaints"] < 0]

print(invalid_complaints)


# -----------------------------
# 6. Convert Inspection Date
# -----------------------------

df["inspection_date"] = pd.to_datetime(
    df["inspection_date"],
    errors="coerce"
)

print("\nInvalid Inspection Dates:")
print(df["inspection_date"].isnull().sum())


# -----------------------------
# 7. Check Categorical Values
# -----------------------------

print("\nWater Availability Values:")
print(df["water_availability"].value_counts(dropna=False))


# -----------------------------
# 8. Remove Duplicate Rows
# -----------------------------

df = df.drop_duplicates()


# -----------------------------
# 9. Handle Missing Values
# -----------------------------

numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )


df["location"] = df["location"].fillna("Unknown")

df["water_availability"] = df[
    "water_availability"
].fillna("Unknown")


# -----------------------------
# 10. Save Cleaned Dataset
# -----------------------------

output_file = "dataset/cleaned_facility_data.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nCleaned dataset saved successfully!")
print(output_file)

print("\nFinal Dataset Shape:")
print(df.shape)