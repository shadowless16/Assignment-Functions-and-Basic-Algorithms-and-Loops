def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = 25
print(f"{celsius_temp}°C is equal to {celsius_to_fahrenheit(celsius_temp)}°F")
