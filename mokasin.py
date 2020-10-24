import smtplib, ssl
import requests
from bs4 import BeautifulSoup
import time


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "*****"  # Enter your address
receiver_email = "*****"  # Enter receiver address
password = "*****"
prevCount = 29
goodMessage = """\
Subject: Good News

Your sub count has changed positively

check it here: YOUTUBE_URL """

badMessage = """\
Subject: Bad News

Your sub count has changed negatively

check it here: YOUTUBE_URL """

while True:
	session = requests.session()

	req = session.get('SOCIALBLADE_REALTIME_URL')

	doc = BeautifulSoup(req.content, 'lxml')

	count = doc.findAll("span", {"class": "odometer-value"})

	print(count)
	if count.text != prevCount:
		print(allGuns[1])
		usedCost, unusedCost = allGuns[1].text.split('.', 1)
		unusedCost, usedCost = usedCost.split('$', 1)
		if count.text > prevCount:
			context = ssl.create_default_context()
			with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			    server.login(sender_email, password)
			    server.sendmail(sender_email, receiver_email, goodMessage)
			print("Good Message sent")
		else:
			context = ssl.create_default_context()
			with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			    server.login(sender_email, password)
			    server.sendmail(sender_email, receiver_email, badMessage)
			print("Bad Message sent")
	else:
		print("Count has not changed yet :(")
	
	prevCount = count

	time.sleep(30)

