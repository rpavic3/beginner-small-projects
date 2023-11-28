import requests

r = requests.get("https://httpbin.org/delay/6", timeout=3)

print(r)
"""payload = {"username": "robika", "password": "bobika"}
r = requests.post("https://httpbin.org/post", data=payload)
r_dict = r.json()
print(r_dict["form"])"""


#skidanje slike
"""
r = requests.get("https://imgs.xkcd.com/comics/python.png")
with open("comic.png", "wb") as f:
	f.write(r.content)
"""
