marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input("Enter subject marks: "))
    marks.append(m)

final_marks = []

for m in marks:
    if 30 <= m < 35:
        final_marks.append(35)
    else:
        final_marks.append(m)

print("Original Marks:", marks)
print("Final Marks:", final_marks)

if all(m >= 35 for m in final_marks):
    print("Result: PASS")
else:
    print("Result: FAIL")