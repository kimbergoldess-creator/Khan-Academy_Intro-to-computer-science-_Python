height=float(input("Type your height in meters (m) "))
weight=float(input("Type your weight in kilos (kg) "))
imc=(round(weight/(height*height),2))
print("Your IMC is " + str(imc))
if imc>30:
    print("You are obese ")
elif imc>=25:
    print("You are overweight ")
elif imc<=18.5:
    print("You are underweight")
else:
    print("You are nomrmal weight")
