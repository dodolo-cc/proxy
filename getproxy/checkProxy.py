# -*- coding: utf-8 -*-
import urllib2
import urllib
import socket
import os
import shutil
import filecmp

def updateIp():
    url = "http://ip.chinaz.com/getip.aspx"
    socket.setdefaulttimeout(1)
    ip_file = "/usr/spider/checkproxy/ip.txt"
    bak_file = "/usr/spider/checkproxy/ip_bak.txt"
    if os.path.exists(ip_file) and os.path.getsize(ip_file):
        print "ip.txt exist and not empty............"
        shutil.copyfile(ip_file,bak_file)
        with open(ip_file,"r") as f:
            lines = f.readlines()
        if filecmp.cmp(ip_file,bak_file):
            print "ip.txt not changed so far.........."
            with open(ip_file,"w") as f_w:
                for line in lines:
                    proxy_host = line.strip()
                    #proxy_host = "http://"+ip[0]+":"+ip[1]
                    proxy_temp = {"http":proxy_host}
                    try:
                        res = urllib.urlopen(url,proxies=proxy_temp).read()
                        f_w.write(line)
                        print line
                    except Exception,e:
                        continue
                

   
if __name__ == '__main__':
 updateIp()
