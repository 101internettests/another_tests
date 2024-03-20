import requests
from links.urls import links, links_urls
from links.urls import first_links, second_links
from links.urls import first_urls, second_urls
from links.urls import first_one_urls, second_two_urls

if __name__ == '__main__':
    for link, redirect_url in zip(first_one_urls, second_two_urls):
        try:
            r = requests.get(link)
            assert r.url == redirect_url, f'{link}'
            print(f'Redirection occurred successfully for link: {link}')
            print(r.history[0].status_code)
            # print(r.url)
        except AssertionError as e:
            print(e)
        except requests.RequestException as e:
            print(f'Error accessing {link}: {e}')