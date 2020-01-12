import time
import scrapeAndFormatData
import smsService
import emailService

def main():
    start = time.time()
    #calling scraping function and formating extracted data
    scrapeAndFormatData.scrapeAndFormatDataFunction()
    #calling sms service
    smsService.smsServiceFunction()

    #calling email service
    emailService.emailServiceFunction()


    end = time.time()
    print("time taken by program is:"+str(end - start))
if __name__=='__main__':
    main()