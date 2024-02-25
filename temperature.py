def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature(temperature_str):
    if '°C' in temperature_str:
        temperature = int(temperature_str.split('°C')[0])
        return celsius_to_fahrenheit(temperature)
    elif '°F' in temperature_str:
        temperature = int(temperature_str.split('°F')[0])
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError('Invalid temperature format')
