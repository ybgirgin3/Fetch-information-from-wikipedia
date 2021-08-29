#!/usr/bin/env python
# coding: utf-8


from bs4 import BeautifulSoup as BS
from urllib.parse import urlparse
from urllib.request import urlopen
import requests
import sys
import os


def get_links(link: str, query: str) -> list:
    all_fetched_links = []
    webpage = requests.get(f"{link}/wiki/Category:{query}")

    soup = BS(webpage.content, "html.parser")
    if not soup:
        return False
    else:
        # find div
        # find ul in div
        # find li in ul
        for links in soup.find_all("div", {"class": "mw-content-ltr"}):
            for ul in links.find_all("ul"):
                for li in ul.find_all("li"):
                    for a in li.find_all("a"):
                        # if not a['href'].startswith('https://'):
                        # print(a['href'])
                        if not a["href"].startswith("https://"):
                            all_fetched_links.append(a["href"])
                        else:
                            pass

        return all_fetched_links


def control(fn):
    if os.path.isfile(fn) and os.access(fn, os.R_OK):
        return True
    else:
        return False


def look_for_file(fn):
    # fn = f"sub/{filename}.txt"
    if control(fn):
        ask = str(input(f"file is exists do you want to override? {fn} [Y/n]: "))
        if ask in ("Y", "y"):
            os.remove(fn)
            return fn

        elif ask in ("N", "n"):
            print("stopped..")
            sys.exit(1)


def write_to_file(web_source: str, subdir: str, q: str, data: list) -> None:
    # if file exist ask user
    # parse main url
    webpage = urlparse(web_source)
    url = f"{webpage[0]}://{webpage[1]}"

    # fn = look_for_file(f"sub/{q}.txt")
    fn = f"{os.path.join(subdir, q)}.txt"
    look_for_file(fn)
    print(fn)

    with open(str(fn), "w") as f:
        for link in data:
            f.write(f"{url}/{link}\n")
        print("done.. 👍🏻")


def get_text(src: str) -> list:
    if control(src):
        with open(src, "r") as f:
            return f.readlines()
    else:
        print(f"file not exists {fn}")


def get_information(urls: list, info_dir: str) -> None:
    look_for_file(info_dir)

    for url in urls:
        if "Category" not in url:
            # fn = url.split('/')[-1]
            html = urlopen(url).read()
            soup = BS(html, features="html.parser")
            page = soup.find("p").get_text()
            # print(page)
            with open(f"{info_dir}", "a") as f:
                f.write("{}\n".format("-" * 40))
                f.write(f"{page}")


if __name__ == "__main__":
    # variables
    # q = "Spanish brands"
    q = sys.argv[1]
    sub_dir = os.path.join("sub", f"{q}.txt")
    info_dir = os.path.join("info", f"{q}_info.txt")
    link = "https://en.wikipedia.org"
    # get url list
    url_list = get_links(link, q)
    # write to file
    write_to_file(link, "sub", q, url_list)
    sub_list = get_text(sub_dir)
    get_information(sub_list, info_dir)
