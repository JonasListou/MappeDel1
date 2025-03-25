import json
import pandas as pd
import matplotlib.pyplot as plt

# Les inn JSON-filen
with open("miljødata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ekstraher tidspunkter og temperaturer
times = [entry["time"] for entry in data["properties"]["timeseries"]]
temps = [entry["data"]["instant"]["details"]["air_temperature"] 
         for entry in data["properties"]["timeseries"]]

# Opprett DataFrame
df = pd.DataFrame({"Time": pd.to_datetime(times), "Temperature (°C)": temps})

# Sorter etter tid (bare i tilfelle)
df = df.sort_values("Time")

# Plot temperatur over tid
plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["Temperature (°C)"], marker="o", linestyle="-", color="b")

# Formatering
plt.xlabel("Tid")
plt.ylabel("Temperatur (°C)")
plt.title("Temperaturutvikling i Trondheim")
plt.xticks(rotation=45)
plt.grid()

# Vis plot
plt.show()


