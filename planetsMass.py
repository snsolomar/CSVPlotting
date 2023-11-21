import pandas as pd
import matplotlib.pyplot as plt

# Path to your local file
file_path = "./planets.csv"  # Replace with your file's actual path

# Read the CSV file
planets = pd.read_csv(file_path, index_col=0)

# Extract data for plotting
planet_masses = planets.loc['Mass (10**24kg)']
planet_names = planet_masses.index

# plot the graph
plt.figure(figsize=(10, 6))
plt.bar(planet_names, planet_masses, color='skyblue')
plt.yscale('log')
plt.xticks(rotation=45)
plt.xlabel('Planets')
plt.ylabel('Mass (10^24 kg)')
plt.title('Mass of Planets in the Solar System (Log Scale)')
plt.show()
