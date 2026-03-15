# src/main.py

from risk_keywords import calculate_keyword_risk
from classification import classify_risk
from priority import priority_score, adjusted_score
import csv
import os

# Input modules/requirements
modules = []

print("Enter software requirements (type 'done' to finish):")

while True:
    module = input("Requirement: ")
    
    if module.lower() == "done":
        break
        
    modules.append(module)

# Output list
results = []

for module in modules:
    score = calculate_keyword_risk(module)
    score = adjusted_score(module, score)
    risk_level = classify_risk(score)
    priority = priority_score(risk_level)
    results.append({
        "Module": module,
        "Risk Score": score,
        "Risk Level": risk_level,
        "Priority": priority
    })

# Print results as a table
print(f"{'Module':40} | {'Score':5} | {'Risk Level':6} | {'Priority':8}")
print("-" * 70)
for r in results:
    print(f"{r['Module']:40} | {r['Risk Score']:5} | {r['Risk Level']:6} | {r['Priority']:8}")

# Save output to CSV
output_folder = "../output"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "prioritized_tests.csv")

with open(output_file, "w", newline="") as csvfile:
    fieldnames = ["Module", "Risk Score", "Risk Level", "Priority"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to {output_file}")