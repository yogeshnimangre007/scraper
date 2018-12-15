# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:53:29 2018

@author: OptimusPrime
"""
import lxml.html
import requests
from lxml.cssselect import CSSSelector
url="http://jobwik.com/page/free-epaper-the-hindu/"
r = requests.get(url)
#responce_initial=r.text
#print(r.text)
tree=lxml.html.fromstring(r.text)
#print(lxml.html.tostring(tree))
sel=CSSSelector('article>div:first-child a[class^=\'color-\']')
first=sel(tree)
#second page selection
first_result=lxml.html.fromstring(first)
#print(first_result)
sel1=CSSSelector('h4>a')
link=sel1(first_result)
print(link)
