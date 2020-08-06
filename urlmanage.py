# url管理器：在new_urls中增加url，urls，判断urls中是否有url，若有才能取出，否则无法取出
class manage():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def addurl(self, url):
        if url is None:
            return
        if url not in self.new_urls or url not in self.old_urls:
            self.new_urls.add(url)

    def addurls(self, urls):
        if len(urls) == 0 or urls is None:
            return
        for url in urls:
            self.addurl(url)

    def hasurl(self):
        return len(self.new_urls) != 0

    def geturls(self):
        if (len(self.new_urls) != 0):
            new_url = self.new_urls.pop()
            self.old_urls.add(new_url)
        return new_url
