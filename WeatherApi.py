import requests;
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;

url = "https://api.open-meteo.com/v1/forecast";

params = {
    "latitude": 18.52,
    "longitude": 73.85,
    "hourly": "temperature_2m"
};

response = requests.get(url, params=params);

# print(response.status_code);
# print();
# print(response);
# print();
# print(response.json())
weather_data = response.json();
# print(weather_data);
# print(weather_data.keys());
times = weather_data['hourly']['time'];
temperatures = weather_data['hourly']['temperature_2m'];
# print(times);
# print(temperatures);

# Using Pandas to create a DataFrame
df = pd.DataFrame({
    'Time': times,
    'Temperature': temperatures
});
# print(df);
# print();
# print(df.head());

# Data Cleaning
# df['Time'] = pd.to_datetime(df['Time']);
# print(df.dtypes);

# Numerical Analysis using NumPy
# avg_temp = np.mean(df['Temperature']); # Finding the average temperature
# max_temp = np.max(df['Temperature']); # Finding the maximum temperature
# min_temp = np.min(df['Temperature']); # Finding the minimum temperature
# std_temp = np.std(df['Temperature']); # Finding the standard deviation of temperature

# print(f"Average Temperature: {avg_temp}");
# print(f"Maximum Temperature: {max_temp}");
# print(f"Minimum Temperature: {min_temp}");
# print(f"Standard Deviation of Temperature: {std_temp}");

# Advanced Analysis using Pandas
# Hottest Hour
# hottest = df.loc[df['Temperature'].idxmax()];
# print(f"Hottest Hour: {hottest['Time']} with Temperature: {hottest['Temperature']}");

# Coldest Hour
# coldest = df.loc[df['Temperature'].idxmin()];
# print(f"Coldest Hour: {coldest['Time']} with Temperature: {coldest['Temperature']}");

# Top 5 Highest Temperatures
# top_5 = df.nlargest(5, 'Temperature');
# print("Top 5 Highest Temperatures:");
# print(top_5);

# Data Visualization using Matplotlib

# Line Chart for Temperature Trend
# plt.figure(figsize=(12, 6));
# plt.plot(df['Time'], df['Temperature'], marker='o', linestyle='-', color='b');
# plt.title('Hourly Temperature Trend');
# plt.xlabel('Time');
# plt.ylabel('Temperature (°C)');
# plt.grid(True);
# plt.show();

# Histogram for Temperature Distribution
# plt.figure(figsize=(10, 5));
# plt.hist(df['Temperature'], bins=15, color='orange', edgecolor='black');
# plt.title('Temperature Distribution');
# plt.xlabel('Temperature (°C)');
# plt.ylabel('Frequency');
# plt.show();

# Scatter Plot for Temperature vs Time
plt.figure(figsize=(12, 6));
plt.scatter(df['Time'], df['Temperature'], color='green');
plt.title('Temperature vs Time');
plt.xlabel('Time');
plt.ylabel('Temperature (°C)');
# plt.show();
plt.savefig('temperature_vs_time.png');  # Save the scatter plot as an image

# Save DataFrame to CSV
df.to_csv('weather_data.csv', index=False);