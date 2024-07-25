from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

n = int(input())

'''
for _ in range(n):
    par = MyHTMLParser()
    par.feed(input())
'''

_feed = ""
for _ in range(n):
  _feed += input()
p = MyHTMLParser()
p.feed(_feed)