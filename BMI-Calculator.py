print("Adult BMI Calculator.")

age = int(input("Enter your age: "))
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilogram: "))


def calculate_adultbmi(weight, height):
  # Conversion from height in centimeters to meters
  height_m = height / 100

  # Calculating BMI using the formula
  bmi = weight / (height_m**2)
  return bmi

  print("BMI:", bmi)

  if age >= 20:

    def suggest_meals(bmi):
      if bmi < 18.5:
        suggestion = "You are underweight. You may consider meals rich in protein and healthy fats. Examples include eggs, lean meats, fish, nuts, and avocados."
      elif bmi >= 18.5 and bmi < 24.9:
        suggestion = "Your weight is normal. Maintain a balanced diet with a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats."
      elif bmi >= 24.9 and bmi < 29.9:
        suggestion = "You are overweight. Focus on portion control and incorporate more fruits, vegetables, whole grains, lean proteins, and low-fat dairy into your meals."
      else:
        suggestion = "You are in the obese range. It is advisable to consult a healthcare professional or nutritionist for a personalized meal plan."

      return suggestion

    meal_suggestion = suggest_meals(bmi)
    print("Meal suggestion:", meal_suggestion)
