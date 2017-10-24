import os
import applescript
import urllib

from animapy import anime

search = raw_input('search: (string) ')
index = int(raw_input('index: (integer) '))

def download(s):
	for ep in anime.searchAnimes(s, quant=1):
		if ep == '': continue
		url = hasattr(ep, 'hd') and ep.hd or ep.normal
		print('downloading %s' % ep.title)
        urllib.urlretrieve(url, ep.title + '.mp4')

while(1):
	download('%s %03d' % (search, index))
	index+=1
