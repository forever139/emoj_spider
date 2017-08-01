# -*- coding: utf-8 -*-
import scrapy
from emoj_spider.items import EmojItem

class ZhuangbiSpider(scrapy.Spider):
    name = 'zhuangbi'
    allowed_domains = ['zhuangbi.info']
    start_urls = ('https://www.zhuangbi.info/?page=%s' % page for page in xrange(1, 77))
    image_items_selector = '//*[@class="picture-list"]/span'
    img_name_x = './/img/@alt'
    img_href_x = './/img/@src'

    def parse(self, response):
        image_items_selector = response.xpath(self.image_items_selector)

        for item_selector in image_items_selector:
            emoj_item = EmojItem()
            emoj_item['title'] = response.xpath(self.img_name_x).extract()[0]
            emoj_item['image_url'] = response.xpath(self.img_href_x).extract()[0]
            emoj_item['source_url'] = response.url
            yield emoj_item



