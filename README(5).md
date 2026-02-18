## Project Description
This Python program simulates an emergency command center system that analyzes disaster resource requests from different zones and generates a final dispatch plan based on classification rules and a personalized filtering logic (PLI).

The system:

Accepts user input for full name

Calculates Personalized Logic Index (PLI)

Accepts multiple resource requests

Classifies requests into categories

Applies filtering based on PLI

Generates a final dispatch report


## How the Program Works
1. Name Processing

The program takes the user's full name as input.

Spaces are removed manually using a for loop.

The length of the name (excluding spaces) is calculated.

PLI is computed using:

PLI = Length % 3

2. Request Classification Rules

Each resource request is categorized as:

Value Range	Category
< 0	Invalid Request
0	No Demand
1 – 20	Low Demand
21 – 50	Moderate Demand
> 50	High Demand


3. Personalized Filtering Logic (PLI)

Based on:

PLI = Length % 3

The PLI value is treated like a traffic signal control mechanism:

PLI Value | Traffic Signal | Rule Applied
0 | Green | Remove all Low Demand requests
1 | Yellow | Remove all High Demand requests
2 | Red | Keep only Moderate Demand requests

The filtering rule applied is:

PLI Value	Rule Applied
0	Remove all Low Demand requests
1	Remove all High Demand requests
2	Keep only Moderate Demand requests


## Output Report Includes

Length of Name (L)

PLI Value

Total Valid Requests

Number of Requests Removed due to PLI

Invalid Requests List

Final Low Demand List

Final Moderate Demand List

Final High Demand List

## Constraints Followed

The program strictly follows:

Uses lists

Uses for loops

Uses conditional statements

No list comprehension

No dictionaries or sets

No max(), min(), sum()

No sorting functions

No hard-coded output


## How to Run

Run the Python script.

Enter your full name.

Enter number of resource requests.

Enter each request value one by one.

View the final dispatch report.

## Example

Input:

Full Name: Srikar Charugundla
Number of Requests: 7
Values: 10 25 60 -3 0 45 80


Output (Example when PLI = 2):

Moderate Demand: [25, 45]
Low Demand: []
High Demand: []
Invalid Requests: [-3]



