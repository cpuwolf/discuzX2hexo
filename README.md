# discuzX2hexo

DiscuzX的论坛关闭了，那么数据库MySQL的帖子要是直接丢弃那就太可惜了。所以我花了一天时间，研究了一下怎么不让这些历史数据浪费。

首先进入mysql，使用数据库ultrax
```
use ultrax;
```
字符集的问题

```
set names utf8;
```
备份一下所有人的联络方式，导出为.csv数据表文件

```
select email,username,password from pre_common_member into outfile '/tmp/mycontact.csv'  fields terminated by ','   optionally enclosed by '"'   lines terminated by '\n'; 
```
这个是重点，导出所有的楼主贴子内容，用';;;'隔离字段，用'|||\r\n'隔离行，以备后续处理

```
select from_unixtime(dateline),subject,message from pre_forum_post where first=1 into outfile '/tmp/mytitle6.csv'  fields terminated by ';;;'   lines terminated by '|||\r\n';
```
最头痛的是帖子里的图片[attach]你需要知道他们所以在路径，而这个路径就放在数据库表格
pre_forum_attachment

```
select aid,tableid from pre_forum_attachment limit 1,6;
```

可惜这个表格只是个所有查询，真正的图片路径在分表格pre_forum_attachment_xx
分表格你可以随便看看

```
select aid,tid,attachment from pre_forum_attachment_9 limit 1,10;
```
下面这段联表查询，我mySQL不太熟，只能用笨办法，导出为csv

```
select * from ((select aid,attachment from pre_forum_attachment_0) union (select aid,attachment from pre_forum_attachment_1) union (select aid,attachment from pre_forum_attachment_2) union (select aid,attachment from pre_forum_attachment_3) union (select aid,attachment from pre_forum_attachment_4) union (select aid,attachment from pre_forum_attachment_5) union (select aid,attachment from pre_forum_attachment_6) union (select aid,attachment from pre_forum_attachment_7) union (select aid,attachment from pre_forum_attachment_8) union (select aid,attachment from pre_forum_attachment_9)) A order by aid into outfile '/tmp/myattachlist.csv'  fields terminated by ','   optionally enclosed by '"'   lines terminated by '\n';
```

Discuz的一些有用的菜单上的链接

```
select url from pre_common_nav;
```

友情链接

```
select * from pre_common_friendlink;
```

现在我拿到了一堆的csv文件，下一步我准备把他们导出为一个个markdown文件，作为博客发布

# Hexo usage

how to post?

hexo new post "title"
