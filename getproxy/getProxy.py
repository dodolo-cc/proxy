# -*- coding: utf-8 -*-
import urllib2
import urllib
import socket
import filecmp
import shutil
import os
  

'''
获取现有和更新的代理IP地址
'''
def getProxyIp():
     proxy = []
     old_pl = "/usr/spider/proxy/proxy_proxylists.txt"
     new_pl = "/usr/spider/checkproxy/proxys/proxy_proxylists.txt"
     old_kuai = "/usr/spider/proxy/proxy_kuai.txt"
     new_kuai = "/usr/spider/checkproxy/proxys/proxy_kuai.txt"
     old_xici = "/usr/spider/proxy/proxy_xici.txt"
     new_xici = "/usr/spider/checkproxy/proxys/proxy_xici.txt"
     old_66ip = "/usr/spider/proxy/proxy_66ip.txt"
     new_66ip = "/usr/spider/checkproxy/proxys/proxy_66ip.txt"
     if os.path.exists(old_pl) and os.path.getsize(old_pl) and not filecmp.cmp(old_pl,new_pl) :
         shutil.copyfile(old_pl,new_pl)
         with open(new_pl,"r") as f_pl:
             lines_pl = f_pl.readlines()
             for line in lines_pl:
                 proxy.append(line)
                 
     if os.path.exists(old_kuai) and os.path.getsize(old_kuai) and not filecmp.cmp(old_kuai,new_kuai):
         shutil.copyfile(old_kuai,new_kuai)
         with open(new_kuai,"r") as f_k:
             lines_k = f_k.readlines()
             for line in lines_k:
                 proxy.append(line)
                 
     if os.path.exists(old_xici) and os.path.getsize(old_xici) and not filecmp.cmp(old_xici,new_xici):
         shutil.copyfile(old_xici,new_xici)
         with open(new_xici,"r") as f_x:
             lines_x = f_x.readlines()
             for line in lines_x:
                 proxy.append(line)
                 
     if os.path.exists(old_66ip) and os.path.getsize(old_66ip) and not filecmp.cmp(old_66ip,new_66ip):
         shutil.copyfile(old_66ip,new_66ip)
         with open(new_66ip,"r") as f_6:
             lines_6 = f_6.readlines()
             for line in lines_6:
                 proxy.append(line)
     if os.path.exists("/usr/spider/checkproxy/ip.txt") and os.path.getsize("/usr/spider/checkproxy/ip.txt"):
         with open("/usr/spider/checkproxy/ip.txt","r") as ips:
             lines_ip = ips.readlines()
             for line in lines_ip:
                 if line not in proxy:
                     proxy.append(line)  
     return proxy
             
         
     
     
     

'''

验证获得的代理IP地址是否可用
'''
def validateIp(proxy):
 url = "http://ip.chinaz.com/getip.aspx"
 socket.setdefaulttimeout(1) 
 with open("/usr/spider/checkproxy/ip.txt","w") as f:
     print f.name
     for i in range(0,len(proxy)):
          print proxy[i]
          try:
               proxy_host = proxy[i].strip().split("://")
               proxy_temp = {proxy_host[0]:proxy[i].strip()}
               res = urllib.urlopen(url,proxies=proxy_temp).read()
               f.write(proxy[i])
          except Exception,e:
               continue

  
     
if __name__ == '__main__':
 proxy = getProxyIp()
 validateIp(proxy)
