import bs4, requests

finalResultDict = {}


def scrapingFunction(urlName, tagName, className):
    print("scraping web for top 100 books start")

    #url = "https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
    res = requests.get(url, verify=False)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # slno=soup.find_all("a",attrs={"class":"fi cn hx hy hz ia"})
    #bookAndAuthors = soup.find_all("strong", attrs={"class": "id ke"})
    ExtractedHTML = soup.find_all(tagName, attrs={"class": className})


if __name__ == '__main__':
    print("unexpected calling")


