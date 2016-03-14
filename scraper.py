#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
import csv
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

	for a_tag in span_tag.find_all("a"):
		page_uris.add( a_tag.get('href'))

	return page_uris

#
# Get the all post ids on this page
# DOM Location: 	<table class="forumline">
# 						<span class="name"> 
#							<a name={post_id}> 
#
def get_post_ids(soup):
	post_ids = []
	table_tag = soup.find("table", class_="forumline")

	for span_tag in table_tag.find_all("span", class_="name"):
		a_tag = span_tag.find('a')
		post_id = a_tag.get('name')
		post_ids.append(post_id)
		
	return post_ids

#
# Get the all post authors on this page
# DOM Location: 	<table class="forumline">
# 						<span class="name"> 
#							<b>{post_author}</b>
#
def get_post_authors(soup):
	post_authors = []
	table_tag = soup.find("table", class_="forumline")

	for span_tag in table_tag.find_all("span", class_="name"):
		b_tag = span_tag.find('b')
		post_author = b_tag.text
		post_authors.append(post_author)
		# CONVERT FROM UNICODE TO ASCII so chars in foreign names show up right 

	return post_authors

#
# Get the all post dates on this page
# DOM Location: 	<table class="forumline">
# 						<span class="postdetails">"Posted: {post_date}				
#
def get_post_dates(soup):
	post_dates = []
	date_prefix = 'Posted: '
	table_tag = soup.find("table", class_="forumline")

	for span_tag in table_tag.find_all("span", class_="postdetails"):
		if date_prefix in span_tag.contents[0]:
			post_dates.append(span_tag.contents[0].lstrip(date_prefix))

	return post_dates

#
# Get the all post bodies on this page
# DOM Location: 	<table class="forumline">
# 						<span class="postbody">{post_body}<br />_________________				
#
def get_post_bodies(soup):
	post_bodies = []
	date_prefix = 'Posted: '
	table_tag = soup.find("table", class_="forumline")

	for span_tag in table_tag.find_all("span", class_="postbody"):
		body = unicode('')
		for text in span_tag.contents:
			if text == '_________________':
				break
			else:
				body += unicode.join(u'',text)
				# CONVERT FROM UNICODE TO ASCII so chars like the currency symbol show up right "£30k?" 
		post_bodies.append(body.encode('utf8'))


	return post_bodies

def get_post_data_per_page(soup):
	post_ids = get_post_ids(soup)
	post_authors = get_post_authors(soup)
	post_dates = get_post_dates(soup)
	post_bodies = get_post_bodies(soup)
	post_data = zip(post_ids, post_authors, post_dates, post_bodies)
	return post_data

def write_post_data_to_csv(post_data):
	writer = csv.writer(open('forum.csv', 'a'))#, quoting=csv.QUOTE_MINIMAL)
	for value in post_data:
	   writer.writerow(value)
	   #MUST BE SEMICOLON SEPARATED STRING instead of unicode string tuples on each row
	   #ALSO MUST SEE \n in strings instead of having them interpreted

if __name__ == "__main__":
	base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'
	url = base_url
	html_doc = get_html_doc(url)
	soup = BeautifulSoup(html_doc, 'html.parser')
	page_uris = get_all_page_uris(soup)


	# get post detils on the first page
	print('\n\nGetting post data for url\n')
	print(url)
	post_data = get_post_data_per_page(soup)
	write_post_data_to_csv(post_data)

	# then loop through all subsequent pages in the thread
	for path in page_uris:
		url = urljoin(base_url, path)
		print('\n\nGetting post data for url\n')
		print(url)
		html_doc = get_html_doc(url)
		soup = BeautifulSoup(html_doc, 'html.parser')
		post_data = get_post_data_per_page(soup)
		write_post_data_to_csv(post_data)

	