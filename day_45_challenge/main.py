import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
articles = soup.find_all(name="div", class_="article-title-description")

movie_list = list(reversed([article.select(selector="div h3")[0].getText() for article in articles]))
# print(movie_list)
# for article in articles:
#     title = article.select(selector="div h3")[0].getText()
#     movie_list.append(title)
list_text = "".join(f"{movie}\n" for movie in movie_list)
# list_text = ""
# for movie in movie_list:
#     list_text += f"{movie}\n"

with open(file="movies.txt", mode="w") as file:
    file.write(list_text)

