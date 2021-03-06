# -*- coding: utf-8 -*-
"""
Created on July 2017

@author: Wei Shuai <cpuwolf@gmail.com>
"""

import re

attachlist = []

# get attachment list
# format
# 2,"201505/06/160507sxu6iuwaawpaay7b.jpg"
# 3,"201505/07/172718j6ntgnfv7snttnfy.jpg"
#
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
    line=re.sub(r'\[media\=(.[^\[]*)\](.*)\[\/media\]',r'[\2](\2)',line)
    line=re.sub(r'\[media\](.*)\[\/media\]',r'[\1](\1)',line)
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
# format
#
# 2015-05-01 13:57:56;;;title;;;content
#

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

#convert GBK to UTF-8 file
def convutf8(ipath, opath):
    outf=open(opath, "w")
    inf=open(ipath ,"rU")
    tmpstr=inf.read()
    tmpwstr=tmpstr.decode("GBK").encode("UTF-8")
    outf.write(tmpwstr)
    inf.close()
    outf.close()
    
mytaglist=[u"视频",u"更新",u"地景",u"计算",u"放出",u"消息",u"插件",u"地形",u"免费"]

mycatelist=[[u"导航数据",[u"导航数据"]],
            [u"插件飞机",[u"737",u"757",u"320",u"777",u"727",u"767",u"插件"]],
            [u"插件地景",[u"机场",u"地景",u"插件",u"地形"]],
            [u"教程",[u"设置",u"计算",u"安装",u"下载"]],
            [u"新闻",[u"发布",u"放出",u"购买",u"美金"]],
            ]
            
def gencategery(opath, t_gbk):
    opath.write("categories:\n")
    for cate in mycatelist:
        for kword in cate[1]:
            res=re.search(kword,t_gbk)
        if res:
            opath.write("- "+cate[0].encode("GBK")+"\n")
            return

def writetagcat(ofile,text):
    textgbk = unicode(text, "gbk")  
    gencategery(ofile, textgbk)

    ofile.write("tags:\n")
    for cate in mytaglist:
        rest=re.search(cate,textgbk)
        if rest:
            ofile.write("- "+cate.encode("GBK")+"\n")
    

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
            writetagcat(smd,filesec[1].strip()+filesec[2].strip())
            smd.write('---\n\n')
            smd.write(filesec[2])
            smd.close()
            # input file => output file
            convutf8('out/vip_old'+str(idx)+'.md', 'blog/source/_posts/forum_old'+str(idx)+'.md')
            #user external linux command to convert gb2312 to utf-8
            #os.system('iconv -c -t utf-8 -f gb2312 ' + 'out/vip_old'+str(idx)+'.md' + '> blog/source/_posts/forum_old'+str(idx)+'.md')
        idx=idx+1
fpre.close()
