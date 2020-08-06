import urllib.request as urllib2
class download():
    def down(self,url):
        if url is None:
            return
        response = urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()