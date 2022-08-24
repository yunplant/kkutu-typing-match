
import pyautogui as pag
import pygetwindow as gw
from jamo import h2j, j2hcj
from selenium import webdriver
from bs4 import BeautifulSoup

cons = {'ㄱ': 'r', 'ㄲ': 'R', 'ㄴ': 's', 'ㄷ': 'e', 'ㄸ': 'E', 'ㄹ': 'f', 'ㅁ': 'a', 'ㅂ': 'q', 'ㅃ': 'Q', 'ㅅ': 't', 'ㅆ': 'T', 'ㅇ': 'd', 'ㅈ': 'w', 'ㅉ': 'W', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅍ': 'v', 'ㅎ': 'g','ㅏ': 'k', 'ㅐ': 'o', 'ㅑ': 'i', 'ㅒ': 'O', 'ㅓ': 'j', 'ㅔ': 'p', 'ㅕ': 'u', 'ㅖ': 'P', 'ㅗ': 'h', 'ㅘ': 'hk', 'ㅙ': 'ho', 'ㅚ': 'hl', 'ㅛ': 'y', 'ㅜ': 'n', 'ㅝ': 'nj', 'ㅞ': 'np', 'ㅟ': 'nl', 'ㅠ': 'b', 'ㅡ': 'm', 'ㅢ': 'ml', 'ㅣ': 'l','ㄳ': 'rt', 'ㄵ': 'sw', 'ㄶ': 'sg', 'ㄺ': 'fr', 'ㄻ': 'fa', 'ㄼ': 'fq', 'ㄽ': 'ft', 'ㄾ': 'fx', 'ㄿ': 'fv', 'ㅀ': 'fg', 'ㅄ': 'qt','1': '1', '2' : '2', '3' : '3', '4' : '4', '5' : '5', '6' : '6', '7' : '7', '8' : '8', '9' : '9', '0' : '0'}

def search() :
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    posts = soup.find("div", attrs={"class":"jjo-display ellipse"})
    posts_ = posts.get_text()
    posts__ = posts_.split(' ')
    word1 = posts__[0]
    word2 = posts__[1]
    return word1

def time():
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    posts = soup.find("div", attrs={"class": "graph jjo-round-time"})
    posts_ = posts.get_text()
    posts__ = posts_.split('.')
    posts___ = int(posts__[0])
    return posts___

driver = webdriver.Chrome('chromedriver')
url = 'https://kkutu.co.kr/'
driver.get(url)
a = input()

pag.press('hangul')

while True :
    b = search()
    bb = time()
    if bb > 1 :
        sample_text = b
        text = j2hcj(h2j(sample_text))
        retype = ""
        for i in range(len(text)):
            retype = retype + cons[text[i]]
        pag.write(retype,interval=0.01)
        pag.press('enter')
    else :
        pass

