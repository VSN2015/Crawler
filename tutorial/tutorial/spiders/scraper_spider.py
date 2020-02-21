import scrapy
from ..items import TutorialItem

class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    start_urls = ['']

    def parse(self, response):
      # item = TutorialItem()
      # image_urls= []
      # for img in response.css('a img'):
      #   image_urls.append(img.css('img::attr(src)').extract_first())
      #  	item['image_urls'] = image_urls
      # return item

        SET_SELECTOR = 'a img'
        for brickset in response.css(SET_SELECTOR):

            MEANING_SELECTOR = 'img::attr(alt)'
            IMAGE_SELECTOR = 'img::attr(src)'
            yield {
                'meaning': [brickset.css(MEANING_SELECTOR).extract_first()],
                'image_urls': [brickset.css(IMAGE_SELECTOR).extract_first()]
                }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield {scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )}