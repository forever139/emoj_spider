# -*- coding: utf-8 -*-

import scrapy

class EmojItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()
    image_backup_url = scrapy.Field()
