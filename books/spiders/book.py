# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book'
    # allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        lenxp = '//ol/li'
        lngth = len(response.xpath(lenxp))
        namexp = '(//ol/li)[{}]/article/h3/a/@title'
        ratingxp = '(//ol/li)[{}]/article/p/@class'
        pricexp = '(//ol/li)[{}]/article/div/p[@class="price_color"]/text()'
        for i in range(lngth):
            namexpath = namexp.format(i+1)
            pricexpath = pricexp.format(i+1)
            ratingxpath = ratingxp.format(i+1)
            name = response.xpath(namexpath).get()
            price = response.xpath(pricexpath).get()
            rating = (response.xpath(ratingxpath).get()).lstrip('star-rating ')
            if rating == 'One':
                rating = 1
            elif rating == 'Two':
                rating = 2
            elif rating == 'Three':
                rating = 3
            elif rating == 'Four':
                rating = 4
            elif rating == 'Five':
                rating = 5
            yield {'Booksname':name, 'Price':price, 'Rating':rating} 
        
        # nextpage = response.xpath('//li[@class="next"]/a/@href').get()
        # # print(nextpage)
        # if nextpage is not None:
        #     nextpage = response.urljoin(nextpage)
        #     yield scrapy.Request(nextpage, callback=self.parse)
