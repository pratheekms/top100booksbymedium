import openpyxl


def writeToTxtFileFunction(slno, bookName, authorName):
    f = open("top100BooksByMedium.txt", "a")
    f.write(str(slno) + '\t' + str(bookName) + '\t' + authorName + '\n')
    f.close()


if __name__ == '__main__':
    print("unexpected calling")
