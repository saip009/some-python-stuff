# https://www.jazzcinemas.com/

from bs4 import BeautifulSoup
import requests
import os
import time

url = 'https://www.jazzcinemas.com/'

movie_name = "CAPTAIN"

x = 1

while True:
    try:
        html = requests.get(url).text

        soup_11 = BeautifulSoup(html, "lxml")

        # xx = html_11.count(movie_name)
        # print 'x: ' + str(xx) + " occurrences"

        y = html.count(movie_name)
        print 'y: ' + str(y) + " occurrences"

        # if thu > 0 or fri > 0:
        # if xx>13 or y > 0:
        if y > 0:
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

