# Smart Transaction Risk Detector

##  Overview

The **Smart Transaction Risk Detector** is a Python-based program that analyzes daily transaction amounts of a user and identifies potential risk patterns. It categorizes transactions, detects suspicious behavior, and generates a final risk classification report.

This project demonstrates how basic programming concepts can be applied to solve real-world problems like **fraud detection in digital payment systems**.

---

##  Features

* Accepts multiple transaction amounts as input
* Classifies transactions into:

  * Normal (1–500)
  * Large (501–2000)
  * High Risk (>2000)
  * Invalid (≤0)
* Stores categorized data using a dictionary
* Detects patterns such as:

  * Frequent transactions
  * Large total spending
  * Suspicious high-risk activity
* Generates:

  * Total transaction value
  * Number of transactions
  * Final risk classification
* Includes a **Custom Risk Score** for enhanced analysis

---

##  Logic & Approach

1. **Input Handling**

   * User enters number of transactions and their values.
   * Data is stored in a list.

2. **Transaction Classification**

   * Each transaction is evaluated using conditional statements.
   * Categorized into different risk levels and stored in a dictionary.

3. **Computation**

   * Total transaction value and valid transaction count are calculated.

4. **Pattern Detection**

   * Frequent Transactions: more than 5 transactions
   * Large Spending: total value greater than 5000
   * Suspicious Activity: 3 or more high-risk transactions

5. **Risk Evaluation**

   * High Risk → if suspicious activity is detected
   * Moderate Risk → if frequent or large spending
   * Low Risk → otherwise

---

##  Custom Risk Score

An additional scoring system is implemented:

* Frequent Transactions → +1
* Large Spending → +2
* Suspicious Activity → +3

This helps provide a **numerical representation of risk level**.

---

##  Technologies Used

* Python
* Core concepts:

  * Lists
  * Loops (`for`)
  * Conditional statements
  * Dictionary
  * Tuple
  * List comprehension

---

##  Output

The program displays:

* Categorized transactions
* Total transaction value
* Number of transactions
* Final risk classification
* Custom risk score
* Summary tuple

---

##  How to Run

1. Run the Python program
2. Enter the number of transactions
3. Input each transaction value
4. View the generated risk report

---

##  Learning Outcomes

* Understanding of real-world problem solving using Python
* Efficient use of data structures like lists and dictionaries
* Implementation of conditional logic for classification
* Introduction to basic risk analysis techniques

---

##  Conclusion

This project simulates a simplified fraud detection system. It highlights how structured programming can help identify risky financial behavior and support decision-making.

---

