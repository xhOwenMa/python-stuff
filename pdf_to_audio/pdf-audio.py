import pyttsx3
from pypdf import PdfReader

reader = PdfReader("book.pdf")
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) # set the voice to Zira - one of the Microsoft built-in voices
# use voice.py the find the voice you like
text = ""

for page in reader.pages:
    clean_text = page.extract_text().strip().replace('\n', ' ')
    text += clean_text + "\n"
    
speaker.save_to_file(text, 'story.mp3')

speaker.runAndWait()

speaker.stop()
