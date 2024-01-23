# Netflix Movie Duration Analysis #

## Overview

This project explores the Netflix dataset to analyze the duration of movies and investigate if there is evidence of movies getting shorter over time. The analysis involves loading the Netflix data, filtering out TV shows, and focusing on movies. We then examine the distribution of movie durations, particularly those shorter than 60 minutes, and those longer than 60 minutes or 60 minutes exactly. The findings are visualized through a bar plot to provide insights into the trend of movie durations over the years.

### Short Movie Data:

- **Objective:** Short Movies Bar Chart Code
  
- **Code Snippet:**
  ```python
  fig = plt.figure(figsize=(10, 6))
  short_movies = netflix_movies[netflix_movies['duration'] < 60]
  plt.bar(x=short_movies['release_year'], height=short_movies['duration'], color='green')
  plt.xlabel('release_year')
  plt.ylabel('duration')
  plt.title('Movies Under 60 mins')
  plt.show()
  ```

### Short Movies Bar Chart:
<img width="996" alt="Screenshot 2024-01-23 at 5 00 30 PM" src="https://github.com/Gregory204/Investigating-Netflix-Movies/assets/131078905/f63b50bb-d018-4d20-80a9-54340a2f4e57">

### Long Movie Data:

- **Objective:** Long Movies Bar Chart Code
  
- **Code Snippet:**
  ```python
  fig = plt.figure(figsize=(10, 6))
  long_movies = netflix_movies[netflix_movies['duration'] >= 60]
  plt.bar(x=long_movies['release_year'], height=long_movies['duration'], color='red')
  plt.xlabel('release_year')
  plt.ylabel('duration')
  plt.title('Movies Over 60 mins')
  plt.show()
  ```

### Long Movies Bar Chart:
<img width="998" alt="Screenshot 2024-01-23 at 5 02 01 PM" src="https://github.com/Gregory204/Investigating-Netflix-Movies/assets/131078905/3aca29fa-d60e-4f2b-b217-0e43bd0dfeda">

## How?

The analysis is conducted using Python, with the primary libraries being Matplotlib and Pandas. Various data manipulation techniques, such as sorting, slicing, and indexing, are employed to extract relevant information from the Netflix dataset.

## Why?

Driven by a growing interest in data analysis, this project serves as an exploration into the field. The task aims to answer questions about the changing landscape of Netflix movies and contributes to building skills in data analysis. Aspiring to delve into deep learning, machine learning, and artificial intelligence in the future, this project lays the foundation for broader knowledge in the field.

## What's Next?

Excited about the world of data, the plan is to continue working on more projects related to data analysis. 

## Conclusion

After performing the analysis and visualizing the data, the question "Are we certain that movies are getting shorter?" is addressed. The answer is provided in the analysis results down below. (Hint: No they aren't getting shorter)

### Short vs Large Movie Data:


- **Objective:** Short vs Long Movies Bar Chart Code.
  
- **Code Snippet:**
  ```python
  fig = plt.figure(figsize=(10, 6))
  plt.bar(x=short_movies['release_year'] - 0.2,
  height=short_movies['duration'], label='Short Movies', color='green')
  plt.bar(x=long_movies['release_year'], height=long_movies['duration'], label='Long Movies', alpha=0.7, color='red')
  plt.xlabel('Release Year')
  plt.ylabel('Duration (min)')
  plt.title('Movies Duration Comparison')
  plt.legend()
  plt.show()
  ```

### Short Vs Long Movies Bar Chart:
<img width="999" alt="Screenshot 2024-01-23 at 4 54 33 PM" src="https://github.com/Gregory204/Investigating-Netflix-Movies/assets/131078905/19d0cbed-7b78-4d9b-8e7a-ecf8d71da303">



