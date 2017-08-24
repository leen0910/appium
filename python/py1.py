import urllib.request
#print(urllib.__file__)
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.163.com")

print(html)