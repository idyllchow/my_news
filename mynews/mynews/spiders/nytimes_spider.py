import scrapy
from scrapy.loader import ItemLoader

from mynews.items import MynewsItem


class NYSpider(scrapy.Spider):
    name = "nytimes"
    allowed_domains = ["cn.nytimes.com"]
    start_urls = ["https://cn.nytimes.com/"]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # for sel in response.xpath('//ul/li'):
        #     item = MynewsItem()
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     print('title is %s, link is %s' % (title, link))
        #     yield item

        # for sel in response.xpath('//h3'):
        l = ItemLoader(item=MynewsItem(), response=response)
        l.add_xpath('name', '//div[@class="product_name"]')
        l.add_xpath('price', '//p[@id="price"]')
        return l.load_item()


def parseFirstPage(self, response):
    for sel in response.xpath('//h3'):
        item = MynewsItem()
        content = sel.xpath('a/text()').extract()
        print('content ===== %s' % content)
