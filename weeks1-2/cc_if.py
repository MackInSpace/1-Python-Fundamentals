"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michelle  |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
gradeToTest = 100
if gradeToTest == 100:
    print("A+")
elif gradeToTest >= 90:
    print("A")
elif gradeToTest >= 80:
    print("B")
elif gradeToTest >= 70:
    print("C")
elif gradeToTest >= 60:
    print("D")
else:
    print("F")