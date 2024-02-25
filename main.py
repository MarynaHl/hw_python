import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from distance import meters_to_feet, feet_to_meters

def convert_temperature_and_distance(input_file, output_file, target_unit):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Date', 'Distance', 'Reading'])
        writer.writeheader()
        
        for row in rows:
            temperature = float(row['Reading'].strip('°C°F'))
            if 'C' in row['Reading']:
                converted_temperature = celsius_to_fahrenheit(temperature) if target_unit == 'F' else temperature
            elif 'F' in row['Reading']:
                converted_temperature = fahrenheit_to_celsius(temperature) if target_unit == 'C' else temperature
            else:
                raise ValueError("Invalid temperature unit")

            distance = float(row['Distance'].strip('mft'))
            if 'm' in row['Distance']:
                converted_distance = meters_to_feet(distance) if target_unit == 'ft' else distance
            elif 'ft' in row['Distance']:
                converted_distance = feet_to_meters(distance) if target_unit == 'm' else distance
            else:
                raise ValueError("Invalid distance unit")

            writer.writerow({'Date': row['Date'], 'Distance': f"{converted_distance}{target_unit}", 'Reading': f"{converted_temperature}°{target_unit}"})

if __name__ == "__main__":
    convert_temperature_and_distance('input.csv', 'output.csv', 'C')
