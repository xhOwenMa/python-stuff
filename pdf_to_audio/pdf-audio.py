import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) # set the voice to Zira - one of the Microsoft built-in voices
# use voice.py to find the voice you like

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    
speaker.save_to_file(clean_text, 'story.mp3')

speaker.runAndWait()

speaker.stop()
