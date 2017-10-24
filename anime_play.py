import os
import applescript

from animapy import anime

search = raw_input('search: (string) ')
index = int(raw_input('index: (integer) '))

script = applescript.AppleScript('''
	on qt_play(url)
		tell Application "QuickTime Player"
			open URL arg1
		end tell
	end qt_play
	
	on qt_close()
		tell Application "QuickTime Player"
			close window 1
		end tell
	end qt_close
''')

def play(s):
	for ep in anime.searchAnimes(s, quant=1):
		if ep == '': continue
		url = hasattr(ep, 'hd') and ep.hd or ep.normal
		print('starting to play %s' % ep.title)
		script.call('qt_play', url)
		
while(1):
	play('%s %03d' % (search, index))
	raw_input('Enter to open next movie: ')
	script.call('qt_close')
	index+=1