# Focused_Crawler
This python based application crawls through the given seed web page and extracts relevant links from the source code.
The relavance can be determined by giving a keyphrase as input to the crawler. The crawler will check whether that keyphrase is 
present in a particular page or not. 

You can also do a full crawl instead of a focused crawl. That meas you don't need to find relevant pages but all the URLs that are
present in the crawled pages.

Libraries used : requests, bs4


Setup:
-----

-> You need to have 'Beautiful Soup' and 'Requests' libraries installed, along with Python3 
   to run the code.

-> 'If' the initial file is a zip file, unzip the file first in a folder.

-> There are three files 'Crawler.py', 'Focused_Crawler.py' and 'Crawler_Main.py' (and the 'logs' folder containing the URLs):
	1) Crawler.py is the non-focused crawler
	2) Focused_Crawler.py is the focused crawler 
	3) Crawler_Main.py is used to initialize the one of the crawlers

-> Make sure that you keep all this three files in the same folder.

-> To start the crawlling, just enter the following command in your Command Prompt or PowerShell:

	" python Crawler_Main.py "

-> Now, simply follow the instructions on the screen.

-> The URLs crawled will be stored in text files in a seperate folder called 'logs'.
