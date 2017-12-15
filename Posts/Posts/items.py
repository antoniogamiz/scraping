# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose
from w3lib.html import remove_tags

def clean_content(content):
    # new_content=re.sub("\<p\>", '', str(content[0]))
    return str(type(content))

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

