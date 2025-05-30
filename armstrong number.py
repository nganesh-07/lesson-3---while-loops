number = int(input("Enter a number here:"))

sum = 0

# use a temporary variable to represent the number entered as there are a lot of operations going on so you need two variables:

temp = number
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if number == sum:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")