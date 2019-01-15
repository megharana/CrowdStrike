import urllib.request as urllib2
import html2text


def generate_file():
    page = urllib2.urlopen("http://hck.re/tHEZGP")
    html_content = page.read()
    rendered_content = html2text.html2text(str(html_content))
    file = open('fileToPush.js', 'w')
    file.write(rendered_content)
    file.close()
