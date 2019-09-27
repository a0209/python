"""
    爬取花椒直播下的游戏分类的主播人气并从高到低排序
"""

import re

from urllib import request


class Spider():

    url = 'https://www.huajiao.com/category/805'
    root_pattern = '<div class="username clearfix">([\s\S]*?)</div>'
    name_pattern = '<p class="name fl">([\s\S]*?)</p>'
    number_pattern = '<span class="watches fr">([\s\S]*?)</span>'

    def __fetch_content(self):
        """
        获取页面内容
        :return: htmls()
        """
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        """
        分析数据
        :param htmls: 获取的网页内容
        :return:
        """
        root_html = re.findall(Spider.root_pattern, htmls)

        anchors = []
        for anchor in root_html:
            name = re.findall(Spider.name_pattern, anchor)
            number = re.findall(Spider.number_pattern, anchor)
            html = {'name': name, 'number': number}
            anchors.append(html)
        # print(anchors)
        # print(root_html[0])
        a = 1
        return anchors

    def __refine(self, anchors):
        """
        提炼数据
        :param anchors:
        :return:
        """
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }

        return map(l, anchors)

    def __sort(self, anchors):
        """
        排序
        :param anchors:
        :return:
        """
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        """
        展示数据
        :param anchors:
        :return:
        """
        for rank in range(0, len(anchors)):
            print(
                'rank : ' + str(rank+1) + anchors[rank]['name'] + '----' + anchors[rank]['number']
            )

    def go(self):
        """
        入口(控制)
        :return:
        """
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        anchors = self.__show(anchors)
        # print(anchors)


spider = Spider()
spider.go()
