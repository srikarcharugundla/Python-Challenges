D = int(input("Enter your first digit of register number: "))
print("first digit is (D):", D)

scores_input = input("Enter your scores separated by space: ")


count = 0
for ch in scores_input:
    if ch == " ":
        count = count + 1
count = count + 1


scores = [0] * count
number = ""
pos = 0

for ch in scores_input:
    if ch != " ":
        number = number + ch
    else:
        scores[pos] = int(number)
        pos = pos + 1
        number = ""

if number != "":
    scores[pos] = int(number)

low_count = 0
medium_count = 0
high_count = 0
critical_count = 0

valid_count = 0
ignored_count = 0

for i in range(len(scores)):
    score = scores[i]

    if score < 0:
        ignored_count = ignored_count + 1

    elif score <= 30:
        valid_count = valid_count + 1
        low_count = low_count + 1

    elif score <= 60:
        valid_count = valid_count + 1
        medium_count = medium_count + 1

    elif score <= 100:
        valid_count = valid_count + 1
        high_count = high_count + 1

    else:
        valid_count = valid_count + 1
        critical_count = critical_count + 1


low_risk = [0] * low_count
medium_risk = [0] * medium_count
high_risk = [0] * high_count
critical_risk = [0] * critical_count


low = medium = high = critical = 0

for i in range(len(scores)):
    score = scores[i]

    if score < 0:
        continue

    elif score <= 30:
        low_risk[low] = score
        low=low + 1

    elif score <= 60:
        medium_risk[medium] = score
        medium=medium + 1

    elif score <= 100:
        high_risk[high] = score
        high = high + 1

    else:
        critical_risk[critical] = score
        critical = critical + 1


print("\nBefore Personalization Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

reg_no = input("Enter your full register number: ")
D = ""

for ch in reg_no:
    if ch >= '0' and ch <= '9':
        D = ch
        break

print("Personalization Digit (D):", D)

count_repeat = 0

for ch in reg_no:
    if ch == D:
        count_repeat = count_repeat + 1

removed_duetopersonalisation = 0

if count_repeat > 1:
    print("\nDigit repeats in register number")
    print("Personalized Rule: Removing Low Risk Scores:",D)
    removed_duetopersonalisation = len(low_risk)
    low_risk = []

else:
    print("\nDigit does NOT repeat in register number:",D)
    print("Personalized Rule is Removing Critical Risk Scores")
    removed_duetopersonalisation = len(critical_risk)
    critical_risk = []



print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nTotal Valid Entries:", valid_count)
print("Ignored Entries:", ignored_count)
print("Removed Due to Personalization:", removed_duetopersonalisation)
