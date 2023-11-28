import smtplib
import requests

r = requests.get("https://coreyms.com", timeout=5)

if r.status_code != 200:
	with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login("rpavic3@gmail.com", "wobwamddaovolxdv")

		subject = "SITE IS DOWN"
		body = "restart servers"
		msg = f"Subject: {subject}\n\n{body}"

		smtp.sendmail("rpavic3@gmail.com", "rpavic3@gmail.com", msg)
