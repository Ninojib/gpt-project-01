import requests
from bs4 import BeautifulSoup

# Replace the URL below with the website you want to scrape
url = ''

# Send an HTTP request to the website
response = requests.get(url)
print('scrapper')
# print(response.text)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the website
    soup = BeautifulSoup(response.text, 'html.parser')

  # Find the span element with the class "ClassLevel1PickUp"
    span = soup.find_all('span', {'class': 'ClassLevel1PickUp'})

    for s in span:
        print(s.get_text(strip=True))

else:
    print(f"Failed to fetch the website content. Status code: {response.status_code}")
