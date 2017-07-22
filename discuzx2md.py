import re
import codecs
import os

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

fout=open("out/blog.txt", "w")

allmd=open("mytitle6.csv")


for line in allmd.readlines():
	#convert attach to markdown image
	nl = re.findall('\[attach\](\d+)\[\/attach\]', line)
	if nl:
		for a in nl:
			linkpth='/images/' + id2src(a).replace('"','')
			line=re.sub(r'\[attach\]'+a+'\[\/attach\]','\r\n![cpuwolf]('+ linkpth +')\r\n',line)
			print a
	line=urltolink(line)
	fout.write(line)

allmd.close()
fout.close()
#preprocess is done, let's open it again
fpre=open("out/blog.txt")

wholetext=fpre.read()

wholetextsinglefile=wholetext.split('|||')

idx=1
for stext in wholetextsinglefile:
	try:
		filesec=stext.split(';;;')
	except ValueError:
		print "split done"
	else:
		if len(filesec) > 1 and len(filesec[1].strip()) > 1 and len(filesec[0].strip()) > 1:
			smd=open('out/vip_old'+str(idx)+'.md','w')
			smd.write('---\r\n')
			smd.write(('title: '+filesec[1].strip()+'\r\n'))
			smd.write('date: '+filesec[0].strip()+'\r\n')
			smd.write('---\r\n\r\n')
			smd.write('## '+filesec[1].strip()+'\r\n\r\n')
			smd.write(filesec[2])
			smd.close()
			os.system('iconv -t utf-8 -f gb2312 ' + 'out/vip_old'+str(idx)+'.md' + '> blog/source/_posts/vip_old'+str(idx)+'.md')
		idx=idx+1
fpre.close()
