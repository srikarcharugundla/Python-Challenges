name_full=input("enter your full name: ")

name_withoutspace = ""

for ch in name_full:
    if ch != " ":
        name_withoutspace = name_withoutspace + ch
length=0
for ch in name_withoutspace:
    length = length + 1


request=[]

n=int(input("enter number of requests: "))

for i in range(n):
    values=int(input("enter the values:"))
    request.append(values)

low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_request=[]

total_valid=0

for r in request:
    if r<0:
        invalid_request.append(r)
    elif r==0:
        pass
    elif 1<=r<=20:
        low_demand.append(r)
        total_valid = total_valid + 1
    elif 21<=r<=50:
        moderate_demand.append(r)
        total_valid = total_valid + 1
    else:
        high_demand.append(r)
        total_valid = total_valid + 1

removed_count=0
PLI = length % 3

if PLI==0:
    for thing in low_demand:
        removed_count = removed_count + 1
    low_demand = []

elif PLI == 1:
    for thing in high_demand:
        removed_count = removed_count + 1
    high_demand = []

elif PLI == 2:
    for thing in low_demand:
        removed_count = removed_count + 1

    for thing in high_demand:
        removed_count = removed_count + 1

    low_demand = []
    high_demand = []

print("\n final lists after filtering:")
print("Length of Name (L):", length)
print("PLI Value:", PLI)
print("Total Valid Requests:", total_valid)
print("Requests Removed Due to PLI:", removed_count)
print("Invalid Requests:", invalid_request)
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)




