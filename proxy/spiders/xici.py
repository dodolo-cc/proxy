# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proxy.items import ProxyItem



class XiciSpider(CrawlSpider):
    name = "xici"
    allowed_domains = ["www.xicidaili.com"]
    start_urls = ("http://www.xicidaili.com/nn/2",)

    rules = (

        Rule(LinkExtractor(allow=(r"http://www.xicidaili.com/nn/[1-2]$")),callback="proxy_parse"),

    )

    def proxy_parse(self, response):
        sel = Selector(response=response)
        item =ProxyItem()
        
        ip_list = sel.xpath('//table[@id="ip_list"]/tr')

        if len(ip_list) > 0:
            ip_list.pop(0)
        for ip in ip_list:
            item["ip"] = ip.xpath("td[2]/text()").extract()[0].strip()
            item["port"] = ip.xpath("td[3]/text()").extract()[0].strip()
            item["p_type"] = ip.xpath("td[6]/text()").extract()[0].strip()
            if "http" == item["p_type"].lower():  
                yield item 

