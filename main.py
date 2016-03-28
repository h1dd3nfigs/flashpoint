#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
import csv
from bs4 import BeautifulSoup, NavigableString, Tag
from scraper import Scraper
import pycurl
from StringIO import StringIO
from urlparse import urlparse, urljoin

def get_html_doc(url):
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	body = buffer.getvalue()
	return body

def write_post_data_to_csv(post_data, mode ='a'):
	with open('forum.csv', mode) as f:
		writer = csv.writer(f, delimiter=';')
		for value in post_data:	
			writer.writerow(value)

if __name__ == "__main__":
	base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'
	url = base_url
	html_doc = get_html_doc(url)
	soup = BeautifulSoup(html_doc, 'html5lib')
	scraper = Scraper(soup, url)

	# get the URIs for all pages in this forum thread
	page_uris = scraper.get_all_page_uris()
	
	# get post details on the first page
	post_data = scraper.get_post_data_per_page()
	write_post_data_to_csv(post_data, 'w')

	# then loop through all subsequent pages in the thread
	for path in page_uris:
		url = urljoin(base_url, path)
		html_doc = get_html_doc(url)
		soup = BeautifulSoup(html_doc, 'html5lib')
		post_data = scraper.get_post_data_per_page()
		write_post_data_to_csv(post_data)

	