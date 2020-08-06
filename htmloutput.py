class output(object):
    def __init__(self):
        self.datas = []
    def collectdata(self,data):
        if data is None:
            return
        self.datas.append(data)
    def put(self):
        fout =open('output.html','w')
        fout.write("<html>")
        fout.write('<body>')
        fout.write('<tr>')
        for data in self.datas:
            fout.write('<td>%s</td>' % data['urls'])
            fout.write('<td>%s</td>' % data['title'])
        fout.write('</tr>')
        fout.write('</body>')
        fout.write('</html>')