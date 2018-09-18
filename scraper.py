import scrapy

"""docstring for PyScraper"scrapy.Spideref __init__(self, arg):
    super(PyScraper,scrapy.Spider.__init__()
    self.arg = arg"""
class PyScraper(scrapy.Spider):
  name = 'brickset_pyscrapy'
  start_urls = ['https://brickset.com/sets/year-2018']

