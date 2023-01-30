# -*- coding: utf-8 -*
#!/usr/bin/python
#To Take To More
import requests, re,time
from colorama import Fore,Style,init
from multiprocessing.dummy import Pool as ThreadPool
init(autoreset=True)

r = Fore.RED
y = Fore.YELLOW
g = Fore.GREEN
o = Fore.RESET
def take0ver(url):
	if "http://" in url:
		url =url
	else:
     url = "https://" + url
	try:
		e = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'}, timeout=30).content
		if '<title>Site not found &middot; GitHub Pages</title>' in e:
			print(y+'Valid Take0ver : '+ g + url + o)
			open('take.txt','a').write(urle+'\n')
		else:
			print(r + 'BAD' + ' ' + url + o)
	except:
		pass

print "{}Takeover | Code By H0rn3T Sp1d3rs\n".format(y)
url = open(raw_input('List: '),'r').read().splitlines()
pool = ThreadPool(int(50))
pool.map(take0ver, url)
pool.close()
pool.join()
