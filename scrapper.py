from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome( )
browser.get(START_URL)

time.sleep(10)

response = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
