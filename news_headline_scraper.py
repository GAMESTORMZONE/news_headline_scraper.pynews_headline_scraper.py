import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://www.bbc.com/news"):
    try:
        
        response = requests.get(url)
        response.raise_for_status()  # Hiba dobása rossz státuszkód esetén

        
        soup = BeautifulSoup(response.text, 'html.parser')

        
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        print("Top hírek:")

        
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline.text.strip()}")
    except requests.exceptions.RequestException as e:
        print(f"Hiba az adatok lekérésekor: {e}")

if __name__ == "__main__":
    fetch_headlines()
