# Minor-project-
“AI-powered QA Test Case Generator: Automatically converts software requirements into structured, prioritized test cases using LLMs for faster, consistent, and smarter testing.”

**AI-Powered Risk-Based Test Case Prioritization**

**Overview**
This project implements an AI-driven system to automatically prioritize test cases based on their risk impact. It helps QA teams focus on high-risk modules first, reducing the chance of production failures and improving software quality.

**Key Features**

--Detects critical modules like authentication, payment, security-sensitive flows, financial calculations, and data deletion features.

--Assigns risk scores to each module or feature automatically.

--Prioritizes test cases based on risk level: High, Medium, Low.

--Suggests an optimized regression suite for faster testing cycles.

--Reduces manual effort and human error in test planning.

| Module / Feature           | Risk Score | Priority   |
|----------------------------|:---------:|-----------|
| Payment Gateway            | High      | Test First |
| Profile Picture Upload     | Medium    | Test Next  |
| Theme Color Change         | Low       | Test Later |

**Existing tools**
Tester manually marks:

1.High (red colour-code)

2.Medium (orange colour-code)

3.Low (green colour-code)

**The Ai we built**

Detects:

Authentication modules

Payment modules

Security-sensitive flows

Financial calculations

Data deletion features

Then:

Assigns risk score

Automatically prioritizes test cases

Suggests regression suite

Example:

Payment gateway High risk

Profile picture upload Medium risk

Theme color change Low risk

-Reduces production failure risk.


**Tech stack used**

"Risk keyword model"

"Classification model"

"LLM-based risk scoring

"Python backend"

"Priority scoring algorithm"


# AI-Powered QA Test Case Generation Agent

This project implements a Risk-Based Prioritization system for QA testing using Python.

## Features

- Requirement risk detection
- Risk score adjustment for sensitive modules
- Automatic test prioritization
- CSV export of prioritized test cases
- Interactive Streamlit UI

## Technologies Used

- Python
- Pandas
- Streamlit
- Machine Learning concepts

## Project Structure

Minor-project-
│
├── src
│   ├── app.py
│   ├── classification.py
│   ├── priority.py
│   ├── risk_keywords.py
│   └── ui.py
│
├── output
│   └── prioritized_tests.csv
│
├── requirements.txt
└── README.md

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run src/ui.py


