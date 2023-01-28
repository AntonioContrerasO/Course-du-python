from bs4 import BeautifulSoup
import requests
import spotipy

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"html.parser")
titles = soup.find_all(name="h3",class_="title")
only_titles = [titles[i].text for i in range(99,-1,-1)]
print(only_titles)
titles_send = ""
for i in range(0,100):
    titles_send += only_titles[i]+"\n"

with open("movies.txt",mode="w") as file:
    file.write(titles_send)
























# responce = requests.get(url="https://news.ycombinator.com/news")
# contents = responce.text
# soup = BeautifulSoup(contents,"html.parser")
#
# titles = soup.find_all(name="a",class_="titlelink")
# scores = soup.find_all(name="span",class_="score")
# texts = []
# links = []
# score_int = []
# n = 0
# for title in titles:
#     texts.append(title.text)
#     links.append(title.get("href"))
#     score_int.append(int(scores[n].getText().split()[0]))
#     n += 1
# max_score = max(score_int)
# index = score_int.index(max_score)
# print(texts[index])
# print(links[index])
# print(score_int[index])





































# # import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.p)
#
# # all_anchor_taps = soup.find_all(name="a")
# # print(all_anchor_taps)
# # for tag in all_anchor_taps:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# heading = soup.select(".heading")
# print(heading)