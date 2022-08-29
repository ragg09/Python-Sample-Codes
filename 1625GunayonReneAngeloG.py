class Book(object):
	def __init__(self,title,author_name,publisher):
		self.title = title
		self.author_name = author_name
		self.publisher = publisher
	def	get_title(self):
		return self.title

	def get_author(self):
		return self.author_name

	def get_publisher(self):
		return self.publisher

	def set_title(self,title):
		self.title = title

	def set_author(self,author):
		self.author_name = author

	def set_publisher(self,publisher):
		self.publisher = publisher

title_book = raw_input("Book title: ")
author_book = raw_input("Book's author: ")
publisher_book = raw_input("Publisher's name: ")
test_book = Book(title_book,author_book,publisher_book)
test_book.set_title(title_book)
test_book.set_author(author_book)
test_book.set_publisher(publisher_book)
print("\n"+ "Information/s: ")
print("Title of book: " + test_book.get_title())
print("Author/s of the book is/are: " + test_book.get_author())
print("Publisher's name is: " + test_book.get_publisher())	