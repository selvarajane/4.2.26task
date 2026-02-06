"""
Python Programming Exercises - 50 Tasks
Complete solutions for all 50 exercises
"""

# ============================================================================
# TASK 1: Get user name and age as input and print them
# ============================================================================
def task1():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Name: {name}, Age: {age}")

# ============================================================================
# TASK 2: Input two numbers and print their sum
# ============================================================================
def task2():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Sum: {num1 + num2}")

# ============================================================================
# TASK 3: Convert an integer to a float
# ============================================================================
def task3():
    num = int(input("Enter an integer: "))
    float_num = float(num)
    print(f"Integer: {num}, Float: {float_num}")

# ============================================================================
# TASK 4: Concatenate a string and a number using type casting
# ============================================================================
def task4():
    text = input("Enter a string: ")
    num = int(input("Enter a number: "))
    result = text + str(num)
    print(f"Concatenated result: {result}")

# ============================================================================
# TASK 5: Store different datatypes and print their types using type()
# ============================================================================
def task5():
    integer_var = 10
    float_var = 3.14
    string_var = "Hello"
    bool_var = True
    list_var = [1, 2, 3]
    
    print(f"Type of {integer_var}: {type(integer_var)}")
    print(f"Type of {float_var}: {type(float_var)}")
    print(f"Type of {string_var}: {type(string_var)}")
    print(f"Type of {bool_var}: {type(bool_var)}")
    print(f"Type of {list_var}: {type(list_var)}")

# ============================================================================
# TASK 6: Input two numbers and display addition, subtraction, multiplication, and division
# ============================================================================
def task6():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"Addition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    if num2 != 0:
        print(f"Division: {num1 / num2}")
    else:
        print("Division: Cannot divide by zero")

# ============================================================================
# TASK 7: Check whether a given number is even or odd
# ============================================================================
def task7():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# ============================================================================
# TASK 8: Find the larger of two numbers using the ternary operator
# ============================================================================
def task8():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    larger = num1 if num1 > num2 else num2
    print(f"Larger number: {larger}")

