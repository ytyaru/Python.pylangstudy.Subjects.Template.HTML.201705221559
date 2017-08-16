#!python3
#encoding: utf-8
import os.path
from htmlstr.HtmlBase import HtmlBase
from subjects.CodeOnly import CodeOnly
from subjects.CodeCompare import CodeCompare
from subjects.CodeList import CodeList
class Run(object):
    def __init__(self):
        self.__base = HtmlBase()
        
    def CreateHtmlCodeList(self):
        breadcrumbs_data = {
            'directional_icon_type': 'FontAwesome',
            'datas': [
                {'text': '孫', 'href': 'http://2'},
                {'text': '子', 'href': 'http://1'},
                {'text': '親', 'href': 'http://0'}],
            'is_child_first': True
        }
        metanavi_data = {
            'pydoc': {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
            'env': {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
            'github': {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'}
        }
        c = CodeList()
        title = '課題1のタイトル'
        content = '<h1>{0}</h1>'.format(title)
        content += c.CreateHtml(
            breadcrumbs_data, 
            metanavi_data,
            { 'directional_icon_type': 'FontAwesome',
              'prev': {'text': '前のページ', 'href': 'http://prev'},
              'next': {'text': '次のページ', 'href': 'http://next'} },
            [
                { 'path': '0.py', 'lines': [3, 7] },
                { 'path': 'left.py', 'lines': [3, 7] },
                { 'path': 'right.py', 'lines': [3, 7] }
            ])
        content += self.__GetHighLight()
        html = self.__base.CreateHtml(
            content, 
            meta={
                'title': title, 
                'description': '課題1の説明文。', 
                'author': '課題1の著者', 
                'css_href': [
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                    'https://fonts.googleapis.com/css?family=Open+Sans:300,300italic,400,400italic,600,600italic%7CNoto+Serif:400,400italic,700,700italic%7CDroid+Sans+Mono:400,700',
                    'ul.css',
                    'Breadcrumbs.css',
                    'NextPrevNavi.css',
                    'HeaderNavi.css'
            ]})
        return html
    def CreateHtmlCodeCompare(self):
        breadcrumbs_data = {
            'directional_icon_type': 'FontAwesome',
            'datas': [
                {'text': '孫', 'href': 'http://2'},
                {'text': '子', 'href': 'http://1'},
                {'text': '親', 'href': 'http://0'}],
            'is_child_first': True
        }
        metanavi_data = {
            'pydoc': {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
            'env': {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
            'github': {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'}
        }
        c = CodeCompare()
        title = '課題1のタイトル'
        content = '<h1>{0}</h1>'.format(title)
        content += c.CreateHtml(
            breadcrumbs_data, 
            metanavi_data,
            { 'directional_icon_type': 'FontAwesome',
              'prev': {'text': '前のページ', 'href': 'http://prev'},
              'next': {'text': '次のページ', 'href': 'http://next'} },
            { 'left': { 'title': 'python2', 'path': 'left.py', 'lines': [3, 7] },
              'right': { 'title': 'python3', 'path': 'right.py', 'lines': [3, 7] }})
        content += self.__GetHighLight()
        html = self.__base.CreateHtml(
            content, 
            meta={
                'title': title, 
                'description': '課題1の説明文。', 
                'author': '課題1の著者', 
                'css_href': [
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                    'https://fonts.googleapis.com/css?family=Open+Sans:300,300italic,400,400italic,600,600italic%7CNoto+Serif:400,400italic,700,700italic%7CDroid+Sans+Mono:400,700',
                    'ul.css',
                    'Breadcrumbs.css',
                    'NextPrevNavi.css',
                    'HeaderNavi.css'
            ]})
#        print(html)
        return html
    def CreateHtmlCodeOnly(self):
        breadcrumbs_data = {
            'directional_icon_type': 'FontAwesome',
            'datas': [
                {'text': '孫', 'href': 'http://2'},
                {'text': '子', 'href': 'http://1'},
                {'text': '親', 'href': 'http://0'}],
            'is_child_first': True
        }
        metanavi_data = {
            'pydoc': {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
            'env': {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
            'github': {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'}
        }
        c = CodeOnly()
        title = '課題1のタイトル'
        content = '<h1>{0}</h1>'.format(title)
        content += c.CreateHtml(
            breadcrumbs_data, 
            metanavi_data,
            { 'directional_icon_type': 'FontAwesome',
              'prev': {'text': '前のページ', 'href': 'http://prev'},
              'next': {'text': '次のページ', 'href': 'http://next'} },
            { 'path': '0.py', 'lines': [3, 7] })
        content += self.__GetHighLight()
        html = self.__base.CreateHtml(
            content, 
            meta={
                'title': title, 
                'description': '課題1の説明文。', 
                'author': '課題1の著者', 
                'css_href': [
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                    'https://fonts.googleapis.com/css?family=Open+Sans:300,300italic,400,400italic,600,600italic%7CNoto+Serif:400,400italic,700,700italic%7CDroid+Sans+Mono:400,700',
                    'ul.css',
                    'Breadcrumbs.css',
                    'NextPrevNavi.css',
                    'HeaderNavi.css'
            ]})
#        print(html)
        return html

    def __GetHighLight(self):
        return '<link rel="stylesheet" href="highlight/styles/atom-one-dark.min.css"><script src="highlight/highlight.min.js"></script><script>hljs.initHighlighting()</script>'


if __name__ == '__main__':
    r = Run()
    r.CreateHtmlCodeOnly()
    r.CreateHtmlCodeCompare()
    r.CreateHtmlCodeList()
    path_this = os.path.join(os.path.abspath(os.path.dirname(__file__)))
    with open(os.path.join(path_this, 'htmlstr/test_code_only.html'), 'w') as f:
        f.write(r.CreateHtmlCodeOnly())
    with open(os.path.join(path_this, 'htmlstr/test_code_compare.html'), 'w') as f:
        f.write(r.CreateHtmlCodeCompare())
    with open(os.path.join(path_this, 'htmlstr/test_code_list.html'), 'w') as f:
        f.write(r.CreateHtmlCodeList())
