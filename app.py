from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests

# define target
target = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# define headers to avoid blocking from website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
# get page
page = requests.get(target, headers=headers)

# define page content
page_content = page.text


# Create script to interact with frontend
