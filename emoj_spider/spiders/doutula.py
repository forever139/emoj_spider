# -*- coding: utf-8 -*-
import scrapy
from emoj_spider.items import EmojItem

class DouTuLaSpider(scrapy.Spider):
    name = 'doutula'
    allowed_domains = ['doutula.com']
    start_urls = ('https://www.doutula.com/photo/list/?page=%s' % page for page in xrange(1, 77))
    image_items_selector = '//img'
    img_name_x = './/img/@alt'
    img_href_x = './/img/@src'
    image_backup_url_x = './/img/@data-backup'

    def parse(self, response):
        image_items_selector = response.xpath(self.image_items_selector)

        for item_selector in image_items_selector:
            temp_url = item_selector.xpath(self.img_href_x).extract()[0]
            if 'sinaimg.cn' not in temp_url:
                continue
            emoj_item = EmojItem()
            emoj_item['title'] = item_selector.xpath(self.img_name_x).extract()[0]
            emoj_item['image_url'] = item_selector.xpath(self.img_href_x).extract()[0]
            emoj_item['image_backup_url'] = item_selector.xpath(self.image_backup_url_x).extract()[0]
            yield emoj_item
