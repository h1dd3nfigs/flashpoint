#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
from bs4 import BeautifulSoup, NavigableString, Tag
import math

class Scraper:
	page_uris = set()

	def __init__(self, soup, url):
		self.soup = soup
		self.url = url
	#
	# Get the URIs for all pages in this forum thread, 
		# DOM Location: All <a> descendants of the first <span class="gensmall">
		#
	def get_all_page_uris(self):
		# page_uris = set()
		span_tag = self.soup.find("span", class_="gensmall")
		for a_tag in span_tag.find_all("a"):
			self.page_uris.add( a_tag.get('href'))

		return self.page_uris

	#
	# Get all the post ids on this page
		# DOM Location: <span class="name"><a name={post_id}> 
		#
	def get_post_ids(self):
		post_ids = []
		for span_tag in self.soup.find_all("span", class_="name"):
			a_tag = span_tag.find('a')
			post_id = a_tag.get('name')
			post_ids.append(int(post_id))
		
		return post_ids

	#
	# Get all the post authors on this page
		# DOM Location: <span class="name"><b>{post_author}</b>
	#
	def get_post_authors(self):
		post_authors = []
		for span_tag in self.soup.find_all("span", class_="name"):
			author = span_tag.find('b').text
			post_authors.append(repr(author.encode('utf-8')))

		return post_authors

	#
	# Get all post dates on this page
	# DOM Location:	<span class="postdetails">"Posted: {post_date}				
	#
	def get_post_dates(self):
		post_dates = []
		date_prefix = 'Posted: '
		for span_tag in self.soup.find_all("span", class_="postdetails"):
			if date_prefix in span_tag.contents[0]:
				post_date = span_tag.contents[0].lstrip(date_prefix)
				post_dates.append(repr(post_date.encode('utf-8')))

		return post_dates

	#
	# Get all post bodies on this page
		# DOM Location is the 2nd <td> in every 3rd <tr> in <table class=forumline> 	
		# <table class="forumline">
		# 	<tbody> 
		#		<tr>...</tr>
		#		<tr>...</tr>
		#		<tr>
		#			<td>...</td>
		#			<td>{post_body}</td>
		#		</tr>
		#
	def get_post_bodies(self):
		post_bodies = []
		tbody_children = self.soup.find("table", class_="forumline").find('tbody').contents
		tr_tags = []

		for t in tbody_children:
			if t.name == 'tr':
				tr_tags.append(t)
										   # [2,5,8,11,...,len(tr_tags)]
		for tr_tag in [tr_tags[x] for x in range(len(tr_tags))[2:len(tr_tags):3] ]:
			all_td_tags = tr_tag.find_all('td')
			td_tags = all_td_tags[1].contents
			postbody = unicode('', encoding ='utf-8')	

			for td in td_tags:
				kids = td.find_all('tr')
				if kids:
					tr_with_postbody = kids[2]
					if isinstance(tr_with_postbody, Tag):
						postbody += unicode.join(u'', tr_with_postbody.text)
						postbody = postbody.split('_________________')[0]
					else:	
						postbody += unicode.join(u'', tr_with_postbody)
						postbody = postbody.split('_________________')[0]

			post_bodies.append(repr(postbody.encode('utf-8').strip()))

		return post_bodies


	def get_post_data_per_page(self):
		post_ids = self.get_post_ids()
		post_authors = self.get_post_authors()
		post_dates = self.get_post_dates()
		post_bodies = self.get_post_bodies()
		post_data = zip(post_ids, post_authors, post_dates, post_bodies)

		return post_data