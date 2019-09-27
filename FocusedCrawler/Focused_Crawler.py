import requests
from bs4 import BeautifulSoup
import re
import time
import os


def setDirectory():
    path = r'Logs'
    if not os.path.exists(path):
        os.makedirs(path)


def check_keyphrase(soup_obj, keyphrase):
    if soup_obj.find_all(text=re.compile('(?i)' + keyphrase)):
        return True
    else:
        return False


def spider(seed_url, keyword):
    frontier = [seed_url]
    discovered_urls = []
    main = 'https://en.wikipedia.org/wiki/Main_Page'

    max_depth = 1

    fc_log = open("Logs/fc_log.txt", "w")
    fc_log.write("Seed : " + seed_url + "\n")
    fc_log.write("Keyword : " + keyword + "\n\n")

    fc_log.write("Depth 1 :\n\n")
    count_crawled = 1
    fc_log.write(str(count_crawled) + ") " + seed_url + "\n\n")

    flag = True

    for depth in range(1, 6):
        if flag:
            print("\n----------------------------------------- At depth " + str(
                depth) + "--------------------------------------------------------")
            fc_log.write("Depth " + str(depth) + " :\n\n")
            new_urls = []


            for frontier_url in frontier:


                if flag:

                    time.sleep(1)
                    source_code = requests.get(frontier_url)
                    plain_text = source_code.text
                    soup = BeautifulSoup(plain_text, "html.parser")
                    count_crawled += 1

                    # Check relevance
                    if check_keyphrase(soup, keyword):

                        print(frontier_url)
                        print("\n")
                        fc_log.write(frontier_url)
                        fc_log.write("\n")


                        for link in soup.find_all('a', href=re.compile('^/wiki/')):


                            if count_crawled < 1000 and flag:

                                h_url = link.get('href')

                                if ':' not in h_url:

                                    if '#' not in h_url:
                                        url = 'https://en.wikipedia.org' + h_url

                                        if url not in frontier and url not in new_urls and url not in discovered_urls and url != main:
                                            new_urls.append(url)



                                    else:
                                        # Handle URLs with '#'
                                        hash_pos = h_url.index('#')


                                        url = 'https://en.wikipedia.org' + h_url[:hash_pos]


                                        if url not in frontier and url not in new_urls and url not in discovered_urls and url != main:
                                            new_urls.append(url)

                            else:

                                flag = False
                                print("Limit of 1000 URLs reached")
                                max_depth = depth
                                break

                        discovered_urls.append(frontier_url)

            if len(new_urls) == 0:
                print("No matching URLs at Depth " + str(depth) + "\n")
                fc_log.write("No matching URLs at Depth " + str(depth) + "\n\n")
                flag = False
                max_depth = depth
                break

            frontier = new_urls
            fc_log.write("\n")

    if flag:
        print("Searched till max depth 5")
        max_depth = 6

    print("------------------------------------------------------------------------------------\n")
    print("Logistics :\n\n")
    print("Number of crawls : " + str(count_crawled) + "\n")
    print("Maximum depth reached : Depth " + str(max_depth) + "\n")
    fc_log.write("------------------------------------------------------------------------------------\n")
    fc_log.write("Logistics :\n\n")
    fc_log.write("Number of crawls : " + str(count_crawled) + "\n")
    fc_log.write("Maximum depth reached : Depth " + str(max_depth) + "\n")


def initiate(seed, key):
    seed_url = seed
    keyword = key
    setDirectory()
    spider(seed_url, keyword)
