#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
import pycurl
from StringIO import StringIO
from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin
import stub_html_doc as stub

# Write a scraper using Python 3 (ideally, or 2.7 optionally),
# Pycurl and BeautifulSoup (bs4) to be used to collect all posts from all the pages of this thread in this forum: 
# http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591

# Required fields are: post id, name, date of the post (in text form or as is) and post body.

# Output the results to a text file named forum.csv

# An example of a single post in that file should look like the following:

# 87120;"Rick";"Mon Sep 24, 2012 4:53 pm";"Tonight, 8pm, might be worth a look...?\n\nRJ"


def get_html_doc(url):
	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	body = buffer.getvalue()
	return body

# Get the URIs for all pages in this forum thread, 
# DOM Location: All <a> descendants of the first <span class="gensmall">

def get_all_page_uris(soup):
	page_uris = set()
	span_tag = soup.find("span", class_="gensmall")

	for a_tags in span_tag.find_all("a"):
		page_uris.add( a_tags.get('href'))

	return page_uris

if __name__ == "__main__":
	base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'
	# html_doc = get_html_doc(base_url)
	soup = BeautifulSoup(stub.html_doc, 'html.parser')
	page_uris = get_all_page_uris(soup)
	# print(page_uris)
	
	# after getting post authors on first page
	# visit each other url and get the authors on those pages
	# foreach url get all names of post authors
	for path in page_uris:
		url = urljoin(base_url, path)

