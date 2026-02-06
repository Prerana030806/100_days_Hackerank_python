from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print(f"-> {name} > {value}")
parser = MyParser()
n = int(input())
for _ in range(n):
    parser.feed(input())
