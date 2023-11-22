import pandas as pd
import matplotlib.pyplot as plt

# Path to your local file
file_path = "./planets.csv"  

# Read the CSV file
planets = pd.read_csv(file_path, index_col=0)

# Extract data for plotting
planet_masses = planets.loc['Mass (10**24kg)'] # This row contains the mass values for each planet
planet_names = planet_masses.index # This line retrieves the index of the planet_masses series, which contains the names of the planets

# plot the graph
plt.figure(figsize=(10, 6))
# planet_names provides the labels for the x-axis (names of the planets); planet_masses provides heights of the bars
plt.bar(planet_names, planet_masses, color='skyblue') 
# sets the y-axis scale to logarithmic
plt.yscale('log')
# rotates names of x-axis
plt.xticks(rotation=45)
# Labels
plt.xlabel('Planets')
plt.ylabel('Mass (10^24 kg)')
plt.title('Mass of Planets in the Solar System (Log Scale)')
# Display
plt.show()
