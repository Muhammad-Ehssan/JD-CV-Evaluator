from PyPDF2 import PdfReader 

def get_pdf_text(file_path):
    # creating a pdf reader object 
    reader = PdfReader(file_path) 

    text = ""
    for i in range(len(reader.pages)):
        page = reader.pages[i]         
        page_text = page.extract_text() 
        text = text + page_text #+ "\n"
    return text