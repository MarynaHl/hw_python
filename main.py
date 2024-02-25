from temperature import convert_temperature

temperatures = [
    "10°C",
    "70°F",
    "15°C",
    "62°F",
    "15°C",
    "17°C",
    "15°C",
    "61°F"
]

for temp in temperatures:
    print(f"{temp} is {convert_temperature(temp)}")
