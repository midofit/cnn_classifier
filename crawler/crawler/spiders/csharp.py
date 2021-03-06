import scrapy
import re

class Spider(scrapy.Spider):
    name = "CSharp"
    start_urls = ['http://rosettacode.org/wiki/Category:C_sharp']
    def parse(self, response):
        for url in response.xpath('//a[contains(@href,*)]/@href'):
            yield scrapy.Request('http://rosettacode.org'+url.extract(),callback = self.parseURL)



    def parseURL(self, response):
        a = '';
        comments = r'^\/\/\/ | ^\/\*'
        for code in response.xpath('//pre[contains(@class,"csharp highlighted_source")]/span/text() | //pre[contains(@class,"csharp highlighted_source")]/text() | //pre[contains(@class,"csharp highlighted_source")]/span/br').extract():
            if code == "<br>":
                a += "\n"
                continue
            if re.match(comments, code):
                a+="\n"
                continue
            else:
                a+= re.sub(r"\".*\"",'strv',code)
        if len(a)>0:
            yield {
                    'keywords':a
            }
