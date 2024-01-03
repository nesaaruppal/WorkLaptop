# Define the conversion factor
conversion_factor = 9/5 * 100

# Define a function to convert temperatures
def convert_temperature(temperature, from_temp, to_temp):
    return (temperature - 32) * (5/9) * conversion_factor if from_temp == "F" else (temperature / conversion_factor) * (9/5) + 32 if to_temp == "C" else (temperature - 273.15)

# Get the input temperature
temperature = float(input("Enter the temperature: "))

# Get the input temperature units
from_temp = input("Enter the temperature units (F or C): ")
to_temp = input("Enter the desired temperature units (F or C): ")

# Convert the temperature
result = convert_temperature(temperature, from_temp, to_temp)

# Print the result
print(f"{temperature} {from_temp} is {result} {to_temp}.")