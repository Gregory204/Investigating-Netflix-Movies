import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')
# Remove TV shows use Movie type
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']  # only working with movies
netflix_movies = netflix_subset[['title','country','genre','release_year','duration']]  # using columns with the movie type
''' Output:
                                        title  ... duration
1                                        7:19  ...       93
2                                       23:59  ...       78
3                                           9  ...       80
4                                          21  ...      123
6                                         122  ...       95
...                                       ...  ...      ...
7781                                     Zoom  ...       88
7782                                     Zozo  ...       99
7783                                   Zubaan  ...      111
7784                        Zulu Man in Japan  ...       44
7786  ZZ TOP: THAT LITTLE OL' BAND FROM TEXAS  ...       90

[5377 rows x 5 columns]
'''
# Find movies shorter than 60 mins
short_movies = netflix_movies[netflix_movies['duration'] < 60]  # gathers the movies that are shorter than 60 mins
''' Output:
                                                  title  ... duration
35                                            #Rucker50  ...       56
55                  100 Things to do Before High School  ...       44
67    13TH: A Conversation with Oprah Winfrey & Ava ...  ...       37
101                                   3 Seconds Divorce  ...       53
146                                      A 3 Minute Hug  ...       28
...                                                 ...  ...      ...
7679                    WWII: Report from the Aleutians  ...       45
7692  Ya no estoy aquí: Una conversación entre Guill...  ...       15
7718                     Yoo Byung Jae: Discomfort Zone  ...       54
7771                                               Zion  ...       12
7784                                  Zulu Man in Japan  ...       44

[420 rows x 5 columns]
'''
# Give each genre in netflix movies their own color.
colors = []
for label, row in netflix_movies.iterrows():
    if row['genre'] == "Children":
        colors.append('red')
    elif row['genre'] == "Documentaries":
        colors.append('blue')
    elif row['genre'] == "Stand-Up":
        colors.append('yellow')
    else:
        colors.append('purple')

# Create a scatter plot to find out if movies are getting shorter as time goes on.
fig = plt.figure(figsize=(12, 8))
plt.scatter(x=netflix_movies['release_year'], y=netflix_movies['duration'], c=colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

# The answer is no, according to the scatter plot
# The scatter plot is a file in this repository.
