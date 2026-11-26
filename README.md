# Project 3 – Examination Result and Grace-Mark Validation System

## Description
The Examination Result and Grace-Mark Validation System is a Python-based project that evaluates student marks in multiple subjects. It checks subject-wise pass criteria, applies grace marks according to the specified assumptions, calculates total marks, and displays the final examination result.

## Objectives
- Accept marks in multiple subjects.
- Check subject-wise pass or fail status.
- Apply grace marks to eligible subjects.
- Calculate total marks.
- Display the final examination result.

## Concepts Used
- Variables and Data Types
- Lists
- For Loops
- Conditional Statements (if, elif, else)
- Arithmetic Operators
- User Input

## Grace-Mark Assumptions
- Total subjects: 5
- Maximum marks per subject: 100
- Minimum pass marks: 35
- Students scoring between 30 and 34 receive grace marks to reach 35.
- Students scoring below 30 are considered failed.
- Grace marks are applied independently to each eligible subject in this project.

*Note: These are sample project assumptions, not an official examination policy.*

## Sample Output
```text
Enter Student Name: Ravi
Enter marks of 5 subjects:
78 65 32 90 40

Subject 1: 78 - PASS
Subject 2: 65 - PASS
Subject 3: 35 - PASS WITH GRACE
Subject 4: 90 - PASS
Subject 5: 40 - PASS

Total Marks: 308 / 500
Final Result: PASS
```

## How to Run
1. Open the project folder in VS Code.
2. Open the Python source file.
3. Run the program.
4. Enter the student's name.
5. Enter marks for all five subjects.
6. View the subject-wise results and final result.

## Conclusion
This project demonstrates how Python can be used to evaluate examination results, apply grace marks, and determine student performance. It helps understand lists, loops, conditional statements, and arithmetic operations.
