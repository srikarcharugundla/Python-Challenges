transactions = []

n = int(input("How many transactions? "))

for i in range(n):
    t = int(input(f"Enter transaction {i+1}: "))
    transactions.append(t)

categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}
total_value = 0
valid_count = 0
high_count = 0

for t in transactions:
    if t <= 0:
        categories["invalid"].append(t)
    elif 1 <= t <= 500:
        categories["normal"].append(t)
        total_value += t
        valid_count += 1
    elif 501 <= t <= 2000:
        categories["large"].append(t)
        total_value += t
        valid_count += 1
    else:
        categories["high_risk"].append(t)
        total_value += t
        valid_count += 1
        high_count += 1

num_transactions = len([t for t in transactions])

frequent = num_transactions > 5
large_spending = total_value > 5000

high_risk_count = len(categories["high_risk"])

if high_risk_count >= 3:
    suspicious = True
else:
    suspicious = False

if suspicious:
        risk = "High Risk"
elif large_spending or frequent:
        risk = "Moderate Risk"
else:
        risk = "Low Risk"

risk_score = 0

if frequent:
    risk_score += 1
if large_spending:
    risk_score += 2
if suspicious:
    risk_score += 3

summary = (total_value, valid_count, risk)

for key, value in categories.items():
    print(key, ":", value)

print("Total Transaction Value:", total_value)
print("Number of Transactions:", num_transactions)
print("Final Risk Classification:", risk)
print("Custom Risk Score:", risk_score)
print("\nSummary (Total Value, Number of Transactions):", summary)