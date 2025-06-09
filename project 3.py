number = int(input("Enter any number here:"))

count = 0
while number>0:
    number//= 10
    count+=1
print("The number of digits in the entry is", count)