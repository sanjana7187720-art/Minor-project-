# classification.py

# Function to classify risk score into High / Medium / Low
def classify_risk(score):
    
    if score >= 8:
        return "High"
    
    elif score >= 4:
        return "Medium"
    
    elif score >= 1:
        return "Low"
    
    else:
        return "No Risk"


# Test cases to check if the function works
if __name__ == "__main__":
    
    test_scores = [9, 6, 3, 1, 0]

    for score in test_scores:
        risk_level = classify_risk(score)
        print(f"Risk Score: {score} -> Risk Level: {risk_level}")