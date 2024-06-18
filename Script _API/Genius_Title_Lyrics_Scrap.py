import requests
from bs4 import BeautifulSoup

# Go find all links
def get_all_urls():
    # Declaration of variables
    next_page = ''
    page_number = 1
    links = []
    while next_page is not None:
        # retrieve API response if it returns 200
        r = requests.get(f"https://genius.com/api/artists/1581/songs?page={page_number}&sort=popularity")
        if r.status_code != 200:
            print("We have problem with the URL")
            return
        # get the answer and the index of the page
        response = r.json().get("response", {})
        next_page = response.get("next_page")
        # get all the links relating to music
        songs = response.get("songs")
        links.extend([song.get("url") for song in songs])
        # indent page number
        page_number += 1
        # To display only one page I configured None (Total page 36)
        next_page = None

    print("no more page")
    # return the list
    return links


def extract_lyrics(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("Page Not Found 404")
        return []

    soup = BeautifulSoup(r.content, 'html.parser')
    lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
    title_song = soup.find("span", class_="SongHeaderdesktop__HiddenMask-sc-1effuo1-11 iMpFIj")
    if not lyrics:
        return extract_lyrics(url)

    title = "No title found"
    if title_song:
        title = " ".join([t for t in title_song.stripped_strings])

    lyrics_text = "\n".join([sentence for sentence in lyrics.stripped_strings])

    result = {
        "title": title,
        "lyrics": lyrics_text
    }
    return result

    # [print(f"***{title}***\n") for title in title_song.stripped_strings]
    # [print(sentence) for sentence in lyrics.stripped_strings]
    # print(f"{75 * '-'}\n")


links = get_all_urls()
for url in links:
    result = extract_lyrics(url)
    if result:
        print(f"***{result['title']}***\n")
        print(result['lyrics'])
        print(f"\n{75 * '-'}\n")
