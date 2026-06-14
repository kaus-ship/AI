import requests
from bs4 import BeautifulSoup

def extract_web_text(url):

    html = requests.get(url).text

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    return [
        {
            "source": "Website",
            "reference": url,
            "text": soup.get_text(
                separator=" ",
                strip=True
            )
        }
    ]