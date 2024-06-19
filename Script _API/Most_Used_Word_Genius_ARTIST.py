# This script will sort the artist's most popular words
import requests
from bs4 import BeautifulSoup
from collections import Counter
from pprint import pprint


def get_all_urls() -> list:
    # Declare the variables
    next_page = ''
    page = 1
    links = []
    artist_code = "385596"
    while next_page is not None:
        # -API-
        api_link = requests.get(f"https://genius.com/api/artists/{artist_code}/songs?page={page}&sort=popularity")
        # Check the answer
        if api_link.status_code == 200:
            # Get keys in json file
            response = api_link.json().get("response")
            next_page = response.get("next_page")
            songs = response.get("songs")
            # Configure the loader
            print(f"Page Number : {page}")
            page += 1
            # Add all link in a list
            links.extend([song.get('url') for song in songs])
        # Configure with code for HTTP response
        else:
            print(f"Page -> We have an error : {api_link.status_code}")

    return links


def extract_word(urls):
    # Declare the variables
    all_words = []
    load = 1
    # Extract link 1 by 1
    for url in urls:
        link = requests.get(url)
        # Check the answer
        if link.status_code == 200:
            # Scrap the HTML code
            soup = BeautifulSoup(link.content, 'html.parser')
            # Take lyrics with class name
            lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
            # Configure de loader
            print(f"Song analysis : {load}")
            load += 1
            # Extract all word and sort
            try:
                # Clean HTML
                for sentence in lyrics.stripped_strings:
                    # Extract word by word
                    for word in sentence.split(" "):
                        # Add condition for sort words
                        if len(word) > 4 and '[' not in word and ']' not in word:
                            sort_word = word.strip(':').strip('.').strip(',').lower().split("\n")
                            # Input all sort word in a single list
                            [all_words.append(word) for word in sort_word]
            # Configure an error for no lyrics
            except AttributeError:
                print("No Lyrics")
        # Configure an error with code for HTTP response
        else:
            print(f"Song Link -> We have an error : {link.status_code}")
    # Count and class most used word in lyrics
    counter = Counter(all_words)
    pprint(counter.most_common(100))


links = get_all_urls()
extract_word(links)
