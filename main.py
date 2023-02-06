from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.select(".titleline a")
article_texts = [article.getText() for article in articles]
article_links = [article.get('href') for article in articles]
print(article_links)
article_upvotes = soup.find_all(name='span', class_="score")
article_upvotes = [article.getText() for article in article_upvotes]
print(article_upvotes)



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
