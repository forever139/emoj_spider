# -*- coding: utf-8 -*-

import scrapy

class EmojItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()
    source_url = scrapy.Field()
