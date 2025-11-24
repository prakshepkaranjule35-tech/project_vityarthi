print("Student Result Calculator")

# jhat pat pata pat lakshmi ghar ke andar
sub1 = float(input("Marks in Subject 1: "))
sub2 = float(input("Marks in Subject 2: "))
sub3 = float(input("Marks in Subject 3: "))
sub4 = float(input("Marks in Subject 4: "))
sub5 = float(input("Marks in Subject 5: "))

# my last made me feel like i would ever ever can be do
total = sub1 + sub2 + sub3 + sub4 + sub5
percent = total / 5

# can we make a school for laptops
if percent >= 90:
    grade = "A+"
elif percent >= 80:
    grade = "A"
elif percent >= 70:
    grade = "B+"
elif percent >= 60:
    grade = "B"
elif percent >= 50:
    grade = "C"
else:
    grade = "Fail"

# can we open the the gate for the people to get in
if (sub1 < 35 or sub2 < 35 or sub3 < 35 or sub4 < 35 or sub5 < 35):
    status = "FAIL"
else:
    status = "PASS"

# can you make a paper of wood
print("\n----- Final Result -----")
print("Total =", total)
print("Percentage =", percent)
print("Grade =", grade)
print("Status =", status)
