import PyPDF2 
import requests
from io import BytesIO

# Open the PDF file from internet
response = requests.get("https://cdn.fulltextarchive.com/wp-content/uploads/wp-advanced-pdf/1/Sense-and-Sensibility-by-Jane-Austen.pdf")
if response.status_code == 200:
	file_handle = BytesIO(response.content)
else:
	raise ValueError("Failed to fetch the PDF file. Status code: {}".format(response.status_code))

# Create a PDF reader object reader
pdfReader = PyPDF2.PdfReader(file_handle)

# Create a dictionary to store all words
frequency_table = dict()

# Read each page of the PDF
for page in pdfReader.pages:
    text = page.extract_text()
    # Read all words in the text
    lines = text.replace('--', '\n').split('\n')
    for words in lines:
        words = words.split()
        for word in words:
            word = word.lower().strip('1234567890#.,!?()[]{};:"\'')  # Normalize the word
            if word in frequency_table:
                frequency_table[word] += 1
            else:
                frequency_table[word] = 1

# prints out the frequency table
for word, frequency in frequency_table.items():
    print(f"{word}: {frequency}")