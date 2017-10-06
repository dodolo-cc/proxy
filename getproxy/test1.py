# -*- coding: utf-8 -*-
import urllib2
import urllib
import socket


def deleteLine():
    with open("D:\ip.txt","r") as f:
        lines = f.readlines()
        print(lines)
    with open("D:\ip.txt","w") as f_w:
        for line in lines:
            if "180.104.223.18" in line:
                continue
            f_w.write(line)

if __name__ == '__main__':
 deleteLine()
