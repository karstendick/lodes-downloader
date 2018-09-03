import requests
from bs4 import BeautifulSoup
import wget

# subdirectories = ['rac', 'wac', 'od']
PA_ROOT = 'https://lehd.ces.census.gov/data/lodes/LODES7/pa/wac/'

def main():
    pa_root_response = requests.get(PA_ROOT)

    pa_root_html = pa_root_response.text


    soup = BeautifulSoup(pa_root_html, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if 'csv' in href:
            print(PA_ROOT+href)
            wget.download(PA_ROOT+href, out='data/')



if __name__ == "__main__":
    main()
