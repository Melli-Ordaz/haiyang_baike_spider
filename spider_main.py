import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
	def __init__(self):#初始化下载所需要的url管理器 下载器 解析器 输出器
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def is_not_en_word(self, word: str):
		'''
        判断一个词是否是非英文词,只要包含一个中文，就认为是非英文词汇
        :param word:
        :return:
        '''
		count = 0
		for s in word.encode('utf-8').decode('utf-8'):
			if u'\u4e00' <= s <= u'\u9fff':
				count += 1
				break
		if count > 0:
			return True
		else:
			return False


	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url) #获取url
		while self.urls.has_new_url():
			new_url = self.urls.get_new_url()#当前爬取的url
			print('craw %d : %s' % (count, new_url)) #记录当前爬取的第几个url
			if self.is_not_en_word(new_url):
				continue
			html_cont = self.downloader.download(new_url)#下载好的数据
			new_urls, new_data = self.parser.parse(new_url, html_cont)#new_urls为解析后的新url数据
			self.urls.add_new_urls(new_urls)
			self.outputer.collect_data(new_data)

			if count == 20:
				break

			count = count+1
		self.outputer.output_html()


if __name__ == '__main__':
	#以小鹰号航母为例
	root_url = "https://baike.baidu.com/item/%E5%B0%8F%E9%B9%B0%E5%8F%B7%E8%88%AA%E7%A9%BA%E6%AF%8D%E8%88%B0?fromtitle=%E5%B0%8F%E9%B9%B0%E5%8F%B7&fromid=3265116&fromModule=lemma_search-box" #入口URL
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)#启动爬虫
