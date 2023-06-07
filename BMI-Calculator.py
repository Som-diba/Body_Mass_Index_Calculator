def calculate_bmi(weight, height):
  #Conversion fators
  lbs_to_kg = 0.4536
  in_to_m = 0.0254

  #Conversion of weight from pounds to kilogram
  if unit_of_weight == "lbs":
    weight = float(weight) * lbs_to_kg
  else:
    weight = float(weight)

  #Conversion height to meters
  if unit_of_height == "cm":
    height = float(
      height) / 100  # Conversion of height from centimeters to meters

  elif unit_of_height == "ft_in":
    #Spliting of height into feet and inches
    feet, inches = height.split("'")
    height = (float(feet) * 12 + float(inches)
              ) * in_to_m  #Conversion of height from feet_inches to meters
  elif unit_of_height == "m":
    height = float(height)

  #Calculating BMI using the formula
  bmi = weight / (height**2)
  round_bmi = round(bmi, 2)  #rounding number to 2 decimal places
  return round_bmi


def suggest_meals(bmi):
  if bmi < 18.5:
    suggestion = "You are underweight.\nSuggestion: You may consider meals rich in protein and healthy fats. Examples include eggs, lean meats, fish, nuts, and avocados."

  elif 18.5 <= bmi < 24.9:
    suggestion = "Your weight is normal.\nSuggestion: Maintain a balanced diet with a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats."
  elif 24.9 <= bmi < 29.9:
    suggestion = "You are overweight.\nSuggestion: Focus on portion control and incorporate more fruits, vegetables, whole grains, lean proteins, and low-fat dairy into your meals."
  else:
    suggestion = "You are in the obese range.\nSuggestion: It is advisable to consult a healthcare professional or nutritionist for a personalized meal plan."
  return suggestion


#assigning variables
weight = input("Enter your weight: ")
unit_of_weight = input("Enter unit of weight (kg, lbs): ")
height = input("Enter your height (eg. 5'6 for ft_in): ")
unit_of_height = input("Enter unit of height (ft_in, cm, m): ")

bmi = calculate_bmi(weight, height)
print("Body Mass Index (BMI):", bmi)

meal_suggestion = suggest_meals(bmi)

print("Result:", meal_suggestion)
