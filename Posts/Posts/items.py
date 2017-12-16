# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import TakeFirst, Join

class PostsItem(scrapy.Item):
    author = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    title = scrapy.Field(
        input_processor=TakeFirst(),
        output_processor=TakeFirst(),
    )
    categories = scrapy.Field(
        output_processor=Join(),
    )
    labels = scrapy.Field(
        output_processor=Join(),
    )
    content = scrapy.Field(
        output_processor=Join(),
    )

