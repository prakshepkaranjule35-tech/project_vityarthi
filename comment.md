## Problem Statement

Create a program called "Student Result Calculator" that:

1. Prompts the user to enter marks obtained in 5 subjects.
2. Calculates the total marks and percentage (average) of the student.
3. Assigns a grade based on the following criteria:
   - 90 or above: **A+**
   - 80 to 89: **A**
   - 70 to 79: **B+**
   - 60 to 69: **B**
   - 50 to 59: **C**
   - Below 50: **Fail**
4. Checks if the student has failed in any subject (less than 35 marks in a subject results in FAIL status).
5. Displays the total marks, percentage, grade, and overall status (PASS/FAIL).

### Input

- Five floating-point numbers, each representing marks in one subject.

### Output

- Total marks (float)
- Percentage (float)
- Grade (string)
- Status (PASS/FAIL based on individual subject marks)

### Constraints

- Marks should be numerical values.
- Minimum passing mark per subject is 35.

### Example

**Input:**
```
Marks in Subject 1: 80
Marks in Subject 2: 92
Marks in Subject 3: 67
Marks in Subject 4: 70
Marks in Subject 5: 50
```

**Output:**
```
----- Final Result -----
Total = 359.0
Percentage = 71.8
Grade = B+
Status = PASS
```
