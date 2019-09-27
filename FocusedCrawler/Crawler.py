import requests
from bs4 import BeautifulSoup
import re
import time
import os


def spider(seed_url):
    main = 'https://en.wikipedia.org/wiki/Main_Page'
    count_crawled = 0
    max_depth = 1
    frontier = [seed_url]
    discovered_urls = []

    path = r'Logs'
    if not os.path.exists(path):
        os.makedirs(path)

    c_log = open("Logs/crawler_log.txt", "w")
    c_log.write("Seed : " + seed_url + "\n\n")

    c_log.write("Depth 1 :\n\n")
    count_crawled += 1
    c_log.write(str(count_crawled) + ") " + seed_url + "\n\n")

    flag = True

    print("\nSeed_url: 1)" + seed_url)
    c_log.write("\nSeed_url: 1)" + seed_url)
    for depth in range(1, 6):
        if flag:
            print("\n----------------------------------------- At depth " + str(
                depth) + "--------------------------------------------------------")
            c_log.write("Depth " + str(depth) + " :\n\n")
            extracted_urls = []

            for frontier_url in frontier:

                if flag:

                    source = requests.get(frontier_url)
                    p_text = source.text
                    soup = BeautifulSoup(p_text, "html.parser")

                    for link in soup.find_all('a', href=re.compile('^/wiki/')):

                        if count_crawled < 1000 and flag:

                            h_url = link.get('href')

                            if ':' not in h_url:

                                if '#' not in h_url:
                                    url = 'https://en.wikipedia.org' + h_url

                                    if url not in frontier and url not in extracted_urls and url not in discovered_urls and url != main:
                                        time.sleep(1)
                                        extracted_urls.append(url)
                                        count_crawled += 1
                                        c_log.write(str(count_crawled) + ") " + url + "\n")
                                        print(str(count_crawled) + ") " + url)

                                else:

                                    hash_pos = h_url.index('#')
                                    url = 'https://en.wikipedia.org' + h_url[:hash_pos]
                                    if url not in frontier and url not in extracted_urls and url not in discovered_urls and url != main:
                                        time.sleep(1)
                                        extracted_urls.append(url)
                                        count_crawled += 1
                                        c_log.write(str(count_crawled) + ") " + url + "\n")
                                        print(str(count_crawled) + ") " + url)


                        else:

                            flag = False
                            print("Limit of 1000 URLs reached")
                            max_depth = depth
                            break

                    discovered_urls.append(frontier_url)

            if len(extracted_urls) == 0:
                print("No matching URLs at Depth " + str(depth) + "\n")
                c_log.write("No matching URLs at Depth " + str(depth) + "\n\n")
                flag = False
                max_depth = depth
                break

            frontier = extracted_urls
            c_log.write("\n")

    if flag:
        print("Searched till max depth 5")
        max_depth = 6

    c_log.write("------------------------------------------------------------------------------------\n")
    c_log.write("Logistics :\n\n")
    c_log.write("Number of matching searches : " + str(count_crawled) + "\n")
    c_log.write("Maximum depth reached : Depth " + str(max_depth) + "\n")


def initiate(seed):
    seed_url = seed
    spider(seed_url)
