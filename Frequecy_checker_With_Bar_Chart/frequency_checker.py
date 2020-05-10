import matplotlib.pyplot as plt

class Document:
	def __init__(self,file):
		self.file=file
		with open(self.file ,'r') as f:
			self.data=f.read()

	def read_character(self):
		self.count_=[]
		for self.chars in self.data:			
			self.count=self.data.count(self.chars)
			self.count_.append(self.count)		

	def pie_chart(self):		
		x=list(self.data)			
		plt.title("Character Frequency Chart")
		plt.bar(x,self.count_)
		plt.ylabel("Character Frequency")
		plt.show()
	

d=Document("file.txt")
d.read_character()
d.pie_chart()

