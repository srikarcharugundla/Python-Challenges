n = int(input("Enter number of students: "))

marks = [0] * n

valid = 0
failed = 0


for i in range(n):

    reg = input("Enter Register Number: ")
    m = int(input("Enter Marks: "))


    if m >= 0 and m <= 100:

        lastdigit = int(reg[-4])

        if lastdigit % 2 == 0:
            m = m + 3
        else:
            m = m + 1

    marks[i] = m


print()

for i in range(n):

    m = marks[i]

    if m < 0 or m > 100:
        print(m, "→ Invalid")

    elif m >= 90:
        print(m, "→ Excellent")
        valid = valid + 1

    elif m >= 75:
        print(m, "→ Very Good")
        valid = valid + 1

    elif m >= 60:
        print(m, "→ Good")
        valid = valid + 1

    elif m >= 40:
        print(m, "→ Average")
        valid = valid + 1

    else:
        print(m, "→ Fail")
        valid = valid + 1
        failed = failed + 1


print("Total Valid Students:", valid)
print("Total Failed Students:", failed)
