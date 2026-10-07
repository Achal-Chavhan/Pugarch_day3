# Pugarch_day3

# Facility Data Analysis — Day 03

## Project Overview

This project analyzes a facility dataset containing information about facility locations, cleanliness, odor, waste levels, water availability, footfall, complaints and inspection dates.

The main objective is to identify data-quality issues, clean the dataset, detect outliers, calculate important statistics, discover useful patterns and create meaningful visualizations.



## Dataset Fields

The dataset contains the following fields:

* `facility_id` — Unique identifier for each facility
* `location` — Location of the facility
* `cleanliness_score` — Cleanliness rating
* `odor_score` — Odor-related rating
* `waste_level` — Waste level recorded during inspection
* `water_availability` — Availability of water
* `footfall` — Number of people using the facility
* `complaints` — Number of complaints recorded
* `inspection_date` — Date of facility inspection

---

## Project Structure

```text
day-03-facility-analysis/
│
├── dataset/
│   ├── facility_data.csv
│   └── cleaned_facility_data.csv
│
├── data-cleaning/
│   └── clean_data.py
│
├── analysis/
│   └── facility_analysis.py
│
├── visualizations/
│   ├── cleanliness_by_location.png
│   ├── complaints_by_location.png
│   ├── footfall_distribution.png
│   ├── footfall_vs_complaints.png
│   └── correlation_heatmap.png
│
└── README.md
```

---

## Data Cleaning

The dataset was checked for:

* Missing values
* Duplicate records
* Duplicate facility IDs
* Invalid cleanliness scores
* Invalid odor scores
* Invalid waste values
* Negative footfall values
* Negative complaint values
* Invalid inspection dates
* Inconsistent categorical values

### Cleaning operations

The following operations were performed:

1. Loaded the original CSV dataset.
2. Checked dataset dimensions and data types.
3. Identified missing values.
4. Identified duplicate rows.
5. Checked duplicate facility IDs.
6. Checked numerical values for invalid ranges.
7. Converted `inspection_date` to a proper datetime format.
8. Removed duplicate rows.
9. Filled missing numerical values using the median.
10. Filled missing categorical values with `Unknown`.
11. Saved the cleaned dataset as `cleaned_facility_data.csv`.

---

## Outlier Detection

The Interquartile Range (IQR) method was used to identify outliers.

```text
IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Outliers were checked for:

* Cleanliness score
* Odor score
* Waste level
* Footfall
* Complaints

Outliers were investigated rather than automatically removed because an extreme value may represent a genuine facility condition.

---

## Statistical Analysis

The following statistics were calculated:

* Count
* Mean
* Median
* Standard deviation
* Minimum
* Maximum
* Quartiles

Location-wise averages were also calculated for cleanliness, odor, waste, footfall and complaints.

---

## Visualizations

Five visualizations were created.

### 1. Average Cleanliness by Location

A bar chart comparing the average cleanliness score across different locations.

### 2. Average Complaints by Location

A bar chart showing the average number of complaints for each location.

### 3. Footfall Distribution

A histogram showing the distribution of facility footfall.

### 4. Footfall vs Complaints

A scatter plot showing the relationship between facility usage and complaints.

### 5. Correlation Heatmap

A heatmap showing relationships between the numerical facility variables.

---

## Key Insights

The analysis identifies at least three important insights:

1. The location with the highest average complaint level can be identified and prioritized for maintenance improvements.

2. The location with the lowest average cleanliness score can be identified for additional cleaning and inspection.

3. The correlation between footfall and complaints helps determine whether heavily used facilities tend to receive more complaints.

4. The relationship between cleanliness and complaints can help determine whether poor cleanliness is associated with increased complaints.

The exact conclusions should be based on the numerical results generated from the dataset.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## How to Run

### Install dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 1 — Clean the dataset

```bash
python data-cleaning/clean_data.py
```

### Step 2 — Run the analysis

```bash
python analysis/facility_analysis.py
```

The cleaned dataset will be generated in the `dataset` folder and the five visualizations will be saved in the `visualizations` folder.



