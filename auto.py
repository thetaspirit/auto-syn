from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from bs4 import BeautifulSoup

import smtplib, ssl
import os
import time
from datetime import date

#GLOBALS because this is a util script not "good" code
USERNAME="" #Synergy Username
#add your password as an environment var because sEcUrItY
PASSWORD=os.environ['PY_PASS'] #Synergy Password
EMAIL_PASS=os.environ['PY_EMAIL_PASS'] #Email account password (for the account with SENDER address)
SENDER="" #Email address you're sending from

RECIEVER="" #Email address you're sending to

#driver settings
#firefox
"""
binary = FirefoxBinary('/usr/bin/firefox-developer-edition')
x = webdriver.FirefoxOptions()
x.add_argument('--headless')
driver = webdriver.Firefox(options=x,firefox_binary=binary)
"""
x = webdriver.FirefoxOptions()
x.add_argument('--headless')
driver = webdriver.Firefox(options=x)

#Chrome - download and place chromedriver in path
#x = webdriver.ChromeOptions()
#x.add_argument('--headless')
#driver = webdriver.Chrome(options=x)

#Safari
#x = webdriver.SafariOptions()
#x.add_argument('--headless')
#driver = webdriver.Safari(options=x)

#login
driver.get("https://wa-bsd405.edupoint.com/PXP2_Login_Student.aspx?regenerateSessionId=False")
driver.find_element_by_css_selector('#ctl00_MainContent_username').send_keys(USERNAME)
driver.find_element_by_css_selector('#ctl00_MainContent_password').send_keys(PASSWORD + Keys.RETURN)

#wait for page to load
#yes this is bad practice
#no I don't care because at least it doesn't cause problems this way
time.sleep(10)

#get gradebook page source
driver.find_element_by_css_selector("#mainnav > div:nth-child(1) > a:nth-child(8)").click()

#alternatively, a potentially faster way is to use something like the below but I couldn't get that working /shrug
#driver.get("https://wa-bsd405-psv.edupoint.com/PXP2_Gradebook.aspx?AGU=0&studentGU=70EE0949-5EBF-445E-B8D3-3229D7499528")
source = driver.page_source
#print(source)

#feed source to bs4
soup = BeautifulSoup(source,"lxml")
#grab marks and scores from source
marks = [i.string for i in soup.find_all('span', class_="mark")]
scores = [i.string for i in soup.find_all('span', class_="score")]

#hardcoded for speeeeeeeed (haha yea right it's python) and aesthetics
classes = ["LA", "French", "Math", "PE", "Comp Graphics", "SS", "Chem"]
#to grab the array of classes normally
#classes=[i.string for i in soup.find_all("button", {"class":"btn btn-link course-title"})]

#print(marks)
#print(scores)

#create a list of tuples with class, mark score
everything = list(zip(classes, marks, scores))

#format above data
formatted = ""
for x in everything:
    formatted += f"{x[0]}: {x[2]} [{x[1]}]\n"

#email to parental figure(s)
smtp_server ="smtp-mail.outlook.com"
port = 587
#^ grabbed from ms

today = date.today().strftime("%d/%m/%Y")

#if you want to cc someone (such as yourself or a secondary parent)
#CC=SENDER #or other value
#message = f"From: {SENDER}\r\n" + f"To: {RECIEVER}\r\n" + f"CC: {CC}\r\n" + f"Subject: Grade Digest {today}\r\n" + formatted

message = f"""Subject: Grade Digest {today}

{formatted}
"""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context) # Secure the connection
    server.login(SENDER, EMAIL_PASS)
    server.sendmail(SENDER, RECIEVER, message)

driver.close()
