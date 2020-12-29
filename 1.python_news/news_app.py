from python_news import NVParser

import tkinter as tk


class NewsApp(tk.Canvas):
	def __init__(self, root):
		self.width = 600
		self.height = 800

		super().__init__(root, width=self.width, height=self.height)
		self.parser = NVParser("https://nv.ua/allnews.html")
		self.parser.work()
		self.data = self.parser.parsed_data
		self.pack()
		self.set_main_ui()
		self.show_news()


	def set_main_ui(self):
		self.frame = tk.Frame(self, bg='#80c1ff', bd=5)
		self.frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')


		self.refresh_button = tk.Button(self.frame, text="Refresh", command=self.refresh())
		self.refresh_button.place(relx=0.5, rely=0.05, relwidth=0.3, height=40, anchor='n')


	def show_news(self):
		for i, data in enumerate(self.data[:5]):
			entry = tk.Frame(self.frame, bg='#ffffff')
			entry.place(relx=0.5, rely=0.1 + (0.2 * i) + 0.05, relwidth=0.9, relheight=0.2, anchor='n')
			text = f"{data['date']} - {data['tag']} - {data['title']}"
			label = tk.Label(entry, text=text)
			label.pack()



	def refresh(self):
		pass


root = tk.Tk()
news_app = NewsApp(root)
news_app.mainloop()
