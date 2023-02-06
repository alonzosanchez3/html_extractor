from bs4 import BeautifulSoup

with open('./website.html', 'r') as html_file:
  contents = html_file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.string)
