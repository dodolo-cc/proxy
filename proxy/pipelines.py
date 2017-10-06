# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib2
import urllib
import socket
from scrapy import signals

class ProxyPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, spider):
        pipeline = cls()
        spider.signals.connect(pipeline.spider_opened, signals.spider_opened)
        spider.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
        

    def spider_opened(self, spider):
        #print "!!!!!!!!!!spider '",spider.name,"' opened!!!!"
        file = open('proxy_%s.txt' % spider.name, 'w')
        self.files[spider] = file

    def spider_closed(self, spider):
        #print "************spider '",spider.name,"' closed!!!!"
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
		# 编码的转换
        for k in item:
            item[k] = item[k].encode("utf8")
            
        lower_type = item["p_type"].lower()
        if "http"==lower_type:
            proxy_host = lower_type+"://"+item["ip"]+":"+item["port"]
            proxy_temp = {lower_type:proxy_host}
            url = "http://ip.chinaz.com/getip.aspx"
            socket.setdefaulttimeout(2)
            try:
                res = urllib.urlopen(url,proxies=proxy_temp).read()
                line = proxy_host + "\n"
                print "This is Available: ",line,"!!!"
                self.files[spider].write(line)
            except Exception,e:
                print "This proxy '",proxy_host,"' is Not Available!"
        else:
            print "Not http, pass!"
        return item

    
