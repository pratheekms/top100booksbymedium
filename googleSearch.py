
import getRatingFromGoodreads
import random
def googleSearchFunction(searchPhrase,i):
    print("------------rating process starts------------")

    # book name and book author details are saved to an excel file
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

        # call the sear query function
        for j in search(searchPhrase, tld="com", num=10, stop=1, pause=random.randint(1,3)):  # random.randint(1,3)):
            goodReadsUrl = j
        print("good reads URL is ", goodReadsUrl)
        getRatingFromGoodreads(goodReadsUrl,i)



if __name__ == '__main__':
    print("unexpected calling")
