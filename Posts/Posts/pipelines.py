# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class PostsPipeline(object):
    def open_spider(self, spider):
        self.items = open('./JSON/items.jl', 'w')
        self.items_without_content = open('./JSON/items_without_content.jl', 'w')

    def close_spider(self, spider):
        self.items.close()
        self.items_without_content.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        try:
            if item['content']:
                self.items.write(line)
        except:        
            self.items_without_content.write(line)
        return item