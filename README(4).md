# Personalized Risk Analyzer 

## Project Overview

This project is a Python-based Risk Classification System developed as part of academic coursework.

The program:
- Accepts multiple numeric scores from the user
- Classifies them into different risk categories
- Applies a personalized filtering rule based on the user's register number

The personalization ensures that each student's output is unique.

---

## Risk Classification Rules

Score Range → Category

0 – 30      → Low Risk  
31 – 60     → Medium Risk  
61 – 100    → High Risk  
Above 100   → Critical Risk  
Below 0     → Ignored  

---

##  Personalization Logic

1. The program extracts the first numeric digit from the register number.
2. It checks whether that digit repeats anywhere else in the register number.
3. If the digit repeats → low Risk scores are removed.
4. If the digit does not repeat →  critical Risk scores are removed.

This makes the program output unique for every user.

---

## Program Features

- Manual string parsing (no split() used)
- No inbuilt () function used
- Fixed-size list implementation
- Input validation included
- Fully personalized filtering logic
- Clean and structured output

---

## How to Run the Program

1. Install Python.
2. Open terminal or command prompt.
3. Navigate to project folder.
4. Run:

python filename.py

5. Enter:
   - Your full register number
   - Scores separated by space

---

##  Example Input

Register Number:
AP24110011543

Scores:
25 45 78 120 -5 60

---
