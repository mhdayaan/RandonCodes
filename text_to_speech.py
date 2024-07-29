from gtts import gTTS 
import os
import PyPDF2 
import requests 
file_url = input("Enter the url of the file you want to listen to:")
  
req = requests.get(file_url, stream = True) 
  
with open("example.pdf","wb") as pdf: 
    for chunk in req.iter_content(chunk_size=1024): 
  
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk)   
# creating a pdf file object 
pdfFileOb = open('example.pdf', 'rb')   
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileOb)   
# creating a page object 
pageOb = pdfReader.getPage(0) 
text = pageOb.extractText()
language = "en"
speech = gTTS(text = text, lang = language, slow = False)
speech.save("text.mp3")
os.system("start text.mp3")