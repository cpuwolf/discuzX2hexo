import re

attachlist = []

fatch=open("myattachlist.csv")

for line in fatch.readlines():
	attachlist.append(line.strip().split(','))

fatch.close()

print attachlist

def id2src(id):
	for a in attachlist:
		if a[0] == id:
			return a[1]
	return ''

def urltolink(line):
	#convert url to link
	#[url=A]B[/url]   =>   [B](A)
	#[url]A[/url]  => [](A)
	line=re.sub(r'\[url\=(.[^\[]*)\](.*)\[\/url\]',r'\r\n\r\n[\2](\1)\r\n\r\n',line)
	line=re.sub(r'\[url\](.*)\[\/url\]',r'\r\n\r\n[\1](\1)\r\n\r\n',line)
	#[img]
	line=re.sub(r'\[img\=(.[^\[]*)\](.*)\[\/img\]',r'\r\n\r\n![cpuwolfx-plane](\2)\r\n\r\n',line)
	line=re.sub(r'\[img\](.*)\[\/img\]',r'\r\n\r\n![cpuwolfx-plane](\1)\r\n\r\n',line)
	#[size]
	line=re.sub(r'\[size\=(.[^\[]*)\](.*)\[\/size\]',r'\r\n\2\r\n',line)
	line=re.sub(r'\[size\](.*)\[\/size\]',r'\r\n\1\r\n\r',line)
	#[i=s]
	line=re.sub(r'\[i\=s\](.*)\[\/i\]',r'\r\n\r',line)
	
	#remove like [/color]
	line=re.sub(r'\[\/(.[^\[]*)\]',r'\r\n',line)
	#remove like [color=xx]
	line=re.sub(r'\[size(.[^\[]*)\]',r'\r\n',line)
	line=re.sub(r'\[font(.[^\[]*)\]',r'\r\n',line)
	line=re.sub(r'\[color(.[^\[]*)\]',r'\r\n',line)
	line=re.sub(r'\[align(.[^\[]*)\]',r'\r\n',line)
	line=re.sub(r'\[media(.[^\[]*)\]',r'\r\n',line)
	line=re.sub(r'\[hide\]',r'\r\n',line)
	return line

fout=open("blog.txt", "w")

allmd=open("mytitle6.csv")


for line in allmd.readlines():
	#convert attach to markdown image
	nl = re.findall('\[attach\](\d+)\[\/attach\]', line)
	if nl:
		for a in nl:
			line=re.sub(r'\[attach\]'+a+'\[\/attach\]','\r\n![cpuwolf]('+id2src(a)+')\r\n',line)
			print a
	line=urltolink(line)
	fout.write(line)

allmd.close()
fout.close()
