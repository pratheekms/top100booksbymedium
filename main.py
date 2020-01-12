import time
import webScrapping
import listToNestedDict
import writeToExcelFromDict


def main():
    start = time.time()
    url = "https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
    # webScrapping.scrapingFunction(url, "strong", "id ke")
    extractedValueDict = webScrapping.scrapingFunction(url, "strong", "id ke")
    # dictToNestedDict.HtmlToDictFunction(webScrapping.scrapingFunction.extractedValueDict)
    bookNestedDict = listToNestedDict.listToDictFunction(extractedValueDict)
    writeToExcelFromDict.writeToExcelFunction(bookNestedDict)
    end = time.time()
    print("time taken by program is:" + str(end - start))


if __name__ == '__main__':
    main()
