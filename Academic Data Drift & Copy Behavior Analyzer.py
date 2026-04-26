import random
import numpy as np
import pandas as pd
import math
import copy

def generate_data(n):
    data = []
    for i in range(1, n+1):
        student = {
            "id": i,
            "marks": random.randint(40, 100),
            "attendance": random.randint(50, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data, roll_digit):
    mod_value = roll_digit % 3
    if mod_value == 0:
        mod_value = 1

    for i in range(len(data)):
        if i % mod_value == 0:

            data[i]["marks"] = data[i]["marks"] + math.sqrt(data[i]["marks"])
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 5

def analyze_data(data):
    df = pd.DataFrame(data)

    marks = df["marks"]
    mean = np.mean(marks)
    median = np.median(marks)
    std_dev = np.std(marks)
    manual_mean = sum(marks) / len(marks)
    df["normalized"] = (marks - min(marks)) / (max(marks) - min(marks))

    return df, mean, median, std_dev, manual_mean

def detect_drift(original, modified):
    original_mean = np.mean([x["marks"] for x in original])
    modified_mean = np.mean([x["marks"] for x in modified])

    drift = abs(original_mean - modified_mean)

    return drift

roll_number = input("Enter your roll number: ")
last_digit = int(roll_number[-1])


data = generate_data(10)
original_backup = copy.deepcopy(data)
shallow_copy = data.copy()
deep_copy = copy.deepcopy(data)
mutate_data(shallow_copy, last_digit)
mutate_data(deep_copy, last_digit)
df_original, mean_o, median_o, std_o, manual_mean = analyze_data(data)
df_deep, mean_d, median_d, std_d, _ = analyze_data(deep_copy)
drift = detect_drift(original_backup, deep_copy)

unique_marks = set([x["marks"] for x in data])
threshold = 5

if any(original_backup[i] != data[i] for i in range(len(data))):
    result = "Copy Failure Detected"
elif drift > threshold:
    result = "Critical Drift"
elif drift > 2:
    result = "Minor Drift"
else:
    result = "Stable Data"
print("\nOriginal DataFrame")
print(df_original)

print("\nShallow Copy Data")
print(pd.DataFrame(shallow_copy))

print("\nDeep Copy Data")
print(df_deep)

print("\nUnique Marks (Set):", unique_marks)

print("\nDrift Value:", drift)

print("\nTuple Output:", (mean_d, drift, std_d))

print("\nFinal Classification:", result)

print("\nExplanation")
print("Shallow copy caused drift because it shares references with original data.")
print("When nested data (scores list) was modified, original data also changed.")
print("Deep copy created a fully independent structure, so original data remained unchanged.")