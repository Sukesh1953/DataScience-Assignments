# Data Science Assignment - Week 2
# Name: Sukesh Padagatti
# Description: Python Data Structures and File Handling
# ============================================


# ============================================
# TASK 1: BASIC OPERATIONS
# ============================================

# Taking two integer inputs from the user
num1 = int(input("Enter first number: "))  # Convert input to integer
num2 = int(input("Enter second number: "))

# Performing arithmetic operations
addition = num1 + num2        # Adding two numbers
subtraction = num1 - num2     # Subtracting second number from first
multiplication = num1 * num2  # Multiplying both numbers

# Handling division carefully to avoid division by zero error
if num2 != 0:
    division = num1 / num2    # Dividing first number by second
    modulus = num1 % num2     # Remainder after division
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined (division by zero)"

exponentiation = num1 ** num2  # num1 raised to the power num2

# Displaying results using f-strings
print("\n--- Task 1 Results ---")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")


##Output##
Enter first number:  5
Enter second number:  4

--- Task 1 Results ---
Addition: 9
Subtraction: 1
Multiplication: 20
Division: 1.25
Modulus: 1
Exponentiation: 625



# ============================================
# TASK 2: LISTS AND NUMPY ARRAYS
# ============================================

# Importing NumPy library for numerical operations
import numpy as np

# Creating a list with at least 10 numbers
numbers = [10, 5, 8, 20, 15, 3, 7, 25, 30, 2]

# Printing length of the list
print("\n--- Task 2 Results ---")
print("Length of list:", len(numbers))

# Finding maximum and minimum values
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

# Adding a new element to the list
numbers.append(50)  # Adds 50 to the end of list

# Removing an element from the list
numbers.remove(3)   # Removes the value 3

# Sorting list in ascending order
numbers.sort()
print("List in ascending order:", numbers)

# Sorting list in descending order
numbers.sort(reverse=True)
print("List in descending order:", numbers)

# Converting list to NumPy array
array_numbers = np.array(numbers)

# Calculating statistical measures
mean_value = np.mean(array_numbers)     # Average value
median_value = np.median(array_numbers) # Middle value
std_deviation = np.std(array_numbers)   # Spread of data

# Printing results
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)


##Output##
--- Task 2 Results ---
Length of list: 10
Maximum value: 30
Minimum value: 2
List in ascending order: [2, 5, 7, 8, 10, 15, 20, 25, 30, 50]
List in descending order: [50, 30, 25, 20, 15, 10, 8, 7, 5, 2]
Mean: 17.2
Median: 12.5
Standard Deviation: 13.905394636614956


# ============================================
# TASK 3: DICTIONARIES AND SETS
# ============================================

print("\n--- Task 3 Results ---")

# Creating a dictionary with student details
student = {
    "name": "Sukesh",
    "age": 22,
    "course": "Data Science",
    "marks": 85
}

# Looping through dictionary and printing key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Adding a new key-value pair
student["grade"] = "A"  # Adding grade

# Printing updated dictionary
print("Updated student dictionary:", student)

# Creating a set (duplicates are automatically removed)
courses = {"Python", "Data Science", "AI", "Python"}
print("Unique courses:", courses)

# Creating two sets for operations
set1 = {"Python", "AI", "ML"}
set2 = {"AI", "Data Science", "DL"}

# Performing set operations
print("Union:", set1.union(set2))             # All unique elements
print("Intersection:", set1.intersection(set2)) # Common elements
print("Difference:", set1.difference(set2))   # Elements in set1 not in set2


##Output##
--- Task 3 Results ---
name: Sukesh
age: 22
course: Data Science
marks: 85
Updated student dictionary: {'name': 'Sukesh', 'age': 22, 'course': 'Data Science', 'marks': 85, 'grade': 'A'}
Unique courses: {'Data Science', 'AI', 'Python'}
Union: {'Data Science', 'DL', 'ML', 'AI', 'Python'}
Intersection: {'AI'}
Difference: {'ML', 'Python'}


# ============================================
# TASK 4: FILE HANDLING
# ============================================

print("\n--- Task 4 Results ---")

# Creating and writing data to a text file
with open("student_data.txt", "w") as file:
    # Writing student data in CSV format: name, course, marks
    file.write("A,Data Science,80\n")
    file.write("B,AI,70\n")
    file.write("C,Python,90\n")
    file.write("D,ML,60\n")
    file.write("E,DL,85\n")

# Reading the file and displaying students with marks > 75
with open("student_data.txt", "r") as file:
    print("Students with marks above 75:")
    
    # Reading file line by line
    for line in file:
        # Removing newline and splitting values
        name, course, marks = line.strip().split(",")
        
        # Converting marks to integer for comparison
        if int(marks) > 75:
            print(f"{name} - {course} - {marks}")


##Output##

--- Task 4 Results ---
Students with marks above 75:
A - Data Science - 80
C - Python - 90
E - DL - 85
