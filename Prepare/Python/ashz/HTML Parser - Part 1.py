# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in range(len(attrs)):
            print("-> " + str(attrs[i][0]) + " > " + str(attrs[i][1]))
 
    def handle_endtag(self, tag):
        print("End   :", tag)
 
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in range(len(attrs)):
            print("-> " + str(attrs[i][0]) + " > " + str(attrs[i][1]))

N = int(input())

a = ""
for _ in range(N):
    a += input()
 
parser = MyHTMLParser()
parser.feed(a)
