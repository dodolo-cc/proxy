# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proxy.items import ProxyItem


class KuaiSpider(CrawlSpider):
    name = "kuai"
    allowed_domains = ["www.kuaidaili.com"]
    start_urls = ('http://www.kuaidaili.com/free/inha/','http://www.kuaidaili.com/free/intr/')

    rules = (

        Rule(LinkExtractor(allow=(r"http://www.kuaidaili.com/free/inha/[1-2]/")),callback="proxy_parse"),
        Rule(LinkExtractor(allow=(r"http://www.kuaidaili.com/free/intr/[1-2]/")),callback="proxy_parse")

    )

    def proxy_parse(self, response):
        sel = Selector(response=response)
        item =ProxyItem()
        
        ip_list = sel.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

        for ip in ip_list:
            item["ip"] = ip.xpath("td[1]/text()").extract()[0].strip()
            print item["ip"]
            item["port"] = ip.xpath("td[2]/text()").extract()[0].strip()
            print item["port"]
            item["p_type"] = ip.xpath("td[4]/text()").extract()[0].strip()
            print item["p_type"]
            if "http" == item["p_type"].lower():  
                yield item  
