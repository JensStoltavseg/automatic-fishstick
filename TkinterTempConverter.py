

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature():
    if temp_scale.get() == "Celsius":
        celsius = float(temp_entry.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        result_label.config(text=f"{fahrenheit:.2f}°F")
    elif temp_scale.get() == "Fahrenheit":
        fahrenheit = float(temp_entry.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        result_label.config(text=f"{celsius:.2f}°C")

