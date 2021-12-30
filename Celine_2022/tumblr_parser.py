from bs4 import BeautifulSoup
import requests
import json

api_key = "2oPju6MZxsjf7SEmBAhZknZg61GSsLKZSP526UQzHPdXGdda5b"
tumblr_url = "lookifoundacute.tumblr.com"
url = f"https://api.tumblr.com/v2/blog/{tumblr_url}/posts/photo?api_key={api_key}"

photo_urls = []

while True:
    page = requests.get(url)
    json_reply = json.loads(page.content)

    page_posts = json_reply["response"]["posts"]
    for post in page_posts:
        post_type = post["type"]
        if "text" in post_type:
            continue
        if "photo" in post_type:
            post_photos = post["photos"]
            for photo in post_photos:
                photo_urls.append(photo["original_size"]["url"])
    try:
        next_url = json_reply["response"]["_links"]["next"]["href"]
        url = f"https://api.tumblr.com{next_url}&api_key={api_key}"
    except KeyError:
        print("pics = [\""+'",\n"'.join(photo_urls)+"\"];")
        exit()
    # print(len(photo_urls))
    # a= input()
    # if "stop" in a:
    # if len(photo_urls)>1000:
    #     print("pics = [\""+'",\n"'.join(photo_urls)+"\"];")
    #     exit()