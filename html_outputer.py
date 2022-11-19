class HtmlOutputer(object):
	def __init__(self):
		self.datas = []


	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):#将收集的数据输出到一个html文件里
		fout = open('output.html', 'w')

		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')

		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" % data["url"])
			fout.write("<td>%s</td>" % data["title"])
			fout.write("<td>%s</td>" % data["summary"])
			fout.write("</tr>")


		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')

		fout.close()
