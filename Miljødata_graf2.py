import json
import pandas as pd
import matplotlib.pyplot as plt

# Les inn JSON-filen
with open("miljødata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ekstraher tidspunkter og værparametere
times = []
temps = []
wind_speeds = []
precipitations = []
uv_indexes = []

for entry in data["properties"]["timeseries"]:
    times.append(entry["time"])
    
    details = entry["data"]["instant"]["details"]
    temps.append(details.get("air_temperature", None))
    wind_speeds.append(details.get("wind_speed", None))
    precipitations.append(entry["data"].get("next_1_hours", {}).get("details", {}).get("precipitation_amount", 0))
    uv_indexes.append(entry["data"].get("instant", {}).get("details", {}).get("ultraviolet_index_clear_sky", 0))

# Opprett DataFrame
df = pd.DataFrame({
    "Time": pd.to_datetime(times),
    "Temperature (°C)": temps,
    "Wind Speed (m/s)": wind_speeds,
    "Precipitation (mm)": precipitations,
    "UV Index": uv_indexes
})

# Sorter etter tid
df = df.sort_values("Time")

# Plot værdata
plt.figure(figsize=(12, 6))

plt.plot(df["Time"], df["Temperature (°C)"], marker="o", linestyle="-", label="Temperatur (°C)", color="b")
plt.plot(df["Time"], df["Wind Speed (m/s)"], marker="s", linestyle="--", label="Vindhastighet (m/s)", color="g")
plt.plot(df["Time"], df["Precipitation (mm)"], marker="^", linestyle=":", label="Nedbør (mm)", color="c")
plt.plot(df["Time"], df["UV Index"], marker="d", linestyle="-.", label="UV-indeks", color="m")

# Formatering
plt.xlabel("Tid")
plt.ylabel("Målinger")
plt.title("Værdata for Trondheim")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Vis plot
plt.show()

# Skriv ut første 10 rader som tabell for å vise verdier
print(df.head(10))
