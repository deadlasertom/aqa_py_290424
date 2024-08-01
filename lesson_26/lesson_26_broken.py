from lxml import etree
from io import StringIO


broken_html = """<html><head>
<title>test<body><h1>page title</h1>
<a href='mailto:my@mail.com' rel='my@mail.com'>click me</a>
<p class='abc' > some text
<div id="xyz"> text </div>  <p class="">невірний, покоцаний html
""" # невірний покоцаний хтмл

def clean_html(broken_html):
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(broken_html), parser)  # перетворюєм в зрозумілу структуру
    result = etree.tostring(tree.getroot(),
                            pretty_print=True,
                            method="html")  # звороне перетворення - обєкт дерева у строку
    print(result.decode("utf-8"))
    with open("index.html", "w") as f:
        f.write(str(result, encoding="utf8"))

clean_html(broken_html)