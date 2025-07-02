class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin = celsius + 273.15
        fahrenheit = round(celsius * 1.80, 5) + 32
        return [kelvin, fahrenheit]