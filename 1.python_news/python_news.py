from bs4 import BeautifulSoup
import requests
import  psycopg2


class BaseParser():
	def __init__(self, url):
		self.url = url
		self.raw_html = None
		self.parsed_data = list()


	def work(self):
		try:
			self._get_html()
		except RuntimeError as e:
			print(f"Parsing failed: {e}")
			return False
		self.parsed_data.clear()

		try:
			self._parse_html()
		except RuntimeError as e:
			return False

		try:
			self._save_data()
		except RuntimeError as e:
			return False


		return True

	def _get_html(self):
		"""
		Will fetch raw HTML from the given url.
		"""
		try:
			response = requests.get(self.url)		
		except Exception as e:
			raise RuntimeError(f"Failled to get raw HTML, reason: {e}")
		
		if response.status_code != 200:
			raise RuntimeError(f"Failled to get raw HTML, code: {response.status_code}")
		
		self.raw_html = response.text

	def _parse_html(self):
		"""
		Will parse data from raw HTML
		"""

		raise NotImplementedError()

	def _save_data(self):
		with psycopg2.connect("dbname=hillel4 user=postgres") as connection:
			cursor = connection.cursor()
			cursor.execute("SELECT * FROM news")

class NVParser(BaseParser):
	# def __init__(self):
	# 	pass


	def _parse_html(self):
		soup = BeautifulSoup(self.raw_html, 'html.parser')
		news_block_list = soup.find_all('div', attrs={'class': 'one_result'})

		for block in news_block_list:
			record = dict()
			

			title_element = block.find('span', attrs={'class': 'search__article_title'})
			raw_title = title_element.get_text().encode('iso-8859-1').decode('utf8')
			raw_title = raw_title.strip().replace('\xa0', ' ')
			record['title'] = raw_title
			

			tag_element = block.find('div', attrs={'class': 'atom__additional_category'})
			raw_tag = tag_element.get_text().encode('iso-8859-1').decode('utf8')
			record['tag'] = raw_tag


			data_element = block.find('div', attrs={'class': 'atom__additional_pubDate'})
			raw_date = data_element.get_text().encode('iso-8859-1').decode('utf8')
			record['date'] = raw_date


			url_element = block.find('a', attrs={'class':'result'})
			record['url'] = url_element['href']

			
			self.parsed_data.append(record)





if __name__ == '__main__':
	nvp = NVParser("https://nv.ua/allnews.html")
	nvp.work()
	news = nvp.parsed_data
	print(news)