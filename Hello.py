import streamlit as st
import requests
from bs4 import BeautifulSoup

# Function to scrape news headlines
def scrape_news():
    url = "https://es.kiosko.net/ar/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = []

        # Assuming headlines are in <h2> tags, modify according to the website structure

        for headline in soup.find_all("div"):
            headlines.append(headline.text.strip())

        return headlines
    else:
        st.error("Failed to retrieve data from the website")
        return []

# Streamlit web app
def main():
    st.title("Simple News Scraper")

    # Trigger the scraping function
    if st.button("Scrape News"):
        st.text("Fetching news headlines...")
        headlines = scrape_news()

        # Display the scraped headlines
        if headlines:
            st.subheader("Latest News Headlines:")
            for i, headline in enumerate(headlines, start=1):
                st.write(f"{i}. {headline}")
        else:
            st.warning("No headlines found.")

if __name__ == "__main__":
    main()
