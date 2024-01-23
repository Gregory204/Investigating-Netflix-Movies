import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')
# Remove TV shows use Movie type
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']  # only working with movies
netflix_movies = netflix_subset[['title','country','genre','release_year','duration']]  # using columns with the movie type

fig = plt.figure(figsize=(10, 6))

short_movies = netflix_movies[netflix_movies['duration'] < 60]
#short_movies_am = len(short_movies)  # 420 movies (overall years)
'''
plt.bar(x=short_movies['release_year'], height=short_movies['duration'], color='green')
plt.xlabel('release_year')
plt.ylabel('duration')
plt.title('Movies Under 60 mins')
plt.show()
'''

long_movies = netflix_movies[netflix_movies['duration'] >= 60]
#long_movies_am = len(long_movies)  # 4931 movies (overall years)
'''
plt.bar(x=long_movies['release_year'], height=long_movies['duration'], color='red')
plt.xlabel('release_year')
plt.ylabel('duration')
plt.title('Movies Over 60 mins')
plt.show()
'''

# Bar chart to show short vs long movies comparison:
fig = plt.figure(figsize=(10, 6))
plt.bar(x=short_movies['release_year'] - 0.2, height=short_movies['duration'], label='Short Movies', color='green')
plt.bar(x=long_movies['release_year'], height=long_movies['duration'], label='Long Movies', alpha=0.7, color='red')
plt.xlabel('Release Year')
plt.ylabel('Duration (min)')
plt.title('Movies Duration Comparison')
plt.legend()
plt.show()
'''
