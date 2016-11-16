#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'supercoderX'
import re
import os
#from urlparse3 import urlparse3
import extract_utils as extract_utils
from functools import reduce
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class BodyExtractor(object):
    """
    url:链接地址
    body:正文内容
    depth:行块深度
    """

    def __init__(self, url):
        self.url = url
        self.domain = ''
        self.body = ''    #正文内容
        self.depth = 3    #行块的深度
        self.html = ''
        self.plain_text = ''
        self.html_text = ''
        self.margin = 35  #从text的margin长度开始去匹配text_a_p，数值越大匹配越精确，效率越差

    def execute(self):
        self._pre_process()
        self._extract()
        self._post_process()
        self.body = BeautifulSoup(self.body, 'html5lib').get_text()

    def _pre_process(self):
        html = extract_utils.get_html(self.url)
        self.html = html
        parsed_uri = urlparse(self.url)
        self.domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        plain_text, html_text = clean_html(self.html)
        self.html_text = html_text
        self.plain_text = plain_text

    def _post_process(self):
        """
        把资源链接的相对路径改为完整路径
        清空标签的无用属性，比如class, style
        """
        #TODO: 清空标签无用属性，比如class

        def repl(match):
            s = match.group()
            return s.replace('="', '="' + self.domain)
        self.body = re.sub(r'(?:href=["\']/(.*?)["\'])|(?:src=["\']/(.*?)["\'])', repl, self.body)

    def _extract(self):
        lines = tuple(self.plain_text.split('\n'))
        #lines对应每行的长度
        len_per_lines = [len(re.sub(r'\s+', '', line)) for line in lines]

        #每个块对应的长度
        len_per_blocks = []
        for i in range(len(len_per_lines) - self.depth + 1):
            word_len = sum([len_per_lines[j] for j in range(i, i + self.depth)])
            len_per_blocks.append(word_len)

        text_list = []
        text_begin_list = []
        text_end_list = []

        for i, value in enumerate(len_per_blocks):
            if value > 0:
                text_begin_list.append(i)
                tmp = lines[i]
                while i < len(len_per_blocks) and len_per_blocks[i] > 0:
                    i += 1
                    tmp += lines[i] + "\n"
                text_end_list.append(i)
                text_list.append(tmp)

        result = reduce(lambda str1, str2: str1 if len(str1) > len(str2) else str2, text_list)
        result = result.strip()
        i_start = self._start(result)
        i_end = self._end(result)
        if i_start == 0 or i_end == 0 or i_start > i_end:
            i_start = self._start(result, position=30) - 47
        if i_start < i_end:
            self.body = self.html_text[i_start:i_end]
        else:
            self.body = []
        self.body = ''.join(self.body.splitlines())
        return self.body

    def _start(self, result, position=0):
        i_start = 0
        for i in range(self.margin)[::-1]:
            start = result[position:i + position]
            start = extract_utils.escape_regex_meta(start)
            p = re.compile(start, re.IGNORECASE)
            match = p.search(self.html_text)
            if match:
                s = match.group()
                i_start = self.html_text.index(s)
                break
        return i_start

    def _end(self, result):
        i_end = 0
        for i in range(1, self.margin)[::-1]:
            end = result[-i:]
            end = extract_utils.escape_regex_meta(end)
            p = re.compile(end, re.IGNORECASE)
            match = p.search(self.html_text)
            if match:
                s = match.group()
                i_end = self.html_text.index(s) + len(s)
                break
        return i_end


def clean_html(html):
    """
    清洗html文本，去掉无用标签
    1. "script","style",注释标签<!-->整行用空格代替
    2. 特殊字符转义
    return:(pure_text,html_text):纯文本和包含标签的html文本
    """
    regex = re.compile(
        r'(?:<!DOCTYPE.*?>)|'  #doctype
        r'(?:<head[\S\s]*?>[\S\s]*?</head>)|'
        r'(?:<!--[\S\s]*?-->)|'  #comment
        r'(?:<script[\S\s]*?>[\S\s]*?</script>)|'  # js...
        r'(?:<style[\S\s]*?>[\S\s]*?</style>)', re.IGNORECASE)  # css
    html_text = regex.sub('', html.decode('utf-8'))  #保留html标签
    plain_text = re.sub(r"(?:</?[\s\S]*?>)", '', html_text)  #不包含任何标签的纯html文本
    html_text = extract_utils.html_escape(html_text)
    soup = BeautifulSoup(html_text, 'html5lib')
    plain_text = soup.get_text()

    return plain_text, html_text


if __name__ == "__main__":

    url = 'http://md.tech-ex.com/ired/2016/47848.html'
    url = 'http://md.tech-ex.com/medical/2016/47834.html'
    te = BodyExtractor(url)
    te.execute()
    print(te.body)






