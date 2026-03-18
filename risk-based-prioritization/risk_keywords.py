# risk_keyword1.py

# 1️ Define risky keywords
risk_keywords = {
    "payment": 5,
    "authentication": 4,
    "delete": 4,
    "financial": 5,
    "security": 5,
    "upload": 2,
    "theme": 1
}

# 2️ Function to calculate risk score (Risk Scoring Algorithm)
def calculate_keyword_risk(text):
    score = 0
    for word, weight in risk_keywords.items():
        if word.lower() in text.lower():
            score += weight
    return score

# 3️ Test block – THIS MUST EXIST
if __name__ == "__main__":
    test_modules = [
         "Payment gateway requires authentication",      # High risk
    "Profile picture upload",                        # Medium/Low risk
    "Delete user account feature",                   # High risk
    "Financial calculations for billing",           # High risk
    "Theme color change",                            # Low risk
    "Security-sensitive password reset",            # High risk
    "Upload profile document",                       # Medium risk
    "Change account email",                          # Medium risk
    "Update theme and layout",                       # Low risk
    "Calculate user discounts and financial reports" # High risk
    ]

    for module in test_modules:
        score = calculate_keyword_risk(module)
        print(f"Module: '{module}' → Risk Score: {score}")