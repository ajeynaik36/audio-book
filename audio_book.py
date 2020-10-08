import pyttsx3
import PyPDF2


book = open('sql.pdf', 'rb')
audio = pyttsx3.init()
pdfReader = PyPDF2.PdfFileReader(book)

total_pages = pdfReader.numPages
print(total_pages)


for page in range(total_pages):
    page = pdfReader.getPage(page)
    text = page.extractText()
    audio.say(text)
    audio.runAndWait()
