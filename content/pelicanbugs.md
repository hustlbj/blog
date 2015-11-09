Title: Pelican和Themes的使用tips
Date: 2015-11-09
Category: 补漏记
Tags: pelican, theme, tags, page

1) 关于tags的显示bug

博文http://www.linuxzen.com/shi-yong-pelicanda-zao-jing-tai-bo-ke.html中关于"写一篇文章"中的md文件写法的描述有误，Tag无法显示，应该改为Tags，参照http://docs.getpelican.com/en/3.6.3/content.html#articles-and-pages。

例如在somearticle.md中Tags: tag1, tag2
则文章的抬头标题栏就可以显示Tags。

如果使用bootstrap2等主题，其源templates中，siderbar.html关于Tags的写法有误，将for tag in tag_cloud改为for tag in tags，才能正常在侧边栏中显示tags。

2) 如何使用page

首先，在content目录下创建pages目录，在pages目录下一般放about和contact等纯静态页面，写一个about.md文件在pages目录下。

Title: About

...

然后，修改pelicanconf.py:

PAGE_PATHS = ['pages']

PAGE_URL = 'pages/{slug}/'

PAGE_SAVE_AS = 'pages/{slug}/index.html'

重新make html

然后就可以访问/pages/about/

3) 在菜单栏显示About项

按照http://docs.getpelican.com/en/3.6.3/settings.html中描述的DISPLAY_PAGES_ON_MENU = True设置以后重新make，bootstrap2等主题还是不能在菜单栏显示PAGES，查看该主题的源码，发现base.html中关于此项是这样写的：

for page in PAGES

改成for page in pages以后再次尝试，就正常显示了。
