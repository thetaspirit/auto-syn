from bs4 import BeautifulSoup


def bs4():
    f = open("source2", "r")
    source = f.read()
    f.close()

    soup = BeautifulSoup(source,"lxml")
    print([i.string for i in soup.find_all("button", {"class":"btn btn-link course-title"})])



import smtplib, ssl
from datetime import date
def email():
    formatted = """
LA: 100.0% [A]
French: 97.1% [A]
Math: 96.00% [A]
PE: 99.4%
Comp Graphics: 100.0% [A]
SS: 100.0% [A]
Chem: 3.6 [A]
    """
    smtp_server ="smtp-mail.outlook.com"
    port = 587
    #^ grabbed from ms
    sender_email = ""
    password = "
    receiver_email = ""

    today = date.today().strftime("%d/%m/%Y")
    message = f"""Subject: Grade Digest {today}

    {formatted}
    """

    print(message)
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def cc():
    formatted = """
LA: 100.0% [A]
French: 97.1% [A]
Math: 96.00% [A]
PE: 99.4%
Comp Graphics: 100.0% [A]
SS: 100.0% [A]
Chem: 3.6 [A]
    """
    smtp_server ="smtp-mail.outlook.com"
    port = 587
    #^ grabbed from ms
    sender_email = ""
    password = ""
    receiver_email = ""
    CC="" #change this

    today = date.today().strftime("%d/%m/%Y")
    message = f"From: {sender_email}\r\n" + f"To: {receiver_email}\r\n" + f"CC: {CC}\r\n" + f"Subject: Grade Digest {today}\r\n" + formatted

    print(message)
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def wasyn():
    import os
    import time
    import requests
    USERNAME=""
    PASSWORD=os.environ['PY_PASS'] #add your password as an environment var because sEcUrItY
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


    binary = FirefoxBinary('/usr/bin/firefox-developer-edition')
    x = webdriver.FirefoxOptions()
    #x.add_argument('--headless')
    driver = webdriver.Firefox(options=x,firefox_binary=binary)

    driver.get("https://wa-bsd405.edupoint.com/PXP2_Login_Student.aspx?regenerateSessionId=False")
    driver.find_element_by_css_selector('#ctl00_MainContent_username').send_keys(USERNAME)
    driver.find_element_by_css_selector('#ctl00_MainContent_password').send_keys(PASSWORD + Keys.RETURN)
    time.sleep(10)

    requests.get("https://wa-bsd405.edupoint.com/PXP2_Gradebook.aspx?AGU=0&studentGU=70EE0949-5EBF-445E-B8D3-3229D7499528")
    #the below WORKS
    #driver.find_element_by_css_selector("#mainnav > div:nth-child(1) > a:nth-child(8)").click()
wasyn()
