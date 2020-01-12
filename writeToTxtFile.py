
def writeToTxtFileFunction(bookNestedDict):

    for bn, ba in bookNestedDict.items():
        print("book num", bn)

        col1 = bn  # booknum
        for key in ba:
            print(key + ":", ba[key])

            col2 = ba['name']  # bookname
            col3 = ba['author']  # bookauthor
            f = open("top100BooksByMedium.txt", "a")
            f.write(str(col1) + '\t' + str(col2) + '\t' + col2 + '\n')
            f.close()


if __name__ == '__main__':
    print("unexpected calling")
