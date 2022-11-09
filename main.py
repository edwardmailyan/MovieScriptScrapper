import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

all_movies_url = 'https://imsdb.com/all-scripts.html'
home_url = 'https://imsdb.com'
script_dict = {'title': [],
               'rating': [],
               'genres': [],
               'script': []}


def parse_movie_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    film_list = soup.find_all('table')[1].find('h1').parent
    return film_list.find_all('a')


def parse_script(url):
    link = home_url + url['href']
    response = requests.get(link)
    script_page = BeautifulSoup(response.content, 'html.parser')
    script = script_page.find_all('table')[1].find('td', {'class': 'scrtext'})
    script_dict['script'].append(script.get_text())


def parse_movie_info(urls):
    for i, a in enumerate(urls):
        link = home_url + a['href']
        response = requests.get(link)
        film_page = BeautifulSoup(response.content, 'html.parser')

        try:
            title = film_page.find_all('table')[1].find('h1').get_text().replace(', The Script', '').replace(' Script',
                                                                                                             '')

            rating = film_page.find(text='Average user rating').next.next.next.next.get_text()

            genres = film_page.find_all('table')[1].find(text='Genres').find_all_next('a', href=re.compile('genre'))
            genres = [x.get_text() for x in genres]

            script_link = film_page.find_all('table')[1].find_next('a',
                                                                   href=re.compile('/scripts/'),
                                                                   text=re.compile('Read'))
            if script_link:
                parse_script(script_link)
                script_dict['title'].append(title)
                script_dict['rating'].append(rating)
                script_dict['genres'].append(genres)

                print(f'{i + 1}. ',
                      title,
                      link.replace(' ', '%20').replace('\'', '%27').replace('(', '%28').replace(')', '%29'),
                      'Done...')
            else:
                print(f'{i + 1}. ', title, 'has no script.')

        except IndexError:
            print(f'{i + 1}. ', 'No data')


if __name__ == '__main__':
    links = parse_movie_links(all_movies_url)
    parse_movie_info(links)
    df = pd.DataFrame(script_dict)
    df.to_csv('scripts.csv.gz')
