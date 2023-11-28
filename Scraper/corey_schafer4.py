from requests_html import HTML, HTMLSession

"""with open("home.html") as html_file:
	source = html_file.read()
	html = HTML(html=source)

articles = html.find("div.article")

for article in articles:
	headline = article.find("h2", first=True).text
	summary = article.find("p", first=True).text

	print(headline)
	print(summary)
	print()"""

session = HTMLSession()
r = session.get("https://coreyms.com")
article = r.html.find("article", first=True)
print(article.attrs)

