from urllib.parse import urljoin
import urllib.request as urllib2
from bs4 import BeautifulSoup
import urllib.parse as parse
import re
import sys

sys.setrecursionlimit(10000)

if __name__ == '__main__':
    # http://www.gzgtjt.com/news/class/index.php?page=1&catid=95
    urls = []
    for i in range(1, 13):
        url = 'http://www.gzgtjt.com/news/class/index.php?catid=95&apge='
        # 新的url
        url = url + str(i)
        # 该urls是列表所在的url，还需要获取到内容页面的url
        urls.append(url)
    data_urls = []
    for url in urls:
        if url is not None:
            response = urllib2.urlopen(url)
            content = response.read()
            if response.getcode() == 200:
                soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
                url_divs = soup.find_all(name='div', attrs='title')
                # print(url_div)
                for url_div in url_divs:
                    content_url = url_div.find('a', href=re.compile(r'/*news*/'))
                    new_url = content_url['href']
                    # print(content_url)
                    if re.search('http', new_url) == None:
                        new_full_url = urljoin('http://www.gzgtjt.com/', new_url)
                    else:
                        new_full_url = new_url
                    data_urls.append(new_full_url)
    datas = []
    i = 0
    for data_url in data_urls:
        i = i + 1
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            'Host': 'http://www.gzgtjt.com/'
        }
        headers = parse.urlencode(headers)
        data_request = urllib2.Request(data_url)
        data_response = urllib2.urlopen(data_request)
        data_content = data_response.read()
        if data_response.getcode() == 200:
            soup = BeautifulSoup(data_content, 'html.parser', from_encoding='utf-8')
            data = {}
            news_content = soup.find('div', id='con')
            news_title = soup.find(name='div', attrs='newstitle')
            news_info = soup.find(name='div', attrs='info')
            data['content'] = str(news_content)
            data['info'] = str(news_info.string)
            data['title'] = str(news_title.string)
            datas.append(data)
        print('第' + str(i) + '次循环')
    # print(datas)
    fobj = open('./data95.json', 'w',encoding='utf-8')
    datas=str(datas)
    fobj.write(datas)
    fobj.close()
