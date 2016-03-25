#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
import csv
from bs4 import BeautifulSoup, NavigableString, Tag
from scraper import Scraper
import pycurl
from StringIO import StringIO
from urlparse import urlparse, urljoin
import stub6_html_doc as stub6

def get_html_doc(url):
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	body = buffer.getvalue()
	return body

def write_post_data_to_csv(post_data):
	with open('forum.csv', 'w') as f:
		writer = csv.writer(f, delimiter=';')
		for value in post_data:	
			writer.writerow(value)
		   #ALSO MUST SEE \n in strings instead of having them interpreted

if __name__ == "__main__":
	# cli arg
	base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&postdays=0&postorder=asc&start=75&sid=8616877ffa58d2fec112b34d94d82058' #page 6
	# base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'
	url = base_url
	# html_doc = get_html_doc(url)
	soup = BeautifulSoup(stub6.html_doc, 'html.parser')

	scraper = Scraper(soup, url)
	page_uris = scraper.get_all_page_uris()
	# print(page_uris)
	# exit()

	# # get post details on the first page
	print('\n\nGetting post data for url\n')
	print(url)
	post_data = scraper.get_post_data_per_page()
	write_post_data_to_csv(post_data)

	# then loop through all subsequent pages in the thread
	# for path in page_uris:
	# 	url = urljoin(base_url, path)
	# 	print('\n\nGetting post data for url\n')
	# 	print(url)
	# 	html_doc = get_html_doc(url)
	# 	soup = BeautifulSoup(html_doc, 'html.parser')
	# 	post_data = scraper.get_post_data_per_page()
	# 	write_post_data_to_csv(post_data)

	