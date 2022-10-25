#pyPDF2 module
import PyPDF2
pdf_File=open("116.pdf", "rb")
pdf_reader=PyPDF2.PdfFileReader(pdf_File)
text = pdf_reader.getPage(0).extractText()
print(text)