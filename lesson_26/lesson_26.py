import requests 
# import lxml.html
from lxml.html import fromstring, fragment_fromstring
from lxml import etree


def get_page(url):
    r = requests.get(url)
    return r.content

def get_by_xpath(html_content, x_path):
    tree = fromstring(html_content)
    text = tree.xpath(x_path)
    return text

def get_by_class(html_content, css_class):
    tree = fromstring(html_content)
    text = tree.find_class(css_class)
    return text


if __name__ == "__main__":
    url = "https://lxml.de/index.html"
    html_content = get_page(url)
    #print(html_content)

    xpath = '//*[@id="introduction"]//text()'
    text_introduction = get_by_xpath(html_content, xpath)
    print(text_introduction)

    css_class = "title"
    text_class = get_by_class(html_content, css_class)
    print(text_class)
    print(text_class[0].attrib, text_class[0].text)
    