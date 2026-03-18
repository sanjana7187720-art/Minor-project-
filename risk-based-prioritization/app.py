import pandas as pd
from classification import classify_risk
from priority import priority_score, adjusted_score

def run_risk_analysis():

    requirements = [
        {"module": "Authentication", "text": "User login with email and password"},
        {"module": "Profile", "text": "User uploads profile picture"},
        {"module": "UI", "text": "User changes theme color"},
        {"module": "Payment", "text": "User makes payment using credit card"},
        {"module": "Settings", "text": "User updates notification settings"}
    ]

    data = []

    for req in requirements:

        module = req["module"]
        text = req["text"]

        risk = classify_risk(text)

        if risk == "High":
            score = 3
        elif risk == "Medium":
            score = 2
        else:
            score = 1

        final_score = adjusted_score(module, score)

        priority = priority_score(risk)

        data.append({
            "Module": module,
            "Requirement": text,
            "Risk Level": risk,
            "Risk Score": final_score,
            "Priority": priority
        })

    df = pd.DataFrame(data)

    df.to_csv("../output/prioritized_tests.csv", index=False)

    print(df)


if __name__ == "__main__":
    run_risk_analysis()