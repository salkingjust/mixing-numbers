# def greetings(name):
#     string = f"hello, {name}"
#     return string
# x = greetings("maryam")
# print(x)

# def greetings(name):
#     print(f"Hello, {name}")
#
# greetings("David Enabs")

# def multiplication (x, y, z):
#     return x * y * z
# result = multiplication(2,4,6)
# print(result)

# def myStudents(*names):
#     print(names[0])
# myStudents("Joseph", "Muhammed", "Maryam", "Saleem")
#
# def add(*numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total
# def name(firstname, Lastname):
#     print(f"Hello {firstname} {Lastname}")
# name(Lastname="Enabs", firstname="David")
#
# def my_function (**kid):
#     print("his last name is " + kid["Lname"])
# my_function(fname = "Tobias", Lname = "Refsnes")
#
# def my_function(**kid):
#     print("his last name is " + kid["first"])
# my_function(first= "Deacon", last = "boozer")

# write a program that have four functions, the functions are to add, subtract, multiply
# and divide multiple numbers. Accept the numbers from the user. Note: Ask the user
# whether they want to + - * / and based on the user response, call the necessary
# function and provide the results using python

def add_numbers(numbers):
    result = sum(numbers)
    return result

def subtract_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
            result /= num
    return result

def main():
    print("Welcome")

    operation = input("Choose an operation (+, -, *, /) or 'q' to quit: ")

    if operation == 'q':
        return
    try:
        num_count = int(input("How many numbers do you want to operate on? "))
        numbers = []
        for i in range(num_count):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    if operation == '+':
        result = add_numbers(numbers)
    elif operation == '-':
        result = subtract_numbers(numbers)
    elif operation == '*':
        result = multiply_numbers(numbers)
    elif operation == '/':
        result = divide_numbers(numbers)

    if result is not None:
        print(f"Result: {result}")
main()

