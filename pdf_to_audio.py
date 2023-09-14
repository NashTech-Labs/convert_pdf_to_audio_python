import PyPDF2
from gtts import gTTS

#Open the PDF file
pdf_file = open('/home/ec2-user/file.pdf','rb')
pdfreader = PyPDF2.PdfReader(pdf_file)

#Initialize variables to store extracted text
text = ''

#Extract text from each page of the PDF
for page_num in range(len(pdfreader.pages)):
    page = pdfreader.pages[page_num]
    text += page.extract_text()

#Close the PDF File    
pdf_file.close()

#Create a gTTS object and save the audio to a file
tts = gTTS(text)
tts.save('output.mp3')

print("PDF converted to audio successfully!")
