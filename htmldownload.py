import urllib.request as urllib2
import urllib.parse as parse

class download():
    def down(self, url):
        if url is None:
            return
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            'Host': 'http://www.gzgtjt.com/'
        }
        headers=parse.urlencode(headers)
        request = urllib2.Request(url)
        # print(request)
        response = urllib2.urlopen(request)
        # print(response.read().decode('utf-8'))
        if response.getcode() != 200:
            return None
        return response.read().decode('utf-8')
