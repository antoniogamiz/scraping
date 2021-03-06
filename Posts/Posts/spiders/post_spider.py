#-*- coding: utf-8 -*-
import scrapy
from Posts.items import PostsItem
from scrapy.loader import ItemLoader

class PostsSpider(scrapy.Spider):
    name = "postsosl"
    start_urls = [
        "http://osl.ugr.es/",
    ]

    def parse(self, response):
        for href in response.xpath("//article/section/header/h2/a"):    # Analizamos cada post de una página.
            yield response.follow(href, self.parse_post)

        next_page = response.xpath("/html/body/div[1]/div[2]/div[3]/div/div[1]/nav/ul/li/span/a/@href").extract_first() # Avanzamos a la siguiente página.
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_post(self, response):
        
        loader = ItemLoader(PostsItem(), selector=response)

        loader.add_xpath('author', '/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/div/span/span/a/text()')
        loader.add_xpath('title', '/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/h1/text()')
        loader.add_xpath('categories', '/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/div/a/text()')
        loader.add_xpath('labels', "/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/div/a[@class='btn btn-mini']/text()")
        loader.add_xpath('content', '/html/body/div[1]/div[2]/div[2]/div/div[1]/article/section/p/text()')

        return loader.load_item()




