# Academic-Data-Drift-Copy-Behavior-Analyzer
## Problem Understanding

This program analyzes student academic data and studies how improper data copying can lead to inconsistencies (data drift). It generates student records, applies mutations using shallow and deep copies, and compares their effects. The system also performs statistical analysis to identify variations and classify data stability.

## Logic Used

The program first generates student data using random values and stores it in a list of dictionaries with nested structures. It then creates both shallow and deep copies of the data.

A mutation function is applied only to the copied data, where:

Marks are increased using a mathematical formula
Attendance is modified
Nested scores are updated

The data is then converted into a Pandas DataFrame for analysis. NumPy is used to calculate mean, median, and standard deviation, while mean is also calculated manually.

Data drift is calculated by comparing the mean of original and modified data. Based on the drift value and conditions, the system classifies the data as Stable, Minor Drift, Critical Drift, or Copy Failure.

## Personalization Applied

The program uses the roll number to control mutation logic.

Last digit of Register Number is taken as input
Mutation is applied only on indexes divisible by (last digit % 3)

This ensures each user gets a unique modification pattern and output.

## Features
Uses list of dictionaries with nested structure
Implements shallow copy and deep copy
Applies mathematical transformation using math
Uses Pandas for tabular analysis
Uses NumPy for statistical calculations
Detects data drift
Includes manual calculation (mean)
Uses set to store unique values
Provides final classification of system behavior

## Learning Outcome

This project helped in understanding how shallow and deep copy affect data structures. It also improved knowledge of data analysis using Pandas and NumPy. Additionally, it strengthened problem-solving skills using Python concepts like lists, dictionaries, functions, and conditions.
