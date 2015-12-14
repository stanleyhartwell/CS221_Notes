from bs4 import BeautifulSoup
from subprocess import call

f = open("./index.html","r")
file_text = f.read()
bs_text = BeautifulSoup(file_text,'html.parser')
f.close()
pdf_spans = bs_text.findAll('span', {'class': 'pdfLink'})
prefix = "http://web.stanford.edu/class/cs221/"
lectureCounter = 0
for span in pdf_spans:
	lectureCounter = lectureCounter + 1
	a = span.find_all("a")[0]
	ref = a["href"]
	url = prefix + ref
	title = ref.split("/")[1]
	newTitle = str(lectureCounter) + "_" + title
	call(["wget", url])
	call(["mv", title, newTitle])
