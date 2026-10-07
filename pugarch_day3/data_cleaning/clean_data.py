import pandas as pd
import os



input_file = "dataset/facility_data.csv"

df = pd.read_csv(input_file)

print("=" * 60)
print("FACILITY DATA CLEANING")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())




print("\nMissing Values:")
print(df.isnull().sum())




duplicate_rows = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_rows)




duplicate_ids = df["facility_id"].duplicated().sum()

print("Duplicate Facility IDs:", duplicate_ids)




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




df["inspection_date"] = pd.to_datetime(
    df["inspection_date"],
    errors="coerce"
)

print("\nInvalid Inspection Dates:")
print(df["inspection_date"].isnull().sum())




print("\nWater Availability Values:")
print(df["water_availability"].value_counts(dropna=False))




df = df.drop_duplicates()




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



output_file = "dataset/cleaned_facility_data.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nCleaned dataset saved successfully!")
print(output_file)

print("\nFinal Dataset Shape:")
print(df.shape)