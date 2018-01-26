name = input()
age = int(input())
town = input()
salary = float(input())
print("Name: {}".format(name))
print("Age: {}".format(age))
print("Town: {}".format(town))
print("Salary: ${0:.2f}".format(salary))
if age <= 18:
    print("Age range: teen")
elif age >70:
    print("Age range: elder")
else:
    print("Age range: adult")
if salary <500:
    print("Salary range: low")
elif salary<2500:
    print("Salary range: medium")
else:
    print("Salary range: high")





