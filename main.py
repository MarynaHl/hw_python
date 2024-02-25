import csv
from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

def convert_temperature(input_file, output_file, target_unit):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Date', 'Reading'])
        writer.writeheader()
        
        for row in rows:
            temperature = float(row['Reading'].strip('°C°F'))
            if 'C' in row['Reading']:
                converted_temperature = celsius_to_fahrenheit(temperature) if target_unit == 'F' else temperature
            elif 'F' in row['Reading']:
                converted_temperature = fahrenheit_to_celsius(temperature) if target_unit == 'C' else temperature
            else:
                raise ValueError("Invalid temperature unit")
            
            writer.writerow({'Date': row['Date'], 'Reading': f"{converted_temperature}°{target_unit}"})

if __name__ == "__main__":
    convert_temperature('input.csv', 'output.csv', 'C')

