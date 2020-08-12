import urlmanage
import htmldownload
import htmlparser
import htmloutput
url="http://www.gzgtjt.com/news/class/index.php?page=1&catid=86"
# http://www.gzgtjt.com/news/class/index.php?page=3&catid=95
#这是列表的选项，catid=95代表是党建纪检、catid=86代表是公司动态、catid=97代表是企业文化、catid=100代表是法律法规、catid=104代表是通知公告
# url="https://baidu.com/"
class SpiderMain(object):
    def __init__(self):
        self.urls = urlmanage.manage()
        self.htmldownload = htmldownload.download()
        self.htmloutput = htmloutput.output()
        self.htmlparser = htmlparser.parser()

    def craw(self, url):
        self.urls.addurl(root_url)
        while self.urls.hasurl():
            new_url = self.urls.geturls()
            content = self.htmldownload.down(new_url)
            # print(content)
            new_urls, new_data = self.htmlparser.parse(new_url, content)
            self.htmloutput.collectdata(new_data)
            self.htmloutput.put()


if __name__ == '__main__':
    root_url = url
    spidermain = SpiderMain()
    spidermain.craw(root_url)
