'''
Problem :
you want check the start or end of a string.
like URL .

Solution:
Use the 
startswith() or endswith

date:2014 05 23
author:william
'''
print "zxcvasdfsadf"
filename = 'hello.txt'
filename.endswith('.txt')
filename.startswith('hello')
filename.startswith('asdf')
website = 'www.google.com'
website.startswith('http:')

# if you want check mutiple string
filenames = 'hello.txt','first.py','second.c', 'QQ.py'
for name in filenames:
	if name.endswith(('.py', '.c')):
		print name

# you can to use the splice for replece this way
filename = 'hello.txt'
filename[-4:] == '.txt'

website = 'http://www.google.com'
website[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:'
