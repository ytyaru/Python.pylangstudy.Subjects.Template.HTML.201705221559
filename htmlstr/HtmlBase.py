#!python3
#encoding: utf-8
import htmlstr.HtmlWrapper
class HtmlBase(object):
    def __init__(self):
        self.__wrapper = htmlstr.HtmlWrapper.HtmlWrapper()

    """
    HTML文書文字列を生成する。
    @param {str} bodyは<body>に含めるHTML文字列。
    @param {str} headは<head>に含めるHTML文字列。
    @param {dict} metaは<meta>に入れるデータ。次のキーを持ったdict型。'charset', 'description', 'author', 'viewport', 'title', 'icon_href', 'css_href'
    """
    def CreateHtml(self, body, head=None, meta=None):
        return '''<!DOCTYPE html>
{html}
<head>
<meta charset="{charset}">
<meta name="description" content="{description}">
<meta name="author" content="{author}">
<meta name="viewport" content="{viewport}">
<title>{title}</title>
{icon_href}
{css}
{head}
</head>
<body>{body}</body>
</html>'''.format(
        html=self.__CreateHtmlStartTag(meta), 
        charset=self.__GetCharset(meta), 
        description=self.__GetDescription(meta), 
        author=self.__GetAuthor(meta),
        viewport=self.__GetViewport(meta),
        title=self.__GetTitle(meta),
        icon_href=self.__GetIcon(meta),
        css=self.__GetCss(meta),
        head=self.__GetHead(head),
        body=body
        )

    def __CreateHtmlStartTag(self, meta):
        if meta and 'lang' in meta and meta['lang']:
            return '<html lang="{0}">'.format(meta['lang']) # meta['lang'] = 'ja' など。
        else:
            return '<html>'
    def __GetCharset(self, meta):
        if meta and 'charset' in meta and meta['charset']:
            return meta['charset']
        else:
            return 'utf-8'
    def __GetDescription(self, meta):
        if meta and 'description' in meta and meta['description']:
            return meta['description']
        else:
            return ''
    def __GetAuthor(self, meta):
        if meta and 'author' in meta and meta['author']:
            return meta['author']
        else:
            return ''
    def __GetViewport(self, meta):
        if meta and 'viewport' in meta and meta['viewport']:
            return meta['viewport']
        else:
            return ''
    def __GetTitle(self, meta):
        if meta and 'title' in meta and meta['title']:
            return meta['title']
        else:
            return ''
    def __GetIcon(self, meta):
        if meta and 'icon_href' in meta and meta['icon_href']:
            return '<link rel="shortcut icon" href="{0}">'.format(meta['icon_href'])
        else:
            return ''
    def __GetCss(self, meta):
        if meta and 'css_href' in meta and meta['css_href']:
            if isinstance(meta['css_href'], (list, tuple)):
                css_str = ''
                for path in meta['css_href']:
                    css_str += '<link rel="stylesheet" href="{0}">'.format(path)
                return css_str
            if isinstance(meta['css_href'], str):
                return '<link rel="stylesheet" href="{0}">'.format(meta['css_href'])
        else:
            return ''
    def __GetHead(self, head):
        if head:
            return head
        else:
            return ''
