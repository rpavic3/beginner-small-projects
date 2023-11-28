from bs4 import BeautifulSoup

with open("chat_history.html", "r") as html_file:
	content = html_file.read()

	soup = BeautifulSoup(content, "lxml")
	froom = soup.find_all("div", class_="From")
	for course in froom:
		print(course)

