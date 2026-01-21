import random
import time
def getrandomdate(startdate, enddate):
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'
    starttime = time.mktime(time.strptime(startdate, dateFormat))
    endtime = time.mktime(time.strptime(enddate, dateFormat))
    randomtime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomdate
print("Random date = ", getrandomdate("1/1/1985", "21/1/1990"))
#print("Random date = ", getrandomdate("DD/MM/YYYY", "DD/MM/YYYY"))