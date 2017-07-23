from lxml import html
import requests


def get_page(url = 'http://joyreactor.cc/tag/JaGo'):
    r = requests.get(url)
    with open('page.txt','w') as f:
        try:
            if r.status_code == 200:
                page = r.text
                return page
            else:
                print(r.status_code)
                f.write(r.status_code + '/n')
                return None
        except FileNotFoundError:
            print("File does't exist.")

def parse_page(page):
    result = []
    if not page:
        return
    path = './/span[@class = "link_wr"]/a/@href'
    doc = html.document_fromstring(page)
    value = doc.xpath(path)
    for val in value:
        result.append(val)
    latest_res = 'http://joyreactor.cc/' + result[0]
    return latest_res

def get_post():
    page = get_page()
    res = parse_page(page)
    return res

    