# ============================================================================
# TASK 9: Check if a number is divisible by both 3 and 5
# ============================================================================
def task9():
    num = int(input("Enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by both 3 and 5")
    else:
        print(f"{num} is not divisible by both 3 and 5")

# ============================================================================
# TASK 10: Demonstrate increment and decrement operations
# ============================================================================
def task10():
    num = int(input("Enter a number: "))
    print(f"Original number: {num}")
    num += 1  # Increment
    print(f"After increment: {num}")
    num -= 1  # Decrement
    print(f"After decrement: {num}")

# ============================================================================
# TASK 11: Input marks and print pass or fail
# ============================================================================
def task11():
    marks = float(input("Enter marks: "))
    if marks >= 40:  # Assuming passing marks is 40
        print("Pass")
    else:
        print("Fail")

# ============================================================================
# TASK 12: Input age and check voting eligibility
# ============================================================================
def task12():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

# ============================================================================
# TASK 13: Input temperature and print hot / normal / cold
# ============================================================================
def task13():
    temp = float(input("Enter temperature: "))
    if temp > 30:
        print("Hot")
    elif temp >= 20:
        print("Normal")
    else:
        print("Cold")

# ============================================================================
# TASK 14: Check whether a number is positive, negative, or zero
# ============================================================================
def task14():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# ============================================================================
# TASK 15: Create a simple calculator using if-elif
# ============================================================================
def task15():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
            return
    else:
        print("Invalid operator")
        return
    
    print(f"Result: {result}")

# ============================================================================
# TASK 16: Print numbers from 1 to 10 using a loop
# ============================================================================
def task16():
    for i in range(1, 11):
        print(i, end=' ')
    print()

# ============================================================================
# TASK 17: Print numbers from 10 to 1 in reverse order
# ============================================================================
def task17():
    for i in range(10, 0, -1):
        print(i, end=' ')
    print()

# ============================================================================
# TASK 18: Print the multiplication table of a given number
# ============================================================================
def task18():
    num = int(input("Enter a number: "))
    print(f"Multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# ============================================================================
# TASK 19: Calculate the sum of first n natural numbers
# ============================================================================
def task19():
    n = int(input("Enter n: "))
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum of first {n} natural numbers: {total}")

# ============================================================================
# TASK 20: Count how many even numbers are between 1 and 50
# ============================================================================
def task20():
    count = 0
    for i in range(1, 51):
        if i % 2 == 0:
            count += 1
    print(f"Number of even numbers between 1 and 50: {count}")

# ============================================================================
# TASK 21: Find the length of a string
# ============================================================================
def task21():
    text = input("Enter a string: ")
    print(f"Length of string: {len(text)}")

# ============================================================================
# TASK 22: Convert a string to uppercase and lowercase
# ============================================================================
def task22():
    text = input("Enter a string: ")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")

# ============================================================================
# TASK 23: Count the number of vowels in a string
# ============================================================================
def task23():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(f"Number of vowels: {count}")

# ============================================================================
# TASK 24: Check whether a string is a palindrome
# ============================================================================
def task24():
    text = input("Enter a string: ")
    text_lower = text.lower().replace(" ", "")
    if text_lower == text_lower[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

# ============================================================================
# TASK 25: Calculate tax based on salary slabs
# ============================================================================
def task25():
    salary = float(input("Enter salary: "))
    tax = 0
    
    if salary > 1000000:
        tax = (salary - 1000000) * 0.30 + 500000 * 0.20 + 250000 * 0.10
    elif salary > 500000:
        tax = (salary - 500000) * 0.20 + 250000 * 0.10
    elif salary > 250000:
        tax = (salary - 250000) * 0.10
    else:
        tax = 0
    
    print(f"Tax: {tax}")

# ============================================================================
# TASK 26: Create an electricity bill calculator
# ============================================================================
def task26():
    units = float(input("Enter electricity units consumed: "))
    bill = 0
    
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15
    
    print(f"Electricity bill: ₹{bill}")

# ============================================================================
# TASK 27: Check whether a year is a leap year
# ============================================================================
def task27():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# ============================================================================
# TASK 28: Find the largest of three numbers
# ============================================================================
def task28():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    
    print(f"Largest number: {largest}")

# ============================================================================
# TASK 29: Print grade (A, B, C, Fail) based on marks
# ============================================================================
def task29():
    marks = float(input("Enter marks: "))
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "Fail"
    
    print(f"Grade: {grade}")

# ============================================================================
# TASK 30: Find the factorial of a number using a loop
# ============================================================================
def task30():
    num = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num}: {factorial}")

# ============================================================================
# TASK 31: Print the Fibonacci series
# ============================================================================
def task31():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    print("Fibonacci series:", end=' ')
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# ============================================================================
# TASK 32: Check whether a number is prime
# ============================================================================
def task32():
    num = int(input("Enter a number: "))
    if num < 2:
        print(f"{num} is not prime")
        return
    
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

# ============================================================================
# TASK 33: Print all prime numbers between 1 and 100
# ============================================================================
def task33():
    print("Prime numbers between 1 and 100:")
    for num in range(2, 101):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
    print()

# ============================================================================
# TASK 34: Count the number of digits in a given number
# ============================================================================
def task34():
    num = int(input("Enter a number: "))
    count = 0
    temp = abs(num)
    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp //= 10
    print(f"Number of digits: {count}")

# ============================================================================
# TASK 35: Count the number of words in a sentence
# ============================================================================
def task35():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(f"Number of words: {len(words)}")

# ============================================================================
# TASK 36: Find the frequency of each character in a string
# ============================================================================
def task36():
    text = input("Enter a string: ")
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    print("Character frequency:")
    for char, count in frequency.items():
        print(f"'{char}': {count}")

# ============================================================================
# TASK 37: Remove all spaces from a string
# ============================================================================
def task37():
    text = input("Enter a string: ")
    result = text.replace(" ", "")
    print(f"String without spaces: {result}")

# ============================================================================
# TASK 38: Replace all vowels in a string with *
# ============================================================================
def task38():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += "*"
        else:
            result += char
    print(f"Modified string: {result}")

# ============================================================================
# TASK 39: Find the longest word in a sentence
# ============================================================================
def task39():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    longest_word = max(words, key=len)
    print(f"Longest word: {longest_word}")

# ============================================================================
# TASK 40: Create a function to add two numbers
# ============================================================================
def add_numbers(a, b):
    return a + b

def task40():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"Sum: {result}")

# ============================================================================
# TASK 41: Use a function to calculate factorial
# ============================================================================
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def task41():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"Factorial of {num}: {result}")

