from bs4 import BeautifulSoup
import pandas as pd
import requests

# I COULD HAVE USED ONE LOOP TO COLLECT NAMES,YEAR AND RATINGS BUT THIS WAS EASIER TO READ

url = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(url.content, 'html.parser')
# df = pd.DataFrame(columns=["Name", "Rating", "Year"])
df = pd.DataFrame()

# COLLECTS THE NAMES
movie_names = soup.find_all("td", class_="titleColumn")
movie_name_list = []
for element in movie_names:
    movie = element.a.text
    movie_name_list.append(movie)
df["Name"] = movie_name_list

# COLLECTS THE YEARS
movie_ratings = soup.find_all("td", class_="ratingColumn imdbRating")
movie_rating_list = []
for element in movie_ratings:
    movie = element.text.strip()
    movie_rating_list.append(movie)
df["Rate"] = movie_rating_list

# COLLECTS THE RATINGS
movie_ratings = soup.find_all(class_="secondaryInfo")
movie_year_list = []
for element in movie_ratings:
    movie = element.text.strip("()")
    movie_year_list.append(movie)
df["Year"] = movie_year_list
print(df)
df.to_csv('C:\\Users\\utku1\\Desktop\\CODE\\Python Codes\\List.csv',
          sep=",", index=False)
