import requests
import matplotlib.pyplot as plt

API_KEY = "6c2f910a54323383bdaef3310d440ef7"
CITY = "Pune"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)   # for DEBUG

temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

labels = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
values = [temperature, humidity, pressure]

plt.bar(labels, values)
plt.title(f"Weather Data for {CITY}")
plt.show()
