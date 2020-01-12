extractedValueDict = []

bookNestedDict = {}


def HtmlToDictFunction(ExtractedHTML):
    extractedValueCount = 1
    print("extracting data into dict start")

    for i in range(0, len(ExtractedHTML) - 4):
        if len(ExtractedHTML[i].getText()) > 2:
            extractedValueDict.append(ExtractedHTML[i].getText())
            print(ExtractedHTML[i].getText())

    for i in extractedValueDict:
        print("book " + str(extractedValueCount) + i)

        print(len(extractedValueDict[extractedValueCount - 1]))

        bookNestedDict.update({extractedValueCount: {'name': i.split(' by ')[0], 'author': i.split(' by ')[1]}})
        extractedValueCount += 1
    print("extracted value count"+extractedValueCount)


if __name__ == '__main__':
    print("unexpected calling")
