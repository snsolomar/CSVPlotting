import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "./movies.csv"
movies = pd.read_csv(file_path)

# Filter the DataFrame for movies released between 1990 and 2017
filtered_movies = movies[(movies['Year'] >= 1990) & (movies['Year'] <= 2017)]

# Count the number of movies by year
movie_counts_by_year = filtered_movies['Year'].value_counts()

# Sort the counts by year for better visualization
sorted_movie_counts_by_year = movie_counts_by_year.sort_index()

# Create the plot
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
sorted_movie_counts_by_year.plot(kind='bar')

# Labels
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.title('Number of Movies Released Each Year')
# Rotate x-axis labels for better readability
plt.xticks(rotation=45)  
plt.show()

