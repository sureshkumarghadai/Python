import requests
import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
url = "https://api.open-meteo.com/v1/forecast";

params = {
    "latitude": 18.52,
    "longitude": 73.85,
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params);

print(response.status_code);
print();
print(response);
print();
print(response.json);
weather_data = response.json();
print(weather_data);
print(weather_data.keys());
times = weather_data['hourly']['time'];
temperatures = weather_data['hourly']['temperature_2m'];

#Using Pandas to create a dataframe
df= pd.DataFrame({
    'Time': times,
    'Temperature': temperatures
});
print(df);
print();
print(df.head());

# Data cleaing
df['Time'] = pd.to_datetime(df['Time']);
print(df.dtypes);

# Numerical analysis using NumPy
avg_temp = np.mean(df['Temperature']);
max_temp = np.max(df['Temperature']);
min_temp = np.min(df['Temperature']);
std_temp = np.std(df['Temperature']);

print(f"Average Temperature: {avg_temp}");


# Advanced Analysis usine Pandas
# hosttest hour
hottest = df.loc[df['Temperature'].idxmax()];
print(f"Hottest Hour: {hottest['Time']} with Temperature: {hottest['Temperature']}");

#Coldest Hour
coldest = df.loc[df['Temperature'].idxmin];
print(f"Colderst Hour: {coldest['Time']} with Temperature: {coldest['Temperature']}");
#Top 5 Highest Temperature
top_5 = df.nlargest(5, 'Temperature');
print(top_5);

# Data Visualization using Matplotlib
plt.figure(figsize=(12, 6));
plt.plot(df['Time',df['Temperature'],marker='0',linestyle='-',color='b']);
plt.title
 