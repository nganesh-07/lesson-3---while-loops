n = int(input("Enter any number here:"))

# initial sum is 0, so need to establish that
sum = 0

# intial value you want to add starts with 1
i = 1

while i<=n:
    sum = sum + i
    i = i+1

print(sum)