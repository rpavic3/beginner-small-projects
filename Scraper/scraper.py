import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time


def send_mail():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("rpavic3@gmail.com", "wobwamddaovolxdv")

	msg = MIMEText(f"Cijena je {kune_i_lipe}kn", "plain", "utf-8")

	msg["From"] = "rpavic3@gmail.com"
	msg["To"] = "rpavic3@gmail.com"

	msg["Subject"] = proizvod

	server.send_message(msg)
	print("email sent")
	server.quit()


lista_namirnica = ["https://www.konzum.hr/web/products/pringoooals-hot-spicy-165-g", "https://www.konzum.hr/web/products/deutsche-markenbutter-maslac-250-g", "https://www.konzum.hr/web/products/alpsko-trajno-mlijeko-3-5-m-m-1-l", "https://www.konzum.hr/web/products/eva-sardina-u-maslinovu-ulju-gold-81-g", "https://www.konzum.hr/web/products/cikla-360-g", "https://www.konzum.hr/web/products/brokula-750-grama-k-plus", "https://www.konzum.hr/web/products/doritos-nacho-cips-sir-100-g", "https://www.konzum.hr/web/products/rikula-125-g", "https://www.konzum.hr/web/products/bovidur-tvrdi-sir-200-g-vindija", "https://www.konzum.hr/web/products/rio-mare-insalatissime-tuna-na-meksicki-nacin-160-g", "https://www.konzum.hr/web/products/masline-zelene-otkostene-160-g-podravka", "https://www.konzum.hr/web/products/old-spice-wolfthron-stick-50-ml"]
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
for i in lista_namirnica:
	URL = i
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.text, "html.parser")



	kune = str(soup.find("span",{"class": "price--kn"}).get_text())
	lipe = str(soup.find("span",{"class": "price--li"}).get_text())

	proizvod = soup.find("h1",{"class": "fs-juliett-alpha color-black"}).get_text().strip()

	kune_i_lipe = kune + "," + lipe

	if "Pringles" in proizvod and int(kune) < 15:
		send_mail()
	if "Maslac" in proizvod and int(kune) <= 17:
		send_mail() 
	if "mlijeko" in proizvod and int(kune) < 10:
		send_mail() 
	if "sardine" in proizvod and int(kune) < 12:
		send_mail()
	if "Cikla" in proizvod and int(kune) < 10:
		send_mail() 
	if "Brokula" in proizvod and int(kune) <= 17:
		send_mail() 
	if "Doritos" in proizvod and int(kune) < 11:
		send_mail() 
	if "Rikula" in proizvod and int(kune) < 9:
		send_mail()
	if "Bovidur" in proizvod and int(kune) < 31:
		send_mail() 
	if "Rio" in proizvod and int(kune) < 16:
		send_mail() 
	if "Spice" in proizvod and int(kune) < 29:
		send_mail()

	time.sleep(1)