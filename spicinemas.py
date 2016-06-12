from bs4 import BeautifulSoup
import requests
import os
import time

url_11 = 'https://www.spicinemas.in/chennai/show-times/24-03-2016?seats=2'
url_12 = 'https://www.spicinemas.in/chennai/show-times/25-03-2016?seats=2'

movie_name = "BATMAN"

x = 1
y = fri = thu = 0

while True:
    try:
        html_11 = requests.get(url_11).text
        html_12 = requests.get(url_12).text

        soup_11 = BeautifulSoup(html_11, "lxml")
        soup_12 = BeautifulSoup(html_12, "lxml")

        if movie_name in html_11:
            thu += 1

        if movie_name in html_12:
            fri += 1

        # xx = html_11.count(movie_name)
        # print 'x: ' + str(xx) + " occurrences"

        y = html_12.count(movie_name)
        print 'y: ' + str(y) + " occurrences"

        # if thu > 0 or fri > 0:
        # if xx>13 or y > 0:
        if y > 25:
            print "Attempt " + str(x) + ": BOOK IT QUICK!"
            # print thu
            # print fri
            # print len(thu)
            # print len(fri)
            # print "        " + y + " occurrences"
            for z in range(10):
                os.system("start ./starwars.mp3")
                time.sleep(70)

        else:
            print "Attempt " + str(x) + ": GOTTA WAIT MORE "
            # print "        " + y + " occurrences"

    except:
        pass

    x += 1
    time.sleep(30)

