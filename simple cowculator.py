# simple cowculator

# This adds 2 digits
def add(x, y):
    return x + y

# This subtracts 2 digits
def subtract(x, y):
    return x - y

# This multiplies 2 digits
def multiply(x, y):
    return x * y

# This divides 2 digits
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input 
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is correct
    if choice in ('1', '2', '3', '4'):
        digitOne = float(input("Enter first number: "))
        digitTwo = float(input("Enter second number: "))

        if choice == '1':
            print('The result of the sum between {} and {} is: '.format(digitOne, digitTwo), add(digitOne, digitTwo))

        elif choice == '2':
            print('The result of the substraction between {} and {} is: '.format(digitOne, digitTwo), subtract(digitOne, digitTwo))

        elif choice == '3':
            print('The result of the multiply between {} and {} is: '.format(digitOne, digitTwo), multiply(digitOne, digitTwo))

        elif choice == '4':
            print('The result of the sum between {} and {} is: '.format(digitOne, digitTwo), divide(digitOne, digitTwo))
        
        # check if user wants another calculation, if not end loop
        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
          break
    
    else:
        print("Invalid Input")