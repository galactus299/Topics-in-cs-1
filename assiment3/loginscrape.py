import requests
from bs4 import BeautifulSoup

client = requests.Session()

HOMEPAGE_URL = "https://www.linkedin.com"
LOGIN_URL = "https://www.linkedin.com/uas/login-submit"
CONNECTIONS_URL = "https://www.linkedin.com/mynetwork/invite-connect/connections/"

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html, "html.parser")
csrf = soup.find("input", dict(name="loginCsrfParam"))["value"]

login_information = {
    "session_key": "mianshayanbabar@outlook.com",
    "session_password": "******",
    "loginCsrfParam": csrf,
}

try:
    client.post(LOGIN_URL, data=login_information)
    print("Login Successful")
    page = client.get("https://www.linkedin.com/in/rbranson")
    print(page.text)
except:
    print("Failed to Login")
