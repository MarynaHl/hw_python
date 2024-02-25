def convert_temperature(temperature_str):
    if '°C' in temperature_str:
        temperature = int(temperature_str.split('°C')[0])
        return (temperature * 9/5) + 32
    elif '°F' in temperature_str:
        temperature = int(temperature_str.split('°F')[0])
        return (temperature - 32) * 5/9
    else:
        raise ValueError('Invalid temperature format')

