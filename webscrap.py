from bs4 import BeautifulSoup
import requests
import re
import csv

url ="https://www.imdb.com/chart/top"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

movies = soup.select('td.titleColumn')
links =[a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data value') for b in soup.select('td.ratingColumn strong')]

imdb =[]


for index in range(0, len(movies)):
    mov_str = movies[index].get_text()
    movie = (' '.join(mov_str.split()).replace(',',''))
    movie_title = movie[len(str(index))+1: -7]
    year = re.search('\((.*?)\)', mov_str).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data ={"movie_title": movie_title,
           "year": year,
           "place": place,
           "star_cast": crew[index],
           "rating": ratings[index],
           "vote": votes[index],
           "link": links[index]
           }
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring', item['star_cast'] )