# ============================================================================
# TASK 42: Reverse a string using a function
# ============================================================================
def reverse_string(text):
    return text[::-1]

def task42():
    text = input("Enter a string: ")
    reversed_text = reverse_string(text)
    print(f"Reversed string: {reversed_text}")

# ============================================================================
# TASK 43: Create a function to check whether a number is prime
# ============================================================================
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def task43():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")

# ============================================================================
# TASK 44: Create a function to count vowels in a string
# ============================================================================
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def task44():
    text = input("Enter a string: ")
    vowel_count = count_vowels(text)
    print(f"Number of vowels: {vowel_count}")

# ============================================================================
# TASK 45: Create a simple ATM simulation (check balance, deposit, withdraw)
# ============================================================================
balance = 10000  # Initial balance

def task45():
    global balance
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(f"Current balance: ₹{balance}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{balance}")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn ₹{amount}. New balance: ₹{balance}")
            else:
                print("Insufficient balance")
        elif choice == '4':
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice")

# ============================================================================
# TASK 46: Create a login system using username and password validation
# ============================================================================
def task46():
    correct_username = "admin"
    correct_password = "password123"
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

# ============================================================================
# TASK 47: Build a menu-driven calculator using functions
# ============================================================================
def calculator_add(a, b):
    return a + b

def calculator_subtract(a, b):
    return a - b

def calculator_multiply(a, b):
    return a * b

def calculator_divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def task47():
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '5':
            print("Exiting calculator...")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = calculator_add(num1, num2)
            elif choice == '2':
                result = calculator_subtract(num1, num2)
            elif choice == '3':
                result = calculator_multiply(num1, num2)
            elif choice == '4':
                result = calculator_divide(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid choice")

# ============================================================================
# TASK 48: Input student marks and calculate total, average, and grade using functions
# ============================================================================
def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"

def task48():
    num_subjects = int(input("Enter number of subjects: "))
    marks = []
    
    for i in range(num_subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    
    print(f"Total marks: {total}")
    print(f"Average marks: {average:.2f}")
    print(f"Grade: {grade}")

# ============================================================================
# TASK 49: Create a password strength checker (length, digit, special character)
# ============================================================================
def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    has_digit = any(char.isdigit() for char in password)
    if has_digit:
        strength += 1
    else:
        feedback.append("Password should contain at least one digit")
    
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = any(char in special_chars for char in password)
    if has_special:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character")
    
    if strength == 3:
        return "Strong", []
    elif strength == 2:
        return "Medium", feedback
    else:
        return "Weak", feedback

def task49():
    password = input("Enter a password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"  - {item}")

# ============================================================================
# TASK 50: Reverse a string
# ============================================================================
def task50():
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print(f"Reversed string: {reversed_text}")

# ============================================================================
# Main menu to run any task
# ============================================================================
def main():
    print("=" * 70)
    print("Python Programming Exercises - 50 Tasks")
    print("=" * 70)
    print("\nSelect a task to run (1-50) or 0 to exit:")
    
    tasks = {
        1: task1, 2: task2, 3: task3, 4: task4, 5: task5,
        6: task6, 7: task7, 8: task8, 9: task9, 10: task10,
        11: task11, 12: task12, 13: task13, 14: task14, 15: task15,
        16: task16, 17: task17, 18: task18, 19: task19, 20: task20,
        21: task21, 22: task22, 23: task23, 24: task24, 25: task25,
        26: task26, 27: task27, 28: task28, 29: task29, 30: task30,
        31: task31, 32: task32, 33: task33, 34: task34, 35: task35,
        36: task36, 37: task37, 38: task38, 39: task39, 40: task40,
        41: task41, 42: task42, 43: task43, 44: task44, 45: task45,
        46: task46, 47: task47, 48: task48, 49: task49, 50: task50
    }
    
    while True:
        try:
            choice = int(input("\nEnter task number (1-50) or 0 to exit: "))
            if choice == 0:
                print("Exiting...")
                break
            elif choice in tasks:
                print(f"\n{'='*70}")
                print(f"Running Task {choice}")
                print('='*70)
                tasks[choice]()
                print('='*70)
            else:
                print("Invalid choice. Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
