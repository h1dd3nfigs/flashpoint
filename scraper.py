#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Imports 
import csv
import pycurl
from StringIO import StringIO
from bs4 import BeautifulSoup, NavigableString, Tag
from urlparse import urlparse, urljoin
# import stub_html_doc as stub
# import stub5_html_doc as stub5
# import stub3_html_doc as stub3
# import stub3_extra_nest_html_doc as stub3x

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
# DOM Location: <span class="name"><a name={post_id}> 
#
def get_post_ids(soup):
	post_ids = []
	for span_tag in soup.find_all("span", class_="name"):
		a_tag = span_tag.find('a')
		post_id = a_tag.get('name')
		post_ids.append(post_id)
	
	return post_ids

#
# Get the all post authors on this page
# DOM Location: <span class="name"><b>{post_author}</b>
#
def get_post_authors(soup):
	post_authors = []
	for span_tag in soup.find_all("span", class_="name"):
		author = span_tag.find('b').text
		post_authors.append(author)
		# CONVERT FROM UNICODE TO UTF8 so chars in foreign names show up right 

	return post_authors

#
# Get all post dates on this page
# DOM Location:	<span class="postdetails">"Posted: {post_date}				
#
def get_post_dates(soup):
	post_dates = []
	date_prefix = 'Posted: '
	for span_tag in soup.find_all("span", class_="postdetails"):
		if date_prefix in span_tag.contents[0]:
			post_dates.append(span_tag.contents[0].lstrip(date_prefix))

	return post_dates

#
# Get all post bodies on this page
# DOM Location for a post WITHOUT quoted posts: 	
# 	<span class="postbody">{post_body}<br />_________________				
						
# 	 		 OR
# DOM Location for 1 quoted post nested in a post: 	
# <span class=postbody></span>
# 	<table>
# 		<tr><td>
# 			<span class="genmed">{quoted author} wrote: </span>
# 			<td class="quote">{quoted body}</td>
# 		</td></tr>
# </table>
# <span class="postbody">{postbody}<br />_________________
# 
# parameters:
# span_tag 	bs4.element.Tag object, the 
# author 	string, 	

def get_quoted_post(span_tag, author='', nesting_level = 1):	
	print('\nrunning RECURSIVE FUNCTION now\n')
	author += span_tag.find_next('table').find('span', class_='genmed').text + ' ['
	sibling_table = span_tag.find_next('table').find('td', class_='quote')
	
	if sibling_table.contents == []:
		nesting_level += 1
		return get_quoted_post(sibling_table, author, nesting_level)

	else:
		quote_body = author
		quote_pieces = sibling_table.contents
		if len(quote_pieces)  > 1:
			for q in quote_pieces:
				if not isinstance(quote_pieces,Tag):
					quote_body += unicode.join(u'', q)

		elif len(quote_pieces) == 1:
			print(quote_pieces[0])
			quote_body += quote_pieces[0]
		else:
			pass

		return [nesting_level, quote_body ]


def get_post_bodies(soup):
	post_bodies = []
	i = 0
	nesting_level = 0
	is_quote_post = False
	body = unicode('', encoding ='utf-8')	
	span_tag_result_set = soup.find_all("span", class_="postbody")

	for span_tag in span_tag_result_set:

		# if the span tag's empty, this post body contains a quoted post
		if span_tag.contents == []: 			
			nesting_level, quote_body = get_quoted_post(span_tag)
			body = quote_body

		# otherwise, it's a regular post so put the contents into a new post body's string
		else:
			body = unicode('', encoding ='utf-8')
			for text in span_tag.contents:

				# the underscore marks the end of a post body if the author ends posts with a signature
				if text == '_________________':
					is_quote_post = False
					break
				
				else:

					if isinstance(text, NavigableString):
						body += text
				
					# the text is prob a <br/> tag so get the string repr of it
					elif isinstance(text,Tag):
						# body += str(text)
						pass

					else:
						body += unicode.join(u'',text)
			
			#endfor

		# based on the number of quoted posts that are nested in the post body, 
		# create a list of the span tags to check when deciding whether a span's text belongs in a nested quoted post or just a regular post
		priors = [span_tag_result_set[x].contents for x in range(i - nesting_level - 1, i, 1)]

		if i== 0 or (span_tag_result_set[i].contents == []):
			post_bodies.append(body.encode('utf-8'))

		# if the previous element in this span_tag_result_set contained no text, it sign
		# then pop off that last item and concatenate this body string with that one because it was a quoted post and needs to be combined with the author's actual text
		# elif i >= 1 and span_tag_result_set[i].contentgits != [] and (span_tag_result_set[i-nesting_level].contents == [] or span_tag_result_set[i-nesting_level-1].contents == []):
		elif i >= 1 and span_tag_result_set[i].contents != [] and any(p == [] for p in priors):
			print('in block 2')
			print('and luckily nesting level is {0}'.format(nesting_level))	
			prev_body = unicode(post_bodies.pop()+']', encoding='utf-8')
			prev_body += unicode.join(u'',body)

			print('appending\n {0} to position {1} of post_bodies list'.format(prev_body.encode('utf-8'), len(post_bodies)))

			post_bodies.append(prev_body.encode('utf-8'))
			is_quote_post = False
			nesting_level -= 1

		# else, the previous element did not belong ot a quoted post so we can just append this additional body text as a new post's text
		else:
			print('in block 3')
			print('appending\n {0} to position {1} of post_bodies list'.format(body.encode('utf-8'), len(post_bodies)))

			post_bodies.append(body.encode('utf-8'))
			# is_quote_post = False
		i += 1

		
	# print(post_bodies[1])
	# exit()
	return post_bodies

def get_post_data_per_page(soup):
	post_ids = get_post_ids(soup)
	post_authors = get_post_authors(soup)
	post_dates = get_post_dates(soup)
	post_bodies = get_post_bodies(soup)
	post_data = zip(post_ids, post_authors, post_dates, post_bodies)

	return post_data

def write_post_data_to_csv(post_data):
	with open('forum.csv', 'a') as f:
		writer = csv.writer(f, delimiter=';')
		for value in post_data:	
			writer.writerow(value)
			# writer.writerow([value.encode('utf-8')])
		   #ALSO MUST SEE \n in strings instead of having them interpreted

if __name__ == "__main__":
	base_url = 'http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591'
	url = base_url
	html_doc = get_html_doc(url)
	soup = BeautifulSoup(html_doc, 'html.parser')
	page_uris = get_all_page_uris(soup)


	# # get post details on the first page
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

	