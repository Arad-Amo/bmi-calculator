while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number for age!")

if age < 18:
    print("BMI calculation is not applicable for individuals under 18.")
else:
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            height = float(input("Enter your height (m): "))
            break
        except ValueError:
            print("Please enter valid numbers for weight and height!")

    BMI = weight / (height ** 2)

    if BMI < 18.5:
        print("Category: Underweight")
    elif 18.5 <= BMI < 25:
        print("Category: Normal")
    elif 25 <= BMI < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    print(f"Your BMI is: {BMI}")
