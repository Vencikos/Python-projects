
# User input
name = input("Name: ")
gender = input("Gender(M / F): ")
age = input("Age: ")
weight = input("Weight in kg: ")
height = input("Height in cm: ")
print("[1.2] - Sedentary\n[1.375} - Lightly Active\n[1.55] - Moderately Active\n[1.795] - Very Active\n[1.9] - Extremely Active")
activity = input("Activity level: ")
bmi = int(weight) / (int(height) * int(height)) * 10000


def tdee():
  
  # Male and bmi <= 18.5
  if gender == "M" and bmi <= 18.5:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) + 5) * float(activity))
    print(name + "'s BMI is: ")
    print(str(round(bmi, 2)) + " - Underweight")

  # Male and bmi is between 18.5 and 25
  if gender == "M" and bmi > 18.5 and bmi < 25:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) + 5) * float(activity))
    print(name + "'s BMI is: ")
    print(str(round(bmi, 2)) + " - Normal")

  # Male and bmi is between 25 and 30
  if gender == "M" and bmi > 25 and bmi < 30:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) + 5) * float(activity))
    print(name + "'s BMI is: ")
    print(str(round(bmi, 2)) + " - Overweight")

  # Male and bmi > 30
  if gender == "M" and bmi > 30:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) + 5) * float(activity))
    print(name + "'s BMI is: ") 
    print(str(round(bmi, 2)) + " - Obese")

  # Female and bmi <= 18.5
  if gender == "F" and bmi <= 18.5:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) - 161) * float(activity))
    print(name + "'s BMI is: ")
    print(str(round(bmi, 2)) + " - Underweight")

  # Female and bmi is between 18.5 and 25
  if gender == "F" and bmi > 18.5 and bmi < 25:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) - 161) * float(activity))
    print(name + "'s BMI is: ")
    print(str(round(bmi, 2)) + " - Normal")

  # Female and bmi is between 25 and 30
  if gender == "F" and bmi > 25 and bmi < 30:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) - 161) * float(activity))
    print(name + "'s BMI is: ")
    print(str(round(bmi, 2)) + " - Overweight")

  # Female and bmi > 30
  if gender == "F" and bmi > 30:
    print(name + "'s TDEE is: ")
    print((10 * int(weight) + (6.25 * int(height)) - (5 * int(age)) - 161) * float(activity))
    print(name + "'s BMI is: ") 
    print(str(round(bmi, 2)) + " - Obese")

tdee()
