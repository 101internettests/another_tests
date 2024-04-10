import requests

urls_to_check = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.github.com"
    ]


class TestUrl:
    def test_check_url_response(self):
        for url in urls_to_check:
            try:
                response = requests.get(url)
                print(f"Response code for {url}: {response.status_code}")
                if response.status_code == 502:
                    print("502 Bad Gateway error detected!")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while checking {url}: {e}")


