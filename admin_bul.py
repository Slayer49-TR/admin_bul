#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Coder Slayer49

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("admin.txt","r");
	link = raw_input("Site Adresini Yazınız \n(Örn : site.com or www.site.com ): ")
	print "\n\nDoğru Linkler : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Tamam => ",req_link

def Credit():


	Space(4); print " Coder Slayer49 "
	Space(4); print " İsimim Her Yıkık Duvarda  "
Credit()
findAdmin()
