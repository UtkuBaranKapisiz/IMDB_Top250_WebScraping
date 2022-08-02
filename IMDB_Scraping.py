from bs4 import BeautifulSoup
import pandas as pd
import requests

# I COULD HAVE USED ONE LOOP TO COLLECT NAMES,YEAR AND RATINGS BUT THIS WAS EASIER TO READ
base_url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
url = requests.get(base_url)
soup = BeautifulSoup(url.text, "lxml")
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
movie_years = soup.find_all("td", class_="ratingColumn imdbRating")
movie_rating_list = []
for element in movie_years:
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
# COLLECTS THE LINKS
table = soup.find_all("table")
movie_link_list = []
for i in table:
    get_td = i.find_all('td', class_="titleColumn")
    for j in get_td:
        get_ = j.find('a')['href'].strip().split('>')[-1]
        movie_link_list.append("www.imdb.com" + get_)
df["Link"] = movie_link_list
df.to_csv('C:\\Users\\utku1\\Documents\\GitHub\\IMDB_Top250_WebScraping\List.csv',
          sep=",", index=False)
