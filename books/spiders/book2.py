# -*- coding: utf-8 -*-
import scrapy


class BookSpider(scrapy.Spider):
    name = 'book2'
    # allowed_domains = ['http://books.toscrape.com/']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        
        page = response.url.split("/")[-2]
        filename = 'book-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        linkxp = '//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]/article/h3/a/@href'
        linklist = response.xpath(linkxp)
        yield from response.follow_all(linklist, self.parsedata)

        nextpage = response.xpath('//li[@class="next"]/a/@href').get()
        if nextpage is not None:
            nextpage = response.urljoin(nextpage)
            yield scrapy.Request(nextpage, callback=self.parse)

    def parsedata(self, response):
        name = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
        price = response.xpath('//div[@class="col-sm-6 product_main"]/p/text()').get()
        pdd = response.xpath('//article[@class="product_page"]/p/text()').get()
        pi1 = response.xpath('//table[@class="table table-striped"]//tr/th/text()').getall()
        pi2 = response.xpath('//table[@class="table table-striped"]//tr/td/text()').getall()
        l = []
        for i in range(len(pi1)):
            l.append({pi1[i]:pi2[i]})
        yield {
            'BookName':name, 'Price':price,
            'Product Description':[pdd],
            'Product Information':l
        }

        








    # def parse(self, response):
    #     lenxp = '//ol/li'
    #     lngth = len(response.xpath(lenxp))
    #     namexp = '(//ol/li)[{}]/article/h3/a/@title'
    #     ratingxp = '(//ol/li)[{}]/article/p/@class'
    #     pricexp = '(//ol/li)[{}]/article/div/p[@class="price_color"]/text()'
    #     for i in range(lngth):
    #         namexpath = namexp.format(i+1)
    #         pricexpath = pricexp.format(i+1)
    #         ratingxpath = ratingxp.format(i+1)
    #         name = response.xpath(namexpath).get()
    #         price = response.xpath(pricexpath).get()
    #         rating = (response.xpath(ratingxpath).get()).lstrip('star-rating ')
    #         if rating == 'One':
    #             rating = 1
    #         elif rating == 'Two':
    #             rating = 2
    #         elif rating == 'Three':
    #             rating = 3
    #         elif rating == 'Four':
    #             rating = 4
    #         elif rating == 'Five':
    #             rating = 5
    #         yield {'Booksname':name, 'Price':price, 'Rating':rating} 
        
    #     nextpage = response.xpath('//li[@class="next"]/a/@href').get()
    #     # print(nextpage)
    #     if nextpage is not None:
    #         nextpage = response.urljoin(nextpage)
    #         yield scrapy.Request(nextpage, callback=self.parse)
