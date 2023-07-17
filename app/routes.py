from cgitb import text
from bs4 import BeautifulSoup
import requests
from markupsafe import escape
from flask import jsonify
from app import app
from cryptography.fernet import Fernet

domain = "https://dramacool.cr"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/517.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/517.36"} 


f = Fernet(b'u6XOwSZ7JZvr8ibrixGZY6rBsrTMG4gD-GTlIl39Eq0=')
@app.route('/')
def index():
    response = requests.get(f"{domain}", headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
   
    data = []
    trending_soup =  soup.select("ul.switch-block.list-episode-item li")[0:50]
   
    print(type(data))
    return jsonify({"links":list_scraper(trending_soup)})

def encryptor(text):
    temp_bytes = f.encrypt(text.encode())
    bytes_to_string = temp_bytes.decode("utf-8")
    return bytes_to_string

def list_scraper(list):
    temp_list = []
    for  l in list:
        image = l.select_one("a > img")["data-original"]
        # format the link by altering image link 
        # https://imagecdn.me/cover/the-real-deal-has-come-1679286638.png
        final_image = image.replace(f'https://imagecdn.me/cover/',"").split("-")[:-1]

        link = "drama-detail/"+("-").join(final_image)
        title = l.select_one("a > h3").text.strip()
        episode = l.select_one("a > span.ep").text.strip()

        temp_list.append({
            "link": link,
            "image":image,
            "title": title,
            "episode": episode.lower()
        })


    return temp_list