import re

def extract_urls_from_bio(bio_text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    urls = re.findall(url_pattern, bio_text)
    urls=[url.replace("u002F","") for url in urls]
    bio_urls="\n".join(urls)
    
    return bio_urls


# print(extract_urls_from_bio("NOVA CONTA : https://www.tiktok.com/@livedomanoodairdacosta?_t=8heo5ebNzYP&_r=1"))


# ??????????????????

from bs4 import BeautifulSoup
import requests

channel_url=f"https://www.tiktok.com/@discasdomanoodairdacosta"
# scraping additional data from channel url
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
}

soup = BeautifulSoup(requests.get(channel_url, headers=headers).content, "html.parser")
data=str(soup.prettify())

Bio=None
signature_match = re.search(r'"signature":"([^"]+)"', data)
if signature_match:
    Bio = signature_match.group(1)
else:
    Bio=""
    
urls_in_bio = extract_urls_from_bio(Bio)

print(Bio)
print(urls_in_bio)