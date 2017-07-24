# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: Wei Shuai <cpuwolf@gmail.com>
"""

import re
import codecs
import os
import io

attachlist = []

# get attachment list
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

# preprocess marks
def preproc(line):
    #convert url to link
    #[url=A]B[/url]   =>   [B](A)
    #[url]A[/url]  => [](A)
    line=re.sub(r'\[url\=(.[^\[]*)\](.*)\[\/url\]',r'[\2](\1)',line)
    line=re.sub(r'\[url\](.*)\[\/url\]',r'[\1](\1)',line)
    #[media=A]B[/media]  => [B](A)
    line=re.sub(r'\[media\=(.[^\[]*)\](.*)\[\/media\]',r'{% iframe \2 [320] [240] %}',line)
    line=re.sub(r'\[media\](.*)\[\/media\]',r'{% iframe \1 [320] [240] %}',line)
    #[flash=A]B[/flash]  => [B](A)
    line=re.sub(r'\[flash\=(.[^\[]*)\](.*)\[\/flash\]',r'<embed src="\2" height="240" width="320"/>',line)
    line=re.sub(r'\[flash\](.*)\[\/flash\]',r'<embed src="\1" height="240" width="320"/>',line)
    #[img]
    line=re.sub(r'\[img\=(.[^\[]*)\](.*)\[\/img\]',r'\n![](\2)\n',line)
    line=re.sub(r'\[img\](.*)\[\/img\]',r'\n![](\1)\n',line)
     #[p]
    line=re.sub(r'\[p\=(.[^\[]*)\](.*)\[\/p\]',r'\2',line)
    line=re.sub(r'\[p\](.*)\[\/p\]',r'\1',line)
    #[size]
    line=re.sub(r'\[size\=(.[^\[]*)\](.*)\[\/size\]',r'\2',line)
    line=re.sub(r'\[size\](.*)\[\/size\]',r'\1',line)
    #[yun]A[/yun]  => [](A)
    line=re.sub(r'\[yun\=(.[^\[]*)\](.*)\[\/yun\]',r'[password:\2](\1)',line)
    line=re.sub(r'\[yun\](.*)\[\/yun\]',r'[\1](\1)',line)
    #[font]
    line=re.sub(r'\[font\=(.[^\[]*)\](.*)\[\/font\]',r'\2',line)
    line=re.sub(r'\[font\](.*)\[\/font\]',r'\1',line)
    #[b]
    line=re.sub(r'\[b\](.*)\[\/b\]',r'**\1**',line)
    #[i=s]
    line=re.sub(r'\[i\=s\](.*)\[\/i\]',r'\n',line)
    #[backcolor]
    line=re.sub(r'\[backcolor\=(.[^\[]*)\](.*)\[\/backcolor\]',r'\2',line)
    line=re.sub(r'\[backcolor\](.*)\[\/backcolor\]',r'\1',line)
    #[color]
    line=re.sub(r'\[color\=(.[^\[]*)\](.*)\[\/color\]',r'\2',line)
    line=re.sub(r'\[color\](.*)\[\/color\]',r'\1',line)
     #[align]
    line=re.sub(r'\[align\=(.[^\[]*)\](.*)\[\/align\]',r'\2',line)
    line=re.sub(r'\[align\](.*)\[\/align\]',r'\1',line)
     #[list]
    line=re.sub(r'\[list\=(.[^\[]*)\](.*)\[\/list\]',r'\2',line)
    line=re.sub(r'\[list\](.*)\[\/list\]',r'\1',line)
     #[hide]
    line=re.sub(r'\[hide\=(.[^\[]*)\](.*)\[\/hide\]',r'\2',line)
    line=re.sub(r'\[hide\](.*)\[\/hide\]',r'\1',line)


    #remove all other alone no parm headers like [header=xx]
    line=re.sub(r'\[font\=(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[color\=(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[size\=(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[align\=(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[list\=(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[backcolor\=(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[p(.[^\[]*)\]',r'',line)
    line=re.sub(r'\[b\]',r'',line)
    line=re.sub(r'\[hide\]',r'',line)
    line=re.sub(r'\[list\]',r'',line)
    line=re.sub(r'^\[\*\]',r'* ',line)
     #remove all other alone footers like [/footer]
    line=re.sub(r'\[\/(.[^\[]*)\]',r'\n',line)
    return line


# input file
allmd=open("mytitle6.csv", 'rU')
# output file
fout=open("out/preblog.txt", "w")

for line in allmd.readlines():
    #convert attach to markdown image
    nl = re.findall('\[attach\](\d+)\[\/attach\]', line)
    if nl:
        for a in nl:
            linkpth='/images/data/attachment/' + id2src(a).replace('"','')
            line=re.sub(r'\[attach\]'+a+'\[\/attach\]','\n![cpuwolf]('+ linkpth +')\n',line)
            print a
    line=preproc(line)
    fout.write(line)

allmd.close()
fout.close()


#preprocess is done, let's open it again
def convutf8(ipath, opath):
    outf=open(opath, "w")
    inf=open(ipath ,"rU")
    tmpstr=inf.read()
    tmpwstr=tmpstr.decode("GBK").encode("UTF-8")
    outf.write(tmpwstr)
    inf.close()
    outf.close()

# input file
fpre=open("out/preblog.txt" ,"rU")

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
            smd.write('---\n')
            smd.write(('title: '+filesec[1].strip()+'\n'))
            smd.write('date: '+filesec[0].strip()+'\n')
            smd.write('---\n\n')
            smd.write(filesec[2])
            smd.close()
            convutf8('out/vip_old'+str(idx)+'.md', 'blog/source/_posts/forum_old'+str(idx)+'.md')
            #os.system('iconv -c -t utf-8 -f gb2312 ' + 'out/vip_old'+str(idx)+'.md' + '> blog/source/_posts/forum_old'+str(idx)+'.md')
        idx=idx+1
fpre.close()
