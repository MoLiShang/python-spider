import urlmanage
import htmldownload
import htmlparser
import htmloutput
class SpiderMain(object):
    def __init__(self):
        self.urls = urlmanage.manage()
        self.htmldownload = htmldownload.download()
        self.htmloutput = htmloutput.output()
        self.htmlparser = htmlparser.parser()
    def craw(self,url):
        self.urls.addurl(root_url)
        while self.urls.hasurl():
            new_url = self.urls.geturls()
            content = self.htmldownload.down(new_url)
            new_urls,new_data = self.htmlparser.parse(new_url,content)
            self.htmloutput.collectdata(new_data)
            self.htmloutput.put()




if __name__ == '__main__':
    root_url = 'http://baidu.com'
    spidermain = SpiderMain()
    spidermain.craw(root_url)