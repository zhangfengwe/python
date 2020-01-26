# xpath学习

from lxml import etree


def func(source):
    # <html><h1>123<small>asd</small></h1></html>
    selector = etree.HTML(source)
    result = selector.xpath('//h1/text()')
    print(result)


if __name__ == '__main__':
    func('<html><h1>123<small>asd</small></h1></html>')




