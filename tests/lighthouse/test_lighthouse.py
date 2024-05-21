import subprocess


def test_run_lighthouse():
    urls = [
        "https://www.moskvaonline.ru/providers",
        "https://www.moskvaonline.ru/",
        "https://www.moskvaonline.ru/rating"
    ]
    for url in urls:
        output_path = f"{url.replace('://', '_').replace('/', '_')}.html"
        cmd = f'lighthouse {url} --output=html --quiet --output-path={output_path}'
        result = subprocess.run(cmd, shell=True)

        if result.returncode == 0:
            print(f"Lighthouse report for {url} saved to: {output_path}")
        else:
            print(f"An error occurred while running Lighthouse for {url}.")


