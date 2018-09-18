import scrapy

"""docstring for PyScraper"scrapy.Spideref __init__(self, arg):
    super(PyScraper,scrapy.Spider.__init__()
    self.arg = arg"""

"""Inheriting Spider class from Scrapy and creating PyScraper sub
class inheriting features from Spider class."""
class PyScraper(scrapy.Spider):
  name = 'brickset_pyscrapy'
  start_urls = ['https://brickset.com/sets/year-2018']

  def parse(self, response):
    SET_SELECTOR = '.set'
    for brickset in response.css(SET_SELECTOR):
      NAME_SELECTOR = 'h1 ::text'
      yield {
        'name': brickset.css(NAME_SELECTOR).extract_first(),
      }
    """selecting .set as css selector for response object. Grabs all the sets
    on the page and loops over them to extract the data. Uses brickset object
    to loop over each set using its own css method to locate set name and
    display"""
