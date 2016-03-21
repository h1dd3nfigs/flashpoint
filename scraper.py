#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
import csv
import pycurl
from StringIO import StringIO
from bs4 import BeautifulSoup, NavigableString, Tag
from urlparse import urlparse, urljoin
import stub_html_doc as stub
import stub5_html_doc as stub5
import stub3_html_doc as stub3

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
# Get all post dates on this page
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
# Get all post bodies on this page
# DOM Location for regular post: 	
# <table class="forumline">
# 	<span class="postbody">{post_body}<br />_________________				
						
# 	 		 OR
# DOM Location for quoted post nested in a post: 	
# <span class=postbody></span>
# <table><tr><td>
# 	<span class="genmed">{quoted author}</span>
# 	<td class="quote">{quoted body}</td>
# 	</td></tr>
# </table>
# <span class="postbody">{postbody}<br />_________________

def get_quoted_post(span_tag, author='', nesting_level = 1):
	
	print('\nRUNNIN MY RECURSIVE FUNCTION\n')
	
	sibling_table = span_tag.find_next('table').find('td', class_='quote')

	author += span_tag.find_next('table').find('span', class_='genmed').text + ' ['
	
	if sibling_table.contents == []:
		nesting_level += 1
		print('yuck')		
		return get_quoted_post(sibling_table, author, nesting_level)

	else:
		quote_body = author
		quote_pieces = sibling_table.contents
		if len(quote_pieces)  > 1:
			for q in quote_pieces:
				if not isinstance(quote_pieces,Tag):
					quote_body += unicode.join(u'', q)

		elif len(quote_pieces) == 1:
			quote_body += quote_pieces[0]
		else:
			pass


		return [nesting_level, quote_body + ']']


def get_post_bodies(soup):
	post_bodies = []
	date_prefix = 'Posted: '
	table_tag = soup.find("table", class_="forumline")

	nesting_level = 0
	print('the number of <span class=postbody> are \n')
	print(len(table_tag.find_all("span", class_="postbody")))
	exit()
	for span_tag in table_tag.find_all("span", class_="postbody"):
		# nesting_level of 0 means this post text does NOT have any quoted posts nested within it
		# nesting_level of 1 means there's 1 quoted post nested in this post's text
		# nesting_level of 2 means there are 2 quotes nested in this post's text, etc.

		if nesting_level > 0:
			is_quote_post = True 
		else: 
			is_quote_post = False

		# if we're not looping grabbing post_body text for nested quotes, start a new string for a new post
		if not is_quote_post:
			body = unicode('', encoding ='utf-8')

		if span_tag.contents == []: 			
			#then the <span class="postbody"> is empty so it's prob a quoted post, so get the quote author
			# which is this span's sibling table.tr.td.span[class="genmed"]
				# is_quote_post = True 
				# body = unicode('', encoding ='utf-8')

			nesting_level, quote_body = get_quoted_post(span_tag)

			body += quote_body

			print('\n.BEFORE..nesting level is {0}\n'.format(nesting_level))
			
			if nesting_level != 0:
				nesting_level -= 1

			print('\nAFTER...nesting level is {0}\n'.format(nesting_level))

		else:

			# it's not a quoted post so put the postbody contents into a new post body's string
			print('\n.BEFORE..nesting level is {0}\n'.format(nesting_level))
			
			if nesting_level != 0:
				nesting_level -= 1

			print('\nAFTER...nesting level is {0}\n'.format(nesting_level))

			for text in span_tag.contents:

				if text == '_________________':
					# the underscore marks the end of a post body if the author ends posts with a signature
					# is_quote_post = False
					break
				
				else:

					if isinstance(text, NavigableString):
						body += text
				
					elif isinstance(text,Tag):
						# this Tag is prob a <br/> tag so ignore it
						# print('we got an empty tag')
						# print(text)
						body += str(text)

						pass

					else:
						body += unicode.join(u'',text)
			
			#endfor
		# print('\nNEW post body\n')
		# print(body.encode('utf-8'))
		post_bodies.append(body.encode('utf-8'))
		
		# is_quote_post = False
		print(post_bodies)

	return post_bodies

def get_post_data_per_page(soup):
	post_ids = get_post_ids(soup)
	post_authors = get_post_authors(soup)
	post_dates = get_post_dates(soup)
	post_bodies = get_post_bodies(soup)
	print("num of post dates is {0} and num post bodies is {1}".format(len(post_dates),len(post_bodies)))
	# print(post_ids)
	# print(post_authors)
	# print(post_bodies)

	# exit()
	# print('post_bodies list BEFORE decoding into unicode:\n')
	# print(post_bodies)
	# print('post_bodies list AFTER decoding into unicode:\n')
	# decoded = [bod.decode("utf-8") for bod in post_bodies]
	# print(decoded)
	post_data = zip(post_ids, post_authors, post_dates, post_bodies)
	# post_data = post_bodies
	# print(post_data)
	return post_data

def write_post_data_to_csv(post_data):
	# writer = csv.writer(open('forum.csv', 'a'))#, quoting=csv.QUOTE_MINIMAL)
	# for value in post_data:
	# 	print(value)
	# 	print(type(value))	
	# 	uvalue = unicode(value, encoding='utf-8')
	# 	print(uvalue)
	# 	print(type(uvalue))	
	# 	writer.writerow(uvalue)
	with open('forum.csv', 'w') as f:
		writer = csv.writer(f, delimiter=';')
		for value in post_data:	
			writer.writerow(value)
			# writer.writerow([value.encode('utf-8')])
		   #ALSO MUST SEE \n in strings instead of having them interpreted

if __name__ == "__main__":
	base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'
	url = base_url
	# html_doc = get_html_doc(url)
	soup = BeautifulSoup(stub3.html_doc, 'html.parser')
	page_uris = get_all_page_uris(soup)


	# # get post detils on the first page
	# print('\n\nGetting post data for url\n')
	# print(url)
	post_data = get_post_data_per_page(soup)
	write_post_data_to_csv(post_data)
	# # # exit()
	# # # then loop through all subsequent pages in the thread
	# for path in page_uris:
	# 	url = urljoin(base_url, path)
	# 	print('\n\nGetting post data for url\n')
	# 	print(url)
	# 	html_doc = get_html_doc(url)
	# 	soup = BeautifulSoup(html_doc, 'html.parser')
	# 	post_data = get_post_data_per_page(soup)
	# 	write_post_data_to_csv(post_data)

	