from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name='span', class_='titleline')
print(len(articles))
article_texts = [article.getText() for article in articles]
print(len(article_texts))
article_links = [article.find(name='a').get('href') for article in articles]
article_upvotes = soup.find_all(name='span', class_="score")
article_upvotes = [int(article.getText().split(' ')[0]) for article in article_upvotes]
print(article_upvotes)

max_index = 0
for i in range(0, len(article_upvotes)):
  if article_upvotes[max_index] < article_upvotes[i]:
    max_index = i

print(article_texts[max_index], article_links[max_index])
#





# with open('./website.html', 'r') as html_file:
#   contents = html_file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# all_anchor_tags = soup.find_all(name='a')

# for tag in all_anchor_tags:
#   print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.text)

# company_url = soup.select_one(selector='p a')
# print(company_url.get('href'))
