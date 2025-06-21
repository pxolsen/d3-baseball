import requests
from bs4 import BeautifulSoup
from random import randint

user_agent_list = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
            'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
        ]

url = "https://www.ncsasports.org/baseball/division-3-colleges"

rand_index = randint(0, len(user_agent_list) -1)

headers = {
    "User-Agent": user_agent_list[rand_index]
}

session = requests.Session()
session.headers = {}
response = session.get(url=url, headers=headers, allow_redirects=True)
soup = BeautifulSoup(response.content, "html.parser")
school_rows = soup.find_all(attrs={"itemprop": "item"})


for row in school_rows:
    contents = row.find_all("div")
    school_name = contents[0].text
    location_contents = contents[1].find_all("span")
    city = location_contents[0].text
    state = location_contents[1].text
    school_type = contents[2].text
    conference = contents[3].text
    division = contents[4].text
    print({
        "name": school_name,
        "city": city,
        "state": state,
        "type": school_type,
        "conference": conference,
        "division": division
        }
    )


