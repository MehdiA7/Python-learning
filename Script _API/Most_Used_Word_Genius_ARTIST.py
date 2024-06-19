# This script will sort the artist's most popular words
import requests
from bs4 import BeautifulSoup
from collections import Counter
from pprint import pprint


def get_all_urls() -> list:
    next_page = ''
    page = 1
    links = []
    while next_page != None:
        api_link = requests.get(f"https://genius.com/api/artists/14693/songs?page={page}&sort=popularity")
        if api_link.status_code == 200:
            response = api_link.json().get("response")
            next_page = response.get("next_page")
            songs = response.get("songs")
            print(f"Page Number : {page}")
            page += 1
            links.extend([song.get('url') for song in songs])
        else:
            print(f"Page -> We have an error : {api_link.status_code}")
    return links


def extract_word(urls):
    all_words = []
    load = 1
    for url in urls:
        link = requests.get(url)
        if link.status_code == 200:
            soup = BeautifulSoup(link.content, 'html.parser')
            lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
            print(f"Song analysis : {load}")
            load += 1
            try:
                for sentence in lyrics.stripped_strings:
                    for word in sentence.split(" "):
                        if len(word) > 4 and '[' not in word and ']' not in word:
                            sort_word = word.strip(':').strip('.').strip(',').lower().split("\n")
                            [all_words.append(word) for word in sort_word]
            except AttributeError:
                print("Not a song")
        else:
            print(f"Song Link -> We have an error : {link.status_code}")
    counter = Counter(all_words)
    pprint(counter.most_common(100))


links = get_all_urls()
extract_word(links)
