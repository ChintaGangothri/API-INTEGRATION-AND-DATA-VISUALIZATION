import requests
import matplotlib.pyplot as plt


api_key = "d36ee602ac5846a9c223efe95a2d54e9"
city = "Hyderabad"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()


dates = []
temps = []

for item in data["list"][:8]:
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])


plt.figure()
plt.plot(dates, temps)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title(f"Weather Forecast - {city}")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
