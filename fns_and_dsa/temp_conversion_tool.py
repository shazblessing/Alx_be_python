FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for C to F

def convert_to_celsius(fahrenheit):
  """
  Converts a temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit (float).

  Returns:
      The temperature converted to Celsius (float).
  """
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

def convert_to_fahrenheit(celsius):
  """
  Converts a temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius (float).

  Returns:
      The temperature converted to Fahrenheit (float).
  """
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

def main():
  """
  Prompts the user for temperature conversion and displays the result.
  """
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
      if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        converted_unit = 'F'
      elif unit == 'F':
        converted_temperature = convert_to_celsius(temperature)
        converted_unit = 'C'
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
      print(f"{temperature:.1f}°{unit} is {converted_temperature:.1f}°{converted_unit}")
      break
    except ValueError as e:
      print(f"Error: {e}. Please enter a valid numeric value and unit.")

if __name__ == "__main__":
  main()