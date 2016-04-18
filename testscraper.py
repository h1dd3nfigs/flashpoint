#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
from bs4 import BeautifulSoup
from scraper import Scraper
from stub_html_doc import html_doc

class TestScraper(unittest.TestCase):
  
  maxDiff = None

  def setUp(self):
      self.soup = BeautifulSoup(html_doc,'html5lib')
      self.scraper = Scraper(self.soup)
      
  def tearDown(self):
      self.soup = self.scraper = None

  def test_get_all_page_uris(self):
      uris = set([u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=60&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=15&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=105&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=30&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=75&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=90&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=120&sid=5231e0b382464441052b0a7af66e34ce',
                  u'viewtopic.php?t=12591&postdays=0&postorder=asc&start=45&sid=5231e0b382464441052b0a7af66e34ce'
                  ])
      self.assertEqual(self.scraper.get_all_page_uris(), uris)

  def test_get_post_ids(self):
      ids = [87120, 87131, 87133, 87135, 87136, 87139, 87140, 87142, 87146, 87148, 87149, 87151, 87154, 87156, 87157]    
      self.assertEqual(self.scraper.get_post_ids(), ids)

  def test_get_post_authors(self):
      authors = ["'Rick'", "'pigtin'", "'riley541'", "'47p2'", "'Rick'", "'welshrover'", "'welshrover'", "'swampy'", "'welshrover'", "'Penman'", "'victor 101'", "'peterwpg'", "'pigtin'", "'riley541'", "'Rick'"]
      self.assertEqual(self.scraper.get_post_authors(), authors)

  def test_get_post_dates(self):
      dates = ["'Mon Sep 24, 2012 4:53 pm'", "'Mon Sep 24, 2012 8:29 pm'", "'Mon Sep 24, 2012 8:47 pm'", "'Mon Sep 24, 2012 9:00 pm'", "'Mon Sep 24, 2012 9:04 pm'", "'Mon Sep 24, 2012 9:09 pm'", "'Mon Sep 24, 2012 9:10 pm'", "'Mon Sep 24, 2012 10:02 pm'", "'Mon Sep 24, 2012 10:31 pm'", "'Tue Sep 25, 2012 12:34 am'", "'Tue Sep 25, 2012 1:34 am'", "'Tue Sep 25, 2012 4:28 am'", "'Tue Sep 25, 2012 6:41 am'", "'Tue Sep 25, 2012 7:21 am'", "'Tue Sep 25, 2012 7:41 am'"]
      self.assertEqual(self.scraper.get_post_dates(), dates)

  def test_get_post_bodies(self):
    bodies = ["'Tonight, 8pm, might be worth a look...?\\n\\n\\n\\nRJ'", '"Oh dear! Just switched off... a couple of geezers on an ego trip, couldn\'t take any more when they picked up the shock absorber in the breakers yard. Would you want to sell a classic at a knockdown price to this guy?"', '"What a terrible programme. Why on earth did the production company choose that foul mouthed cockney bodger to front it? I\'ll watch this one until the bitter end out of curiousity but that\'s it for me, no more of this rubbish."', '"I\'ve recorded it to watch later, I might give it a miss now"', '\'Deary me, "restore" something and leave that awful glass pop-up sunroof in it, not to mention the junk they bought from the other fella. Good to hear that they repaired a piston, and cleaned out the cylinders though ... \\n\\n\\n\\n\\xc3\\x82\\xc2\\xa330k?\\n\\n\\n\\nRJ\\n\\n\\n\\nI\\\'ll probably watch the next one though, out of curiosity\'', "'what a load of rubbish .arthur daley would have done a better job . poxy modern sunroof ,nice pinky red paint then bangs it into an engine .would you buy a car from these two plonkers .'", '"47p2 wrote:\\t\\t\\t  I\'ve recorded it to watch later, I might give it a miss now  \\t\\n\\ni wouldn\'t bother."', '"One and half days to sort out the \'too much oil in the carb\' issue just after he had boasted that he\'d been doing this for thirty something years   I can truly say that I was awestruck"', "'those diagprahms in the carbs looked new too.'", '"Hi\\n\\nThe e type was the first car designed using a wind tunnel??\\n\\nI think not, Bristol Cars used Bristol Aeroplane\'s wind tunnel in the design stages of the 401 introduced in 1948."', "'I turned off before it was half way through, about where he pulled some supposedly E type parts of the back of a pick up truck.'", '\'Penman wrote:\\t\\t\\t  Hi\\n\\nThe e type was the first car designed using a wind tunnel??\\n\\nI think not, Bristol Cars used Bristol Aeroplane\\\'s wind tunnel in the design stages of the 401 introduced in 1948.\\t\\n\\n\\n\\nand as far back as 1934 Chrysler used the wind tunnel for their "Airflow" series.   \\n\\n\\n\\nI haven\\\'t seen the programme that is the subject of this thread, but poorly researched and gross presentations are quite common this side of the "pond"\'', '"It was dumbed down to a point where I thought I\'d switched on Eastenders by mistake. I believe there are a load of \'Toff\' producers with a very strange idea about what many of us \'Plebs\' like to watch. Surely they could have asked someone who knew about restorations to look it over.\\n\\nHaving switched off before halfway through I can only assume, from comments on here, the programme didn\'t redeem itself in the second half..."', "'Make your opinion known - I have-\\n\\n\\n\\ncustomerservices@channel5.com'", "'Times like this I wish I had shares in Isopon \\n\\n\\n\\nRJ'", "''"]
    self.assertEqual(self.scraper.get_post_bodies(), bodies)

  # not a good unit test since it's dependent on 4 other methods to behave
  def test_get_post_data_per_page(self):
    data = [(87120, "'Rick'", "'Mon Sep 24, 2012 4:53 pm'", "'Tonight, 8pm, might be worth a look...?\\n\\n\\n\\nRJ'"), (87131, "'pigtin'", "'Mon Sep 24, 2012 8:29 pm'", '"Oh dear! Just switched off... a couple of geezers on an ego trip, couldn\'t take any more when they picked up the shock absorber in the breakers yard. Would you want to sell a classic at a knockdown price to this guy?"'), (87133, "'riley541'", "'Mon Sep 24, 2012 8:47 pm'", '"What a terrible programme. Why on earth did the production company choose that foul mouthed cockney bodger to front it? I\'ll watch this one until the bitter end out of curiousity but that\'s it for me, no more of this rubbish."'), (87135, "'47p2'", "'Mon Sep 24, 2012 9:00 pm'", '"I\'ve recorded it to watch later, I might give it a miss now"'), (87136, "'Rick'", "'Mon Sep 24, 2012 9:04 pm'", '\'Deary me, "restore" something and leave that awful glass pop-up sunroof in it, not to mention the junk they bought from the other fella. Good to hear that they repaired a piston, and cleaned out the cylinders though ... \\n\\n\\n\\n\\xc3\\x82\\xc2\\xa330k?\\n\\n\\n\\nRJ\\n\\n\\n\\nI\\\'ll probably watch the next one though, out of curiosity\''), (87139, "'welshrover'", "'Mon Sep 24, 2012 9:09 pm'", "'what a load of rubbish .arthur daley would have done a better job . poxy modern sunroof ,nice pinky red paint then bangs it into an engine .would you buy a car from these two plonkers .'"), (87140, "'welshrover'", "'Mon Sep 24, 2012 9:10 pm'", '"47p2 wrote:\\t\\t\\t  I\'ve recorded it to watch later, I might give it a miss now  \\t\\n\\ni wouldn\'t bother."'), (87142, "'swampy'", "'Mon Sep 24, 2012 10:02 pm'", '"One and half days to sort out the \'too much oil in the carb\' issue just after he had boasted that he\'d been doing this for thirty something years   I can truly say that I was awestruck"'), (87146, "'welshrover'", "'Mon Sep 24, 2012 10:31 pm'", "'those diagprahms in the carbs looked new too.'"), (87148, "'Penman'", "'Tue Sep 25, 2012 12:34 am'", '"Hi\\n\\nThe e type was the first car designed using a wind tunnel??\\n\\nI think not, Bristol Cars used Bristol Aeroplane\'s wind tunnel in the design stages of the 401 introduced in 1948."'), (87149, "'victor 101'", "'Tue Sep 25, 2012 1:34 am'", "'I turned off before it was half way through, about where he pulled some supposedly E type parts of the back of a pick up truck.'"), (87151, "'peterwpg'", "'Tue Sep 25, 2012 4:28 am'", '\'Penman wrote:\\t\\t\\t  Hi\\n\\nThe e type was the first car designed using a wind tunnel??\\n\\nI think not, Bristol Cars used Bristol Aeroplane\\\'s wind tunnel in the design stages of the 401 introduced in 1948.\\t\\n\\n\\n\\nand as far back as 1934 Chrysler used the wind tunnel for their "Airflow" series.   \\n\\n\\n\\nI haven\\\'t seen the programme that is the subject of this thread, but poorly researched and gross presentations are quite common this side of the "pond"\''), (87154, "'pigtin'", "'Tue Sep 25, 2012 6:41 am'", '"It was dumbed down to a point where I thought I\'d switched on Eastenders by mistake. I believe there are a load of \'Toff\' producers with a very strange idea about what many of us \'Plebs\' like to watch. Surely they could have asked someone who knew about restorations to look it over.\\n\\nHaving switched off before halfway through I can only assume, from comments on here, the programme didn\'t redeem itself in the second half..."'), (87156, "'riley541'", "'Tue Sep 25, 2012 7:21 am'", "'Make your opinion known - I have-\\n\\n\\n\\ncustomerservices@channel5.com'"), (87157, "'Rick'", "'Tue Sep 25, 2012 7:41 am'", "'Times like this I wish I had shares in Isopon \\n\\n\\n\\nRJ'")]
    self.assertEqual(self.scraper.get_post_data_per_page(), data)

suite = unittest.TestLoader().loadTestsFromTestCase(TestScraper)
unittest.TextTestRunner(verbosity=2).run(suite)