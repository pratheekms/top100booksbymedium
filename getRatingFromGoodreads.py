import bs4, requests
import lxml
import writeToExcel


def getRatingFromGoodreadsFunction(goodReadsUrl, i):
    print("---scrapping for rating start---")
    #print("url from get rating"+goodReadsUrl)
    # logger.info("---scrapping for rating start---")
    try:
        res = requests.get(goodReadsUrl, verify=False)
    except:
        res.raise_for_status()
        # break
        print("exception at get ratin fron goodreads")
        exit()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    ratingObj = soup.find("span", itemprop="ratingValue")
    try:
        rating = ratingObj.getText()
        print("rating in try "+rating)
        # print("ratinng of", bookname, bookauthor, rating)
        # call write ti excel
        print("calling write to excel from try")
        writeToExcel.writeToExcelFunction(i, 4, rating)


    except:
        rating = "Error"
        print("rating in exception " + rating)
        # print("ratinng of", bookname, bookauthor, rating)
        # call write to excel pass Error
        print("calling write to excel from exception")
        writeToExcel.writeToExcelFunction(i, 4, rating)


if __name__ == '__main__':
    print("unexpected calling")
