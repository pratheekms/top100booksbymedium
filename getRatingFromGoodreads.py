import bs4, requests
import lxml
import  writeToExcel


def getRatingFromGoodreadsFunction(goodReadsUrl,i, null=None):
    print("---scrapping for rating start---")
    # logger.info("---scrapping for rating start---")
    try:
        res = requests.get(goodReadsUrl, verify=False)
    except:
        res.raise_for_status()
        # break
        exit()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    ratingObj = soup.find("span", itemprop="ratingValue")
    try:
        rating = ratingObj.getText()
        # print("ratinng of", bookname, bookauthor, rating)
        # call write ti excel
        writeToExcel.writeToExcelFunction(i,4,rating)

    except:
        rating = "Error"
        # print("ratinng of", bookname, bookauthor, rating)
        # call write to excel pass Error
        writeToExcel.writeToExcelFunction(i,4, rating)


if __name__ == '__main__':
    print("unexpected calling")
