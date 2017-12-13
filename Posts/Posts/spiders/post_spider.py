#-*- coding: utf-8 -*-
import scrapy

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
        yield {
            "title" : response.xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/h1/text()").extract(),
            "author" : response.xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/div/span/span/a/text()").extract(),
            "contenido" : response.xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/article/section/p").extract(),
            "categorias" : response.xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/article/header/div/a/text()").extract(),
        }



